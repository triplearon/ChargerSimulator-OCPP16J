import getopt
import sys

import PyQt5.uic as uic

if __name__ == '__main__':
    input_dir = ""
    output_dir = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("ui2py.py -i <input_dir> -o <output_dir>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("ui2py.py -i <input_dir> -o <output_dir>")
            sys.exit(2)
        elif opt in ("-i", "--input"):
            input_dir = arg
        elif opt in ("-o", "--output"):
            output_dir = arg

    if input_dir == "" or output_dir == "":
        print("ui2py.py -i <input_dir> -o <output_dir>")
        sys.exit(2)

    uic.compileUiDir(input_dir, map=lambda x, y: (output_dir, y))
