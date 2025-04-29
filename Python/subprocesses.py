import subprocess
from pathlib import Path

# Get the current working directory
cwd = Path.cwd()
print(f"Current working directory: {cwd}")

# List the contents of the current working directory
print("Directory contents:")
for file in Path.cwd().iterdir():
    print(file)

# Call a subprocess
subprocess.run(["ls", "-l"])
