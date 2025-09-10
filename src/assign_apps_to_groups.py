"""
Standalone script to assign existing Entra ID applications to groups.
Perfect for when you already have apps and secrets but need to assign them to groups.
"""
import asyncio
import logging
import sys
import os
from typing import List, Dict

# Add the src directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from entra_id_helper import EntraIDHelper

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def assign_apps_to_groups(app_configs: List[Dict[str, any]]) -> None:
    """
    Assign multiple applications to their respective groups.
    
    Args:
        app_configs: List of dictionaries with 'app_id' and 'groups' keys
                    Example: [{"app_id": "abc123", "groups": ["Group1", "Group2"]}]
    """
    helper = EntraIDHelper()
    
    print(f"🚀 Starting group assignment for {len(app_configs)} applications...")
    
    for config in app_configs:
        app_id = config.get('app_id')
        group_names = config.get('groups', [])
        
        if not app_id:
            logger.warning("Skipping config without app_id")
            continue
            
        if not group_names:
            logger.warning(f"No groups specified for app {app_id}")
            continue
        
        print(f"\n📱 Processing app: {app_id}")
        print(f"   Target groups: {', '.join(group_names)}")
        
        # Verify app exists
        app = await helper.find_application_by_app_id(app_id)
        if not app:
            print(f"   ❌ App {app_id} not found - skipping")
            continue
            
        print(f"   ✅ Found app: {app.display_name}")
        
        # Assign to each group
        success_count = 0
        for group_name in group_names:
            try:
                # Find group
                group = await helper.find_group_by_name(group_name)
                if not group:
                    print(f"   ❌ Group '{group_name}' not found")
                    continue
                
                # Assign app to group
                success = await helper.add_app_to_group(app_id, group['id'])
                if success:
                    print(f"   ✅ Added to '{group_name}'")
                    success_count += 1
                else:
                    print(f"   ❌ Failed to add to '{group_name}'")
                    
            except Exception as e:
                print(f"   ❌ Error assigning to '{group_name}': {e}")
        
        print(f"   📊 Successfully assigned to {success_count}/{len(group_names)} groups")


async def main():
    """Main function with example configurations."""
    
    print("🔧 Entra ID App-to-Group Assignment Tool")
    print("=" * 50)
    
    # Example configurations - UPDATE THESE WITH YOUR REAL VALUES
    app_configs = [
        {
            "app_id": "your-first-app-id-here",
            "groups": ["group name"]
        },
        {
            "app_id": "your-second-app-id-here", 
            "groups": ["group name"]
        }
        # Add more app configurations as needed
    ]
    
    # Check if user has updated the configurations
    if any(config['app_id'].startswith('your-') for config in app_configs):
        print("⚠️  CONFIGURATION NEEDED")
        print("Please update the app_configs list in this script with your real:")
        print("- App IDs (Client IDs) from your Entra ID applications")
        print("- Group names that exist in your tenant")
        print()
        print("Example configuration:")
        print("""
app_configs = [
    {
        "app_id": "12345678-1234-1234-1234-123456789abc",
        "groups": ["My Security Group", "API Consumers"]
    },
    {
        "app_id": "87654321-4321-4321-4321-fedcba987654",
        "groups": ["Production Access", "Monitoring Tools"]
    }
]
        """)
        print()
        print("After updating, run: python assign_apps_to_groups.py")
        return
    
    # Prerequisites check
    print("Prerequisites:")
    print("✓ Run 'az login' to authenticate")
    print("✓ Ensure you have Application.ReadWrite.All and GroupMember.ReadWrite.All permissions")
    print("✓ Update app_configs with your real App IDs and group names")
    print()
    
    try:
        await assign_apps_to_groups(app_configs)
        print(f"\n🎉 Assignment process completed!")
        
    except Exception as e:
        print(f"\n❌ Process failed: {e}")
        logger.exception("Full error details:")


if __name__ == "__main__":
    asyncio.run(main())