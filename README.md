# Three body problem simulator
Simple program which simulates a three body problem evolution of a system.
Program performs many actions during runtime:
- solve a three body problem for a specified configuration
- plot detailed information about system evolution
- plot a phase diagram of a system
- create an animation of system's time evolution

## Setup
**Note: Python >=3.9 is required**

Dependency setup is rather standard if user is familiar with Python `venv` package.
1) Create and activate a virtual environment using builtin `venv` package
```
# this command creates a directory called ".venv" in current directory, which includes all necessary files
# name '.venv' is arbitrary, you can change it if you fancy doing so
python -m venv .venv

# activate virtual environment
source .venv/bin/activate
```
2) Download dependencies
```
pip install -r requirements.txt
```

3) Run the program
```
python main.py <configuration>
```

4) Disable virtual environment
```
deactivate
```