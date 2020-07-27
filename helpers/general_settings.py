import os
import pathlib

# _CURRENT_DIRECTORY = os.path.abspath(os.getcwd())
_CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()

# Path to log
PATH_TO_LOGS = str(_CURRENT_DIRECTORY) + os.sep + ".." + os.sep + "Logs" + os.sep
if not os.path.exists(PATH_TO_LOGS):
    os.makedirs(PATH_TO_LOGS)

# Path to screenshots of a browser
PATH_TO_SCREENSHOTS = str(_CURRENT_DIRECTORY) + os.sep + ".." + os.sep + "Logs" + os.sep + "screenshots" + os.sep
if not os.path.exists(PATH_TO_SCREENSHOTS):
    os.makedirs(PATH_TO_SCREENSHOTS)
