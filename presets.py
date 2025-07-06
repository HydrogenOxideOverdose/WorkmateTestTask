from parser_functions import *


class Preset:
	def __init__(self, command, input_type, help, function):
		self.parser_args = {
			'command': command,
			'type': input_type,
			'help': help
		}
		self.function = function


presets_config = [
	Preset( command='--where', input_type=str, help='Filter `column_name`<=>`column_value`', function=filter_lines ),
	Preset( command='--order-by', input_type=str, help='Sort `column_name`=`desc or asc`', function=sort_lines ),
	Preset( command='--aggregate', input_type=str, help='Aggregate `column_name`=`max,min or avg`', function=aggregate_lines )
]