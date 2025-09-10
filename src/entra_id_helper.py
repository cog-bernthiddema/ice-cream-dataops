"""
Modular helper for Microsoft Entra ID operations using Microsoft Graph API.
Allows independent execution of app creation, secret management, and group assignments.
"""
import asyncio
import logging
from typing import Optional, List, Dict, Any
from azure.identity import DefaultAzureCredential
from msgraph import GraphServiceClient
from msgraph.generated.models.application import Application
from msgraph.generated.models.service_principal import ServicePrincipal
from msgraph.generated.models.password_credential import PasswordCredential
from msgraph.generated.applications.item.add_password.add_password_post_request_body import AddPasswordPostRequestBody


class EntraIDHelper:
    """Helper class for Microsoft Entra ID operations."""
    
    def __init__(self, tenant_id: Optional[str] = None):
        """
        Initialize the Entra ID helper.
        
        Args:
            tenant_id: Optional tenant ID. If not provided, uses default from Azure CLI.
        """
        self.credential = DefaultAzureCredential()
        self.client = GraphServiceClient(credentials=self.credential)
        self.tenant_id = tenant_id
        self.logger = logging.getLogger(__name__)
        
    async def create_application(self, display_name: str, sign_in_audience: str = "AzureADMyOrg") -> Application:
        """
        Create a new Entra ID application.
        
        Args:
            display_name: Name for the application
            sign_in_audience: Who can sign in ("AzureADMyOrg", "AzureADMultipleOrgs", etc.)
            
        Returns:
            Application object with details of created app
        """
        try:
            request_body = Application(
                display_name=display_name,
                sign_in_audience=sign_in_audience
            )
            
            app = await self.client.applications.post(request_body)
            self.logger.info(f"Created application: {app.display_name} (App ID: {app.app_id})")
            return app
            
        except Exception as e:
            self.logger.error(f"Failed to create application {display_name}: {str(e)}")
            raise

    async def find_application_by_name(self, display_name: str) -> Optional[Application]:
        """
        Find an application by its display name.
        
        Args:
            display_name: Name of the application to find
            
        Returns:
            Application object if found, None otherwise
        """
        try:
            apps = await self.client.applications.get(
                request_configuration=lambda config: setattr(
                    config.query_parameters, 'filter', f"displayName eq '{display_name}'"
                )
            )
            
            if apps and apps.value:
                return apps.value[0]
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to find application {display_name}: {str(e)}")
            return None

    async def find_application_by_app_id(self, app_id: str) -> Optional[Application]:
        """
        Find an application by its App ID (Client ID).
        
        Args:
            app_id: The App ID (Client ID) of the application
            
        Returns:
            Application object if found, None otherwise
        """
        try:
            apps = await self.client.applications.get(
                request_configuration=lambda config: setattr(
                    config.query_parameters, 'filter', f"appId eq '{app_id}'"
                )
            )
            
            if apps and apps.value:
                return apps.value[0]
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to find application with App ID {app_id}: {str(e)}")
            return None

    async def add_client_secret(self, application_id: str, secret_description: str = "Auto-generated secret") -> Dict[str, Any]:
        """
        Add a client secret to an existing application.
        
        Args:
            application_id: The Object ID of the application (not App ID)
            secret_description: Description for the secret
            
        Returns:
            Dictionary with secret details including the secret value
        """
        try:
            request_body = AddPasswordPostRequestBody(
                password_credential=PasswordCredential(
                    display_name=secret_description
                )
            )
            
            secret = await self.client.applications.by_application_id(application_id).add_password.post(request_body)
            
            result = {
                "secret_id": secret.key_id,
                "secret_value": secret.secret_text,
                "display_name": secret.display_name,
                "start_date_time": secret.start_date_time,
                "end_date_time": secret.end_date_time
            }
            
            self.logger.info(f"Created secret for application {application_id}")
            self.logger.warning("Secret value will only be shown once - save it securely!")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Failed to add secret to application {application_id}: {str(e)}")
            raise

    async def get_or_create_service_principal(self, app_id: str) -> ServicePrincipal:
        """
        Get existing service principal or create one for the given App ID.
        
        Args:
            app_id: The App ID (Client ID) of the application
            
        Returns:
            ServicePrincipal object
        """
        try:
            # Try to find existing service principal
            service_principals = await self.client.service_principals.get(
                request_configuration=lambda config: setattr(
                    config.query_parameters, 'filter', f"appId eq '{app_id}'"
                )
            )
            
            if service_principals and service_principals.value:
                self.logger.info(f"Found existing service principal for app {app_id}")
                return service_principals.value[0]
            
            # Create new service principal
            sp_request = ServicePrincipal(app_id=app_id)
            service_principal = await self.client.service_principals.post(sp_request)
            
            self.logger.info(f"Created service principal for app {app_id}")
            return service_principal
            
        except Exception as e:
            self.logger.error(f"Failed to get/create service principal for app {app_id}: {str(e)}")
            raise

    async def add_app_to_group(self, app_id: str, group_id: str) -> bool:
        """
        Add an application (via its service principal) to a group.
        
        Args:
            app_id: The App ID (Client ID) of the application
            group_id: The Object ID of the group
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure service principal exists
            service_principal = await self.get_or_create_service_principal(app_id)
            
            # Add service principal to group
            request_body = {
                "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{service_principal.id}"
            }
            
            await self.client.groups.by_group_id(group_id).members.ref.post(request_body)
            
            self.logger.info(f"Added app {app_id} to group {group_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to add app {app_id} to group {group_id}: {str(e)}")
            return False

    async def remove_app_from_group(self, app_id: str, group_id: str) -> bool:
        """
        Remove an application from a group.
        
        Args:
            app_id: The App ID (Client ID) of the application
            group_id: The Object ID of the group
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Find service principal
            service_principals = await self.client.service_principals.get(
                request_configuration=lambda config: setattr(
                    config.query_parameters, 'filter', f"appId eq '{app_id}'"
                )
            )
            
            if not service_principals or not service_principals.value:
                self.logger.warning(f"No service principal found for app {app_id}")
                return False
            
            service_principal = service_principals.value[0]
            
            # Remove from group
            await self.client.groups.by_group_id(group_id).members.by_directory_object_id(service_principal.id).ref.delete()
            
            self.logger.info(f"Removed app {app_id} from group {group_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to remove app {app_id} from group {group_id}: {str(e)}")
            return False

    async def find_group_by_name(self, group_name: str) -> Optional[Dict[str, str]]:
        """
        Find a group by its display name.
        
        Args:
            group_name: Name of the group to find
            
        Returns:
            Dictionary with group details if found, None otherwise
        """
        try:
            groups = await self.client.groups.get(
                request_configuration=lambda config: setattr(
                    config.query_parameters, 'filter', f"displayName eq '{group_name}'"
                )
            )
            
            if groups and groups.value:
                group = groups.value[0]
                return {
                    "id": group.id,
                    "display_name": group.display_name,
                    "description": group.description
                }
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to find group {group_name}: {str(e)}")
            return None

    async def list_app_group_memberships(self, app_id: str) -> List[Dict[str, str]]:
        """
        List all groups that an application belongs to.
        
        Args:
            app_id: The App ID (Client ID) of the application
            
        Returns:
            List of group dictionaries
        """
        try:
            # Find service principal
            service_principals = await self.client.service_principals.get(
                request_configuration=lambda config: setattr(
                    config.query_parameters, 'filter', f"appId eq '{app_id}'"
                )
            )
            
            if not service_principals or not service_principals.value:
                self.logger.warning(f"No service principal found for app {app_id}")
                return []
            
            service_principal = service_principals.value[0]
            
            # Get group memberships
            memberships = await self.client.service_principals.by_service_principal_id(service_principal.id).member_of.get()
            
            groups = []
            if memberships and memberships.value:
                for membership in memberships.value:
                    if hasattr(membership, 'display_name'):  # It's a group
                        groups.append({
                            "id": membership.id,
                            "display_name": membership.display_name,
                            "description": getattr(membership, 'description', '')
                        })
            
            return groups
            
        except Exception as e:
            self.logger.error(f"Failed to list group memberships for app {app_id}: {str(e)}")
            return []


# Convenience functions for common operations
async def create_app_with_secret(display_name: str, secret_description: str = "Initial secret") -> Dict[str, Any]:
    """
    Convenience function to create an app and immediately add a secret.
    
    Returns:
        Dictionary with app details and secret information
    """
    helper = EntraIDHelper()
    
    # Create app
    app = await helper.create_application(display_name)
    
    # Add secret
    secret = await helper.add_client_secret(app.id, secret_description)
    
    return {
        "app_id": app.app_id,
        "object_id": app.id,
        "display_name": app.display_name,
        "secret": secret
    }


async def assign_existing_app_to_groups(app_id: str, group_names: List[str]) -> Dict[str, bool]:
    """
    Convenience function to assign an existing app to multiple groups by name.
    
    Args:
        app_id: The App ID (Client ID) of the application
        group_names: List of group names to assign the app to
        
    Returns:
        Dictionary mapping group names to success status
    """
    helper = EntraIDHelper()
    results = {}
    
    for group_name in group_names:
        try:
            # Find group by name
            group = await helper.find_group_by_name(group_name)
            if not group:
                results[group_name] = False
                continue
            
            # Add app to group
            success = await helper.add_app_to_group(app_id, group["id"])
            results[group_name] = success
            
        except Exception as e:
            logging.error(f"Failed to assign app to group {group_name}: {str(e)}")
            results[group_name] = False
    
    return results