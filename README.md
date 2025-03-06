# pipreqs-auto

## 📌 Overview

`pipreqs-auto` is a Python automation script designed to simplify dependency management in Python projects. It intelligently extracts required packages using `pipreqs`, resolves sub-dependencies with `pip-tools`, and optionally installs them—all in one execution.

## 🚀 Features
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
- Extracts dependencies from Python files and Jupyter notebooks.
- Resolves sub-packages and generates `requirements.txt`.
- Installs all dependencies.

### Configuration

Modify the `main()` function in `manage_pip_packages.py` to:
- Disable Jupyter Notebook scanning (`scan_notebooks = False`).
- Skip dependency installation (`install_deps = False`).

## 🛠 Dependencies

Ensure you have Python installed. The script automatically installs:
- `pipreqs`
- `pip-tools`

## 📜 License

This project is licensed under the MIT License.

