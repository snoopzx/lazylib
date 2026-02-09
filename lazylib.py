import sys
import subprocess
import ast
import os
import platform

def get_required_libraries(file_path):
    libraries = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    libraries.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    libraries.add(node.module.split('.')[0])
    except Exception:
        sys.exit(1)
    return libraries

def setup_and_reboot():
    venv_dir = "venv"
    is_windows = platform.system().lower() == "windows"
    
    if not os.path.exists(venv_dir):
        print(f"[*] Creating Virtual Environment in ./{venv_dir}...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)    
    if is_windows:
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(venv_dir, "bin", "python")

    print("[+] venv is ready. Running inside the environment...")    
    subprocess.run([venv_python] + sys.argv)
    sys.exit(0)

def install_and_run(target_script):
    if not os.path.exists(target_script):
        print(f"Error: {target_script} not found.")
        return
    is_venv = sys.prefix != sys.base_prefix
    is_windows = platform.system().lower() == "windows"
    if not is_windows and not is_venv:
        setup_and_reboot()
    libs = get_required_libraries(target_script)
    for lib in libs:
        try:
            print(f"[*] Checking/Installing: {lib}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        except subprocess.CalledProcessError:
            continue
    print(f"\n[+] All libraries ready. Executing {target_script}...\n")
    subprocess.run([sys.executable, target_script])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lazylib.py <script.py>")
    else:
        install_and_run(sys.argv[1])
