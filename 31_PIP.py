import subprocess
import sys

try:
    import pip
    print("PIP is installed.")
    print(f"PIP version: {pip.__version__}")
except ImportError:
    print("PIP is not installed.")
