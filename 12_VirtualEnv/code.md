# Python Virtual Environment Cheatsheet

## 1. Check Python version
`python --version`

or

`py --version`

---

## 2. Check pip version
`pip --version`

---

## 3. Create a new virtual environment
`python -m venv .venv`

---

## 4. Activate the virtual environment

### Windows (PowerShell)

If your folder is named **.venv**

`.\.venv\Scripts\Activate.ps1`

---

### Windows (Command Prompt)

If your folder is named **.venv**

`.venv\Scripts\activate`

---

## 5. Verify that the virtual environment is active

`python --version`

or

`where python`

---

## 6. Upgrade pip

`python -m pip install --upgrade pip`

---

## 7. Install a package

`pip install package_name`

Example:

`pip install requests`

`pip install pymongo`

`pip install flask`

---

## 8. Install multiple packages

`pip install requests pymongo flask`

---

## 9. Check installed packages

`pip list`

---

## 10. Show package information

`pip show package_name`

Example:

`pip show requests`

---

## 11. Save installed packages to requirements.txt

`pip freeze > requirements.txt`

or

`pip list --format=freeze > requirements.txt`

---

## 12. Install packages from requirements.txt

`pip install -r requirements.txt`

---

## 13. Uninstall a package

`pip uninstall package_name`

Example:

`pip uninstall requests`

---

## 14. Run a Python file

`python filename.py`

Example:

`python main.py`

---

## 15. Deactivate the virtual environment

`deactivate`

---

## 16. Delete the virtual environment

### Windows

`rmdir /s /q venv`

or

`rmdir /s /q .venv`

### macOS/Linux

`rm -rf venv`

---

# Using virtualenv (Optional)

## Install virtualenv

`python -m pip install virtualenv`

---

## Check virtualenv version

`python -m virtualenv --version`

---

## Create a virtual environment using virtualenv

`python -m virtualenv venv`

---

## Activate (PowerShell)

`.\venv\Scripts\Activate.ps1`

---

## Deactivate

`deactivate`

---

# Useful pip Commands

## Upgrade a package

`pip install --upgrade package_name`

Example:

`pip install --upgrade requests`

---

## Upgrade pip

`python -m pip install --upgrade pip`

---

## List outdated packages

`pip list --outdated`

---

## Search installed packages

`pip list`

---

## Show all installed packages

`pip freeze`

---

## Install a specific version

`pip install package_name==version`

Example:

`pip install requests==2.32.3`

---

## Install the latest version

`pip install -U package_name`

---

## Check where Python is installed

### Windows

`where python`

### macOS/Linux

`which python`

---

## Check current virtual environment

### Windows

`echo %VIRTUAL_ENV%`

### PowerShell

`$env:VIRTUAL_ENV`

### macOS/Linux

`echo $VIRTUAL_ENV`

---

# Complete Workflow

## Go to project folder

`cd path_to_project`

## Create virtual environment

`python -m venv .venv`

## Activate

`.\.venv\Scripts\Activate.ps1`

## Upgrade pip

`python -m pip install --upgrade pip`

## Install packages

`pip install requests pymongo`

## Check installed packages

`pip list`

## Run the project

`python main.py`

## Save dependencies

`pip freeze > requirements.txt`

## Deactivate

`deactivate`