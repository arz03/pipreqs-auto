import os
import subprocess
import sys

# Configuration variables
scan_notebooks = True  # Set this to False if you don't want to scan Jupyter notebooks
install_deps = True  # Set this to False if you don't want to install dependencies after generation

def create_virtual_environment():
    """Create and activate a virtual environment automatically if it doesn't exist."""
    if os.path.exists("venv"):
        print("Virtual environment already exists. Activating...")
    else:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("Virtual environment created successfully.")
    
    if sys.platform == "win32":
        activate_script = os.path.join("venv", "Scripts", "activate")
        subprocess.run([activate_script], shell=True)
    else:
        activate_script = "source venv/bin/activate"
        subprocess.run(["bash", "-c", activate_script], check=True)
    
    print("Virtual environment activated.")

def install_packages():
    """Ensure pipreqs and pip-tools are installed."""
    required_packages = ["pipreqs", "pip-tools"]
    for package in required_packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

def generate_requirements(project_path="."):
    """Generate a deterministic requirements.txt from the project dependencies."""
    requirements_in = os.path.join(project_path, "requirements.in")
    
    # Construct pipreqs command
    pipreqs_command = ["pipreqs", project_path, "--force", "--savepath", requirements_in]
    if scan_notebooks:
        pipreqs_command.append("--scan-notebooks")
    
    # Generate requirements.in using pipreqs
    subprocess.run(pipreqs_command, check=True)
    
    # Ensure requirements.in exists before compiling
    if os.path.exists(requirements_in):
        subprocess.run(["pip-compile", requirements_in], check=True)
    else:
        print("Error: requirements.in was not generated. Exiting.")
        sys.exit(1)

def install_dependencies():
    """Install dependencies from requirements.txt if required."""
    requirements_txt = "requirements.txt"
    if os.path.exists(requirements_txt):
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_txt], check=True)

def main():
    project_path = os.getcwd()  # Current working directory
    
    create_virtual_environment()
    install_packages()
    generate_requirements(project_path)
    print("\nSuccessfully generated requirements.txt with all dependencies.")
    if install_deps:
        install_dependencies()
        print("\nSuccessfully installed dependencies from requirements.txt.")

if __name__ == "__main__":
    main()
