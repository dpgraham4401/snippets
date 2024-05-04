import os
import subprocess

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# List the contents of the current working directory
print("Directory contents:")
for file in os.listdir(cwd):
    print(file)

# Call a subprocess
subprocess.run(["ls", "-l"])
