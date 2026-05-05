#!/usr/bin/env python3
import os
import shutil

# Change to the repository directory
os.chdir(r'C:\Users\eykgo\Downloads\hawaiian-wiring-tech')

# Check current files
print("Current files in directory:")
for file in os.listdir('.'):
    if file.endswith('.png'):
        print(f"  {file} - {os.path.getsize(file)} bytes")

# Rename electrician.png.png to electrician.png
if os.path.exists('electrician.png.png'):
    print("\nRenaming electrician.png.png to electrician.png...")
    os.rename('electrician.png.png', 'electrician.png')
    print("Success! File renamed.")
    print(f"  electrician.png - {os.path.getsize('electrician.png')} bytes")
else:
    print("ERROR: electrician.png.png not found!")

# Now run git commands
print("\nAdding and committing changes...")
import subprocess
try:
    subprocess.run(['git', 'add', '-A'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Fix: rename electrician.png.png to electrician.png'], check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    print("Success! Changes pushed to GitHub.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
