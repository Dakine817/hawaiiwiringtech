#!/usr/bin/env python3
import subprocess
import os

# Change to the repository directory
os.chdir(r'C:\Users\eykgo\Downloads\hawaiian-wiring-tech')

# Run git commands
try:
    print("Adding changes...")
    subprocess.run(['git', 'add', '-A'], check=True)
    print("Committing changes...")
    subprocess.run(['git', 'commit', '-m', 'Replace with correct electrician image'], check=True)
    print("Pushing to GitHub...")
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    print("Success! Changes pushed to GitHub.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    input("Press Enter to exit...")
