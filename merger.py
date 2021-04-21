import os
import argparse
import shutil
import glob

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="Input directory")
args = parser.parse_args()

if not os.path.isdir(args.input_dir):
    print("%s is not a directory or doesn't exist" % args.input_dir)
    exit()

for path in os.listdir(args.input_dir):
    if path.startswith(".") or os.path.isfile(args.input_dir + "/" + path):
        continue

    for deffile in glob.glob("*.def"):
        cfg_file = args.input_dir + "/" + path + "/" + deffile
        if not os.path.isfile(cfg_file):
            print("%s does not exist. Skipping..." % cfg_file)
            continue

        path_file_path = args.input_dir + "/" + path + "/path.txt"
        with open(path_file_path, "r") as path_file:
            pathtxt = path_file.read()
            pathtxt = pathtxt.replace(".", "")
            destination = os.getcwd() + "/" + pathtxt
            shutil.copy(cfg_file, destination)
