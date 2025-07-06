from tabulate import tabulate
from presets import presets_config
import argparse
import csv




def main():
	parser = argparse.ArgumentParser(description='Testovoe zadanie')
	parser.add_argument('--file', type=str, help='Pass to cvs file')
	for preset in presets_config:										   #Loading all function from config and adding them's arguments
		parser.add_argument(
			preset.parser_args['command'],
			type=preset.parser_args['type'],
			help=preset.parser_args['help']
		)
	args = parser.parse_args()
	if args.file == None:												   #Checking cvs file and trying to open it
		raise Exception("There is no file given\nUse --file <file_name>.csv")
	if args.file.split(".")[-1][-3:] != "csv":
		raise Exception("It's not a csv file")
	try:
		csv_file = csv.DictReader( open( args.file ) )
		lines = list( csv_file )
	except Exception as e:
		raise Exception("Can't open file")
	for preset in presets_config:										  #Runing all function from config
		lines = preset.function(args, lines)
	print(tabulate(lines, tablefmt="grid", stralign='center', headers="keys"))



if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)