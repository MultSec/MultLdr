ProjectName		= result

CCX64			= x86_64-w64-mingw32-gcc

CFLAGS			=  -Os -fno-asynchronous-unwind-tables
CFLAGS 			+= -fno-ident -fpack-struct=8 -falign-functions=1
CFLAGS  		+= -s -ffunction-sections -falign-jumps=1 -w
CFLAGS			+= -Wl,-s,--no-seh,--enable-stdcall-fixup
CLIBS			=

SOURCES			=  src/*.c

all: x64

x64:
	@ $(CCX64) $(SOURCES) $(CFLAGS) $(CLIBS) -o $(ProjectName).exe
