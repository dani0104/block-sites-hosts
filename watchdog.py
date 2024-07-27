import os
import time
import subprocess

script_name = "block_sites.py"

def is_script_running(script_name):
    try:
        output = subprocess.check_output(f'tasklist /FI "IMAGENAME eq python.exe" /FI "WINDOWTITLE eq {script_name}"', shell=True)
        return script_name in str(output)
    except subprocess.CalledProcessError:
        return False

def start_script(script_name):
    subprocess.Popen(["python", script_name], creationflags=subprocess.CREATE_NEW_CONSOLE)

def main():
    while True:
        if not is_script_running(script_name):
            print(f"{script_name} is not running. Starting it...")
            start_script(script_name)
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
