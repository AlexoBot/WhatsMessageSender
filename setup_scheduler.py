import os
import sys
import subprocess
import getpass

def create_bat_file(script_dir, python_script_path, bat_file_path):
    """Create a .bat file to run the Python script."""
    python_exe = sys.executable  # Full path to current Python executable

    bat_content = f'@echo off\n"{python_exe}" "{python_script_path}"\npause\n'

    with open(bat_file_path, 'w') as f:
        f.write(bat_content)

    print(f"Created BAT file: {bat_file_path}")

def setup_task_scheduler(bat_file_path, task_name="WhatsAppPlanner", start_time="09:00"):
    """Set up Windows Task Scheduler to run the BAT file daily."""
    username = getpass.getuser()

    # schtasks command to create daily task
    cmd = [
        'schtasks', '/create', '/tn', task_name, '/tr', f'"{bat_file_path}"',
        '/sc', 'daily', '/st', start_time, '/ru', username, '/rl', 'highest',
        '/f'  # Force overwrite if exists
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print(f"Task Scheduler configured successfully: {task_name}")
            print(f"Task will run daily at {start_time}")
        else:
            print("Failed to create task:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
    except Exception as e:
        print(f"Error setting up Task Scheduler: {e}")

def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Assume .py is in the same directory
    python_script_path = os.path.join(script_dir, 'Main.py')

    if not os.path.exists(python_script_path):
        print(f"Error: {python_script_path} not found.")
        return

    # BAT file path
    bat_file_path = os.path.join(script_dir, 'run_planner.bat')

    # Create BAT file
    create_bat_file(script_dir, python_script_path, bat_file_path)

    # Prompt for start time
    start_time = input("Enter the daily start time (HH:MM, default 09:00): ").strip()
    if not start_time:
        start_time = "09:00"

    # Validate time format
    try:
        hours, minutes = map(int, start_time.split(':'))
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            raise ValueError
    except ValueError:
        print("Invalid time format. Using default 09:00")
        start_time = "09:00"

    # Setup Task Scheduler
    setup_task_scheduler(bat_file_path, start_time=start_time)

if __name__ == '__main__':
    main()