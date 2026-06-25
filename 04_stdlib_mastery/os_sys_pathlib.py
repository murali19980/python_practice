"""
Practice: os, sys, pathlib
"""
import os
from pathlib import Path

def pathlib_demo():
    p = Path("test_folder")
    p.mkdir(exist_ok=True)
    print(f"Created/verified folder: {p.absolute()}")

    py_files = list(Path(".").glob("*.py"))
    print(f"Python files in current dir: {[f.name for f in py_files]}")

    joined = Path("parent") / "child" / "file.txt"
    print(f"Joined path: {joined}")

def os_demo():
    print(f"Current working dir: {os.getcwd()}")
    os.chdir("test_folder")
    with open("dummy.txt", "w") as f:
        f.write("Hello")
    print(f"Absolute path: {os.path.abspath('dummy.txt')}")
    
    # Cleanup to keep workspace clean
    if os.path.exists("dummy.txt"):
        os.remove("dummy.txt")
    os.chdir("..")
    if os.path.exists("test_folder"):
        os.rmdir("test_folder")

if __name__ == "__main__":
    pathlib_demo()
    os_demo()
