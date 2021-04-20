import configparser
import argparse

parser = argparse.ArgumentParser(description='Helper utility to setup variables')
parser.add_argument('input_file', help='Input file with all of the variables defined')
args = parser.parse_args()


config = configparser.ConfigParser()
config.read(args.input_file)

if len(config) <= 1:
    print("%s is not a valid file" % args.input_file)
    exit()

if not "files" in config.sections():
    print("No [files] section found. Nothing to do")

if not "variables" in config.sections():
    print("No [variables] section found. Nothing to do")

write_count = 0
# Loop for every filepath
for filepath in config["files"]["files"].split('\n'):
    try:
        f = open(filepath, "r")
        file_contents = f.read()
        for variable in config["variables"]:
            file_contents = file_contents.replace(r"{{%s}}" % variable, config["variables"][variable])
        
        new_filepath = filepath.replace(".def", "")
        with open(new_filepath, "w") as new_file:
            new_file.write(file_contents)
            write_count += 1
    except Exception:
        print("Failed to open '%s'" % filepath)

print("Successfuly wrote %d files" % write_count)