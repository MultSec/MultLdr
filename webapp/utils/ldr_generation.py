from app import Log

def printPlugins(plugins):
    Log.info("Known Plugins retrieved from server: ")
    
    for key, elements in plugins:
        Log.info(f"{key}:")
        for element in elements:
            Log.info(f"{element}")