# Tetris Playing AI (CS 441/541 AI Group Project)

## Getting Started

Source `activate.sh` to activate the Python virtual environment.
If no environment is found at `./.ai_tetris_venv`, it will create one.

``` bash
cd /path/to/repo
source activate.sh
```

Be sure to *source* `activate.sh`, don't just run it.

## Adding a new dependency

If an external Python library is needed, follow these steps to install it:

1. Ensure `activate.sh` or `.ai_tetris_venv/bin/activate` has been sourced and
   the virtual environment is active.

2. Run `pip install <library>`  to install the library.

3. Run `pip freeze > requirements.txt` to update the requirements file. This
   ensures the new package will be installed for everyone the next time they
   source `activate.sh` or run `pip install -r requirements.txt`.

## Running Tests

To run a test suite:

``` bash
python -m unittest tests/<test_file>.py
```

## Contributors

* Kenzie Gage
* Daniel Hafner
* Joshua Lund
* Matt O'Tousa
* Camille Range
