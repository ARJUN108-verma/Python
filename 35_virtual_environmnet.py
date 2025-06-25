import venv
import os
import subprocess

# 1. Define the environment name
env_dir = 'my_venv'

# 2. Create the virtual environment
builder = venv.EnvBuilder(with_pip=True)
builder.create(env_dir)

print(f"✅ Virtual environment created at: {os.path.abspath(env_dir)}")

# 3. Show how to activate it (platform-specific)
if os.name == 'nt':  # For Windows
    activation_command = f"{env_dir}\\Scripts\\activate.bat"
else:  # For Linux / macOS
    activation_command = f"source {env_dir}/bin/activate"

print("\n🔧 To activate the virtual environment, run:")
print(activation_command)

# 4. Show installed packages (initially empty except pip/setuptools)
print("\n📦 Installed packages in the new environment (using pip freeze):")
try:
    result = subprocess.run(
        [os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'pip'), 'freeze'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)
except Exception as e:
    print("⚠️ Could not show packages:", e)
