BIN_ACTIVATE="./.ai_tetris_venv/bin/activate"

if [ -f $BIN_ACTIVATE ]; then
	echo "found existing virtual environment"
else
	echo "no virtual environment found"
	echo "creating virtual environment..."
	python3 -m venv ./.ai_tetris_venv || exit 1;
	python3 -m pip install --upgrade pip || exit 1;
	echo "done!"
fi

echo "sourcing virtual environment..."
source "$BIN_ACTIVATE";
echo "activating virtual environment \"$(basename $VIRTUAL_ENV)\"..."
echo "attempting to update packages..."
pip install -r requirements.txt;
echo "done!"

