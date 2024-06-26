from app import Log
import time
import importlib

def setStatus(id):
    filename = f'./uploads/{id}/status'

    try:
        with open(filename, 'r') as file:
            # File exists, now overwrite its contents with "Finished"
            pass
        with open(filename, 'w') as file:
            file.write("Finished")
    except FileNotFoundError:
        # File does not exist, create it and write "Working"
        with open(filename, 'w') as file:
            file.write("Working")

def generateLdr(id, plugins):
    Log.info(f"[\033[34m{id}\033[0m] Setting working status")
    
    setStatus(id)

    # Run Payload mods
    for plugin in plugins["payload_mods"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        time.sleep(1) # emulate running plugin
        importlib.import_module(plugPath).run()

    # Run Keying
    for plugin in plugins["keying"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        time.sleep(1) # emulate running plugin
        importlib.import_module(plugPath).run()

    # Run Execution
    for plugin in plugins["execution"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        time.sleep(1) # emulate running plugin
        importlib.import_module(plugPath).run()

    # Run Pre Compilation
    for plugin in plugins["pre_comp"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        time.sleep(1) # emulate running plugin
        importlib.import_module(plugPath).run()

    # Run Post Compilation
    for plugin in plugins["post_comp"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        time.sleep(1) # emulate running plugin
        importlib.import_module(plugPath).run()

    # Mimic compiled binary
    with open(f'./uploads/{id}/result', 'w') as file:
        file.write("LOADER")

    Log.info(f"[\033[34m{id}\033[0m] Work done, updating status")

    setStatus(id) 