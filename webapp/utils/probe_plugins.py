import os
import json

def get_plugins(plugin_dir='./plugins'):
    plugins = {}

    # Iterate over the categories
    for category in os.listdir(plugin_dir):
        category_path = os.path.join(plugin_dir, category)

        # Check if it's a directory
        if os.path.isdir(category_path):
            plugins[category] = {}

            # Iterate over the subcategories
            for subcategory in os.listdir(category_path):
                subcategory_path = os.path.join(category_path, subcategory)

                # Check if it's a directory
                if os.path.isdir(subcategory_path):
                    plugins[category][subcategory] = [
                        plugin for plugin in os.listdir(subcategory_path)
                        if os.path.isdir(os.path.join(subcategory_path, plugin))
                    ]

    return json.dumps(plugins)
