import os
import shutil
import importlib

class Logger:
    @staticmethod
    def info(message):
        print(f"[\033[34m*\033[0m] {message}")

    @staticmethod
    def success(message):
        print(f"[\033[32m+\033[0m] {message}")

    @staticmethod
    def debug(message):
        print(f"[\033[33m^\033[0m] {message}")

    @staticmethod
    def error(message):
        print(f"[\033[31m!\033[0m] {message}")

    @staticmethod
    def section(message):
        print(f"\t[\033[93m-\033[0m] {message}")

    @staticmethod
    def subsection(message):
        print(f"\t\t[\033[95m>\033[0m] {message}")

# Init logger
Log = Logger()

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

def setTemplate(id):

    os.makedirs(f'./uploads/{id}/src/')

    filename = f'./uploads/{id}/src/main.c'

    template = '''\
#include <windows.h>
{{LIBS}}

{{FUNCTIONS}}

__attribute__((section(".text#"))) \
const unsigned char shellcode[] = {
{{SHELLCODE}}
};

int main() {
{{KEYING}}

{{PAYLOAD_MODS}}

{{EXECUTION}}

	return 0;
}\
'''

    with open(filename, 'w') as file:
        file.write(template)

def cleanTemplate(id):
    filename = f'./uploads/{id}/src/main.c'

    # Open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
    
    # Clean Template
    content = content.replace('\n{{LIBS}}\n', '')
    content = content.replace('\n{{FUNCTIONS}}', '')
    content = content.replace('\n{{SHELLCODE}}', '')
    content = content.replace('\n{{KEYING}}', '')
    content = content.replace('\n{{PAYLOAD_MODS}}', '')
    content = content.replace('\n{{EXECUTION}}', '')

    # Open the file in write mode and write the modified content
    with open(filename, 'w') as file:
        file.write(content)

def generateLdr(id, plugins):
    Log.info(f"[\033[34m{id}\033[0m] Setting working status")
    
    setStatus(id)

    Log.info(f"[\033[34m{id}\033[0m] Setting template")
    
    setTemplate(id)

    Log.info(f"[\033[34m{id}\033[0m] Running plugins")

    # Run Keying
    for plugin in plugins["keying"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        importlib.import_module(plugPath).run()
        
    # Run Payload mods
    for plugin in plugins["payload_mods"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        importlib.import_module(plugPath).run()

    # Run Execution
    for plugin in plugins["execution"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        importlib.import_module(plugPath).run()

    # Run Pre Compilation
    for plugin in plugins["pre_comp"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        importlib.import_module(plugPath).run()

    # Run Post Compilation
    for plugin in plugins["post_comp"]:
        plugPath = "plugins" + plugin.replace("/", ".") + ".run"
        Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
        importlib.import_module(plugPath).run()

    Log.info(f"[\033[34m{id}\033[0m] Cleaning up template")
    cleanTemplate(id)

    Log.info(f"[\033[34m{id}\033[0m] Compiling loader")
    with open(f'./uploads/{id}/result', 'w') as file:
        file.write("LOADER")

    Log.info(f"[\033[34m{id}\033[0m] Work done, updating status")

    setStatus(id) 

if __name__ == "__main__":
    id = "dahhfdgsfjhagfdjgawhriweancvbasdf"

    os.makedirs(f'./uploads/{id}')

    plugins = {
                "execution": [
                    
                ],
                "keying": [
                    
                ],
                "payload_mods": [
                    
                ],
                "post_comp": [
                    
                ],
                "pre_comp": [
                    
                ]
            }

    generateLdr(id, plugins)

    # Remove directory
    Log.info(f"[\033[34m{id}\033[0m] Removing temp dir")
    #shutil.rmtree(f'./uploads/{id}')