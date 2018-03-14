# This will batch rename a group of files in a given directory to the name you want to rename it to (numbers will be added)

import os
import argparse

def rename(work_dir, name):
	os.chdir(work_dir)
	num = 1

	for file_name in os.listdir(work_dir):
	    file_parts = (os.path.splitext(file_name))
	    os.rename(file_name, name + str(num) + file_parts[1])
	    num += 1

def get_parser():
	parser = argparse.ArgumentParser(description="Batch renaming of files in a folder")
	parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where you wish to rename the files')
	parser.add_argument('name', metavar='NAME', type=str, nargs=1, help='the new name of the files')
	return parser

def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	work_dir = args['work_dir'][0]
	name = args['name'][0]
	rename(work_dir, name)


if __name__ == "__main__":
	main()
