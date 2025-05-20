# Setup
This describes setup for project developpment.  
NOTE: This project has been designed in Visual Studio Code IDE. It is not mandatory using this IDE. We preferably use a bash terminal. All commands that follows are described for such a terminal.  

## Init setup
Create a project root dir environment variable:
```bash
cd </path/to/git/project/root_dir>
export _project_root="$(pwd)"
echo ${_project_root}
```

This project is written in Python language. We need Python to run it.  
[Python Download](https://www.python.org/downloads/)  

Check Python works, with command:  
```bash
py --version
# OR
python --version
```

Check Pip works, with command:  
```bash
py -m pip --version
# OR
python -m pip --version
```

Development is done in a virtual environment.  
Create virtual environment:  
```bash
py -m venv "${_project_root}/.venv"
# Adding src and tst in PYTHONPATH
echo "export PYTHONPATH=\"${_project_root}/src\":\"${_project_root}/tst\"" >> "${_project_root}/.venv/Scripts/activate"
```

## Start dev
```bash
. "${_project_root}/.venv/Scripts/activate"
pip install -r "${_project_root}/requirements.txt"
```

## Stop dev
```bash
deactivate
```

## Launch tests
```bash
python -m unittest discover -s "${_project_root}/tst"
python -m unittest <test_module.test_class>
python -m unittest <test_module.test_class.test_method>
```

## Save dependencies
```bash
pip install <something>
pip freeze -l > "${_project_root}/requirements.txt"
```
