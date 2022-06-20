import argparse
import glob
import itertools
import os
import string
import sys

def alphabetical_order_naming_according_to_stat(path, stat_lambda):
	abs_path = os.path.abspath(path)

	if not os.path.isdir(abs_path):
		sys.exit(abs_path + " is not a directory!")

	files = glob.glob(abs_path + "/*")

	# Get desired sorted
	sorted_files = sorted(files, key=stat_lambda)

	if sorted_files == sorted(files):
		sys.exit("Folder '" + abs_path + "' is already alphabetically ordered")

	# Add an alphabetic ordering in beginning
	print 'Ordering folder: ' + abs_path

	alphabet = endless_alphabet()
	for file in sorted_files:
		directory = os.path.dirname(file)
		original_file_name = os.path.basename(file)
		original_file = os.path.join(directory, original_file_name)
		new_file = os.path.join(directory, alphabet.next() + "-" + original_file_name)
		os.rename(original_file, new_file)

	print 'Folder successfully ordered!'


def endless_alphabet():
    for i in itertools.count(start = 0, step = 1):
    	yield iterative_alphabet(i)


def iterative_alphabet(index_number):
	alphabet_length = len(string.ascii_uppercase)
	rolling_letter = string.ascii_uppercase[min(index_number, alphabet_length - 1)]

	if index_number < alphabet_length:
		return rolling_letter
	else:
		return rolling_letter + iterative_alphabet(index_number - alphabet_length)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("path", help="The folder whose files you want to have renamed")
	args = parser.parse_args()
	# Sort by modification time (mtime) ascending
	alphabetical_order_naming_according_to_stat(args.path, lambda t: os.stat(t).st_mtime)
