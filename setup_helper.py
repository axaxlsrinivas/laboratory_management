import os
import sys
import platform
import subprocess

def run_command(cmd, shell=True):
    print(f"\nRunning: {cmd}")
    result = subprocess.run(cmd, shell=shell)
    if result.returncode != 0:
        print(f"Error running: {cmd}")
        sys.exit(result.returncode)

def main():
    print("\n=== Laboratory Management Setup Helper ===\n")
    # 1. Create virtual environment
    if platform.system() == 'Windows':
        venv_cmd = 'python -m venv venv'
        activate_cmd = '.\\venv\\Scripts\\activate'
    else:
        venv_cmd = 'python3 -m venv venv'
        activate_cmd = 'source ./venv/bin/activate'
    if not os.path.exists('venv'):
        run_command(venv_cmd)
    print(f"\nActivate your environment with: {activate_cmd}")
    # 2. Install requirements
    pip_cmd = 'pip install -r requirements.txt' if platform.system() == 'Windows' else 'pip3 install -r requirements.txt'
    run_command(pip_cmd)
    # 3. Initialize database
    run_command(f'{sys.executable} run.py')
    # 4. Insert sample data
    run_command(f'{sys.executable} app/db/insert_sample_data.py')
    # 5. Train AI model
    run_command(f'{sys.executable} app/cli/testcli.py train-item-model')
    print("\nSetup complete! To start the web app, run:")
    print(f"{sys.executable} user_interface/lab_management_app.py")
    print("\nThen open http://127.0.0.1:5000/ in your browser.")

if __name__ == "__main__":
    main()
