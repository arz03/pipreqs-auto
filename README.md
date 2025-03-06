# pipreqs-auto

## 📌 Overview

`pipreqs-auto` is a Python automation script designed to simplify dependency management in Python projects. It intelligently extracts required packages using `pipreqs`, resolves sub-dependencies with `pip-tools`, and optionally installs them—all in one execution. It also automatically creates and activates a virtual environment before processing dependencies.

## 🚀 Features
- **Automated Virtual Environment Setup**: Creates and activates a `venv` automatically.
- **Automated Requirements Generation**: Uses `pipreqs` to extract project dependencies.
- **Sub-dependency Resolution**: `pip-tools` ensures that all required sub-packages are included.
- **Jupyter Notebook Support**: Optionally scans `.ipynb` files for imports.
- **Automatic Installation**: Installs dependencies from `requirements.txt` if enabled.

## 📦 Installation

Clone the repository:

```sh
git clone https://github.com/arz03/pipreqs-auto.git
cd pipreqs-auto
```

## 🔧 Usage

Run the script:

```sh
python manage_pip_packages.py
```

By default, it:
- Creates and activates a virtual environment (`venv`).
- Extracts dependencies from Python files and Jupyter notebooks.
- Resolves sub-packages and generates `requirements.txt`.
- Installs all dependencies.

### Configuration

Modify the `manage_pip_packages.py` script to:
- Disable Jupyter Notebook scanning (`scan_notebooks = False`).
- Skip dependency installation (`install_deps = False`).

## 🛠 Dependencies

Ensure you have Python installed. The script automatically installs:
- `pipreqs`
- `pip-tools`

### Virtual Environment Manual Activation
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

## 📜 License

This project is licensed under the MIT License.
