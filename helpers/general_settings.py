import os

_CURRENT_DIRECTORY = os.path.abspath(os.getcwd())

# Path to log
PATH_TO_LOGS = _CURRENT_DIRECTORY + os.sep + ".." + os.sep + "Logs" + os.sep
if not os.path.exists(PATH_TO_LOGS):
    os.makedirs(PATH_TO_LOGS)

# Path to screenshots of a browser
PATH_TO_SCREENSHOTS = _CURRENT_DIRECTORY + os.sep + ".." + os.sep + "Logs" + os.sep + "screenshots" + os.sep
if not os.path.exists(PATH_TO_SCREENSHOTS):
    os.makedirs(PATH_TO_SCREENSHOTS)
