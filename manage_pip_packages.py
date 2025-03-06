import os
import subprocess
import sys

# Global configuration variables
scan_notebooks = True  # Set this to False if you don't want to scan Jupyter notebooks
install_deps = True  # Set this to False if you don't want to install dependencies after generation

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
    
    # Compile requirements.txt using pip-tools
    subprocess.run(["pip-compile", requirements_in], check=True)

def install_dependencies():
    """Install dependencies from requirements.txt if required."""
    requirements_txt = "requirements.txt"
    if os.path.exists(requirements_txt):
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_txt], check=True)

def main():
    project_path = os.getcwd()  # Current working directory
    
    install_packages()
    generate_requirements(project_path)
    
    if install_deps:
        install_dependencies()
    
    print("\nSuccessfully generated requirements.txt with all dependencies.")
    if install_deps:
        print("\nSuccessfully installed dependencies from requirements.txt.")

if __name__ == "__main__":
    main()
