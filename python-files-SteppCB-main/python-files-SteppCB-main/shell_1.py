import subprocess

def run_shell_command(command):
    try:
        # Subprocess to run shell command 
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        
        # Printing the output
        print("Command Output:")
        print(result.stdout)
        
        # If there are errors, print the errors
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")
