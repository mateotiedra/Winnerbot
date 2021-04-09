import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from winnerbot.userMenu.menu import Menu

originFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
absolutePathToDriver = "C:\\webdriver\\chromedriver.exe" #le chemin au chrome driver
relativePathToData = "dataFakeIDs.txt"

menu = Menu(originFilePath, absolutePathToDriver, relativePathToData)

menu.open()