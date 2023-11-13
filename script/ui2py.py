import getopt
import sys

import PyQt5.uic as uic

if __name__ == '__main__':
    ui_dir = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:", ["dir="])
    except getopt.GetoptError:
        print("ui2py.py -d <ui_dir>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("ui2py.py -d <ui_dir>")
            sys.exit(2)
        elif opt in ("-d", "--dir"):
            ui_dir = arg

    if ui_dir == "":
        print("ui2py.py -d <ui_dir>")
        sys.exit(2)

    uic.compileUiDir(ui_dir)
