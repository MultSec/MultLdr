from app import Log
import time

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
    Log.info(f"[{id}] Setting working status")
    
    setStatus(id)

    for i in range(10):
        Log.info(f"[{id}] Working... {i + 1}/10")
        time.sleep(1)

    # Mimic compiled binary
    with open(f'./uploads/{id}/result', 'w') as file:
        file.write("LOADER")

    Log.info(f"[{id}] Work done, updating status")

    setStatus(id)

