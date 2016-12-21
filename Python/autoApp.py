# -*- coding: utf-8 -*-

import subprocess
import sys

def main():
    searchApp("Safari.app")

def searchApp(appName):
    try:
        path = subprocess.check_output(["mdfind", appName])
        path = path.decode("utf-8").split("\n")[0]
        print(path)
        subprocess.check_output(["open", path])
    except:
        print("An Error Occured\n")
        sys.exit()

if __name__ == '__main__':
    main()
