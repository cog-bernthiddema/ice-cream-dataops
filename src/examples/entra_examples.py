"""
Example usage scripts for the EntraIDHelper class.
Each example shows how to perform specific operations independently.
"""
import asyncio
import logging
import sys
import os

# Add the src directory to the path so we can import our helper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entra_id_helper import EntraIDHelper, create_app_with_secret, assign_existing_app_to_groups

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def example_create_app_only():
    """Example: Create an application only."""
    print("\n=== Creating Application Only ===")
    
    helper = EntraIDHelper()
    
    try:
        app = await helper.create_application("Test App - Created via Python")
        print(f"✅ Created app: {app.display_name}")
        print(f"   App ID: {app.app_id}")
        print(f"   Object ID: {app.id}")
        
        return app
        
    except Exception as e:
        print(f"❌ Failed to create app: {e}")
        return None


async def example_add_secret_to_existing_app():
    """Example: Add a secret to an existing application."""
    print("\n=== Adding Secret to Existing App ===")
    
    helper = EntraIDHelper()
    
    # First, find an existing app (or use the one we just created)
    app_name = "Test App - Created via Python"
    
    try:
        app = await helper.find_application_by_name(app_name)
        if not app:
            print(f"❌ App '{app_name}' not found. Create it first.")
            return None
        
        print(f"📱 Found app: {app.display_name}")
        
        # Add a secret
        secret_info = await helper.add_client_secret(app.id, "Secret added later")
        
        print(f"✅ Added secret to app")
        print(f"   Secret ID: {secret_info['secret_id']}")
        print(f"   Secret Value: {secret_info['secret_value']}")
        print("   ⚠️ Save the secret value - it won't be shown again!")
        
        return secret_info
        
    except Exception as e:
        print(f"❌ Failed to add secret: {e}")
        return None


async def example_assign_app_to_groups():
    """Example: Assign an existing application to groups."""
    print("\n=== Assigning App to Groups ===")
    
    # You'll need to replace these with actual group names from your tenant
    app_id = "your-app-id-here"  # Replace with actual App ID
    group_names = ["Group1", "Group2"]  # Replace with actual group names
    
    print("⚠️ This example requires you to update the app_id and group_names variables")
    print(f"Current app_id: {app_id}")
    print(f"Current groups: {group_names}")
    
    if app_id == "your-app-id-here":
        print("❌ Please update the app_id variable with a real App ID")
        return
    
    try:
        results = await assign_existing_app_to_groups(app_id, group_names)
        
        print("📋 Assignment Results:")
        for group_name, success in results.items():
            status = "✅" if success else "❌"
            print(f"   {status} {group_name}")
            
    except Exception as e:
        print(f"❌ Failed to assign app to groups: {e}")


async def example_find_app_by_id():
    """Example: Find an application by its App ID."""
    print("\n=== Finding App by App ID ===")
    
    app_id = "your-app-id-here"  # Replace with actual App ID
    
    if app_id == "your-app-id-here":
        print("❌ Please update the app_id variable with a real App ID")
        return None
    
    helper = EntraIDHelper()
    
    try:
        app = await helper.find_application_by_app_id(app_id)
        
        if app:
            print(f"✅ Found app: {app.display_name}")
            print(f"   App ID: {app.app_id}")
            print(f"   Object ID: {app.id}")
            return app
        else:
            print(f"❌ App with ID {app_id} not found")
            return None
            
    except Exception as e:
        print(f"❌ Failed to find app: {e}")
        return None


async def example_list_app_groups():
    """Example: List all groups an app belongs to."""
    print("\n=== Listing App Group Memberships ===")
    
    app_id = "your-app-id-here"  # Replace with actual App ID
    
    if app_id == "your-app-id-here":
        print("❌ Please update the app_id variable with a real App ID")
        return
    
    helper = EntraIDHelper()
    
    try:
        groups = await helper.list_app_group_memberships(app_id)
        
        if groups:
            print(f"✅ App belongs to {len(groups)} groups:")
            for group in groups:
                print(f"   • {group['display_name']} (ID: {group['id']})")
        else:
            print("📋 App doesn't belong to any groups")
            
    except Exception as e:
        print(f"❌ Failed to list app groups: {e}")


async def example_complete_workflow():
    """Example: Complete workflow - create app, add secret, assign to groups."""
    print("\n=== Complete Workflow Example ===")
    
    try:
        # Step 1: Create app with secret
        app_info = await create_app_with_secret("Complete Workflow Test App", "Initial secret")
        
        print(f"✅ Created app with secret:")
        print(f"   App Name: {app_info['display_name']}")
        print(f"   App ID: {app_info['app_id']}")
        print(f"   Secret: {app_info['secret']['secret_value']}")
        
        # Step 2: Assign to groups (you'll need to update group names)
        group_names = ["Group1", "Group2"]  # Replace with real group names
        print(f"\n⚠️ To complete this example, update group_names with real groups from your tenant")
        print(f"Current groups: {group_names}")
        
        # Uncomment the lines below when you have real group names:
        # results = await assign_existing_app_to_groups(app_info['app_id'], group_names)
        # print("\n📋 Group Assignment Results:")
        # for group_name, success in results.items():
        #     status = "✅" if success else "❌"
        #     print(f"   {status} {group_name}")
        
        return app_info
        
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        return None


async def main():
    """Run all examples."""
    print("🚀 Entra ID Helper Examples")
    print("=" * 50)
    
    # Make sure we're authenticated
    print("Prerequisites:")
    print("1. Run 'az login' to authenticate with Azure")
    print("2. Ensure you have appropriate permissions in Entra ID")
    print("3. Update example scripts with real App IDs and group names where needed")
    print()
    
    # Example 1: Create app only
    app = await example_create_app_only()
    
    # Example 2: Add secret to existing app (using the app we just created)
    if app:
        await example_add_secret_to_existing_app()
    
    # Example 3: Find app by ID (requires updating the script)
    await example_find_app_by_id()
    
    # Example 4: Assign app to groups (requires updating the script)
    await example_assign_app_to_groups()
    
    # Example 5: List app group memberships (requires updating the script)
    await example_list_app_groups()
    
    # Example 6: Complete workflow
    await example_complete_workflow()


if __name__ == "__main__":
    asyncio.run(main())