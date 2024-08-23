import subprocess

def desc():
    return "File Bloating"

def run():
    bloat_size = 200

    make_process = subprocess.run(
        f"dd if=/dev/zero bs=1M count={bloat_size} >> ./result.exe",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        check=True,
        text=True
    )
    
    return