# Creates a directory in working directory if not exists

import os
import sys

def main():
	work_dir = sys.argv[1]
	dir_name = sys.argv[2]
	os.chdir(work_dir)
	if not os.path.isdir(dir_name):
		os.mkdir(dir_name)
		print("Created directory {}".format(dir_name))
	else:
		print("The directory {} already exists".format(dir_name))

if __name__ == '__main__':
	main()