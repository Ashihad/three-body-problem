# Three Body Problem Simulator
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

4) Once done, disable virtual environment
```
deactivate
```

## Documentation generation
Since documentation is being generated for both html and Latex targets ensure that you have `tex` and `doxygen` packages installed.

Example installation command (for Debian-based Linux systems):
```
# NOTE: this will take a while to run
sudo apt update && sudo apt install doxygen texlive-full
```

NOTE: commands below have been turned into a handy script `generate_documentation.sh`, use it instead for quick documentation generation (make sure you set correct file permissions).

Once packages are installed you can proceed with generating documentation with following command:
```
doxygen Doxyfile
```

This will create a directory `docs/` with subdirectories `html/` and `latex/`. Html version is ready to view, simply open `index.html` in your preeferred browser.

To compile `tex` and generate a .pdf documentation file run following commands:
```
cd docs/latex
make
```
This will generate `refman.pdf` file in `docs/latex/` directory.


To open it run following generic command:
```
open refman.pdf
```