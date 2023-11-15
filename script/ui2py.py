import getopt
import sys
import os

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

    for files in os.listdir(ui_dir):
        if files.endswith(".ui"):
            ui_file = os.path.join(ui_dir, files)
            py_file = os.path.join(ui_dir, "ui_" + files.replace(".ui", ".py"))
            print(f"UIC: {ui_file}, {py_file}")
            os.system(f"pyside6-uic {ui_file} -o {py_file}")
