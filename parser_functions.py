def filter_lines(args, lines):															#Filtering file lines if it needs
	if args.where:
		if args.where.count('>') == 1:
			parameter = args.where.split('>')[0]
			value = float( args.where.split('>')[-1] )
			filter_function = lambda element: float( element[parameter] ) > value
		elif args.where.count('=') == 1:
			parameter = args.where.split('=')[0]
			value = args.where.split('=')[-1]
			filter_function = lambda element: element[parameter] == value
		elif  args.where.count('<') == 1:
			parameter = args.where.split('<')[0]
			value = float( args.where.split('<')[-1] )
			filter_function = lambda element: float( element[parameter] ) < value
		else:
			filter_function = lambda element: True
			raise Exception('Wrong where separator')
		if parameter in lines[0].keys():
			lines = list(filter( filter_function, lines ))
		else:
			raise Exception('Wrong where parameter')
	return lines


def aggregate_lines(args, lines):														#Aggregating file lines if it needs
	if args.aggregate:
		if "=" in args.aggregate:
			parameter = args.aggregate.split('=')[0]
		else:
			raise Exception("Wrong aggregate parameter, there is no '=' separator")
		if parameter not in lines[0].keys():
			raise Exception("Wrong aggregate parameter, it's not in csv keys")
		mi = float(lines[0][parameter])
		ma = mi
		su = 0
		for line in lines:
			mi = min( float(line[parameter]), mi )
			ma = max( float(line[parameter]), ma )
			su += float(line[parameter])
		if args.aggregate[-3:] == "min":
			lines = [ { parameter : mi } ]
		elif args.aggregate[-3:] == "max":
			lines = [ { parameter : ma } ]
		elif args.aggregate[-3:] == "avg":
			lines = [ { parameter : su / float(len(lines)) } ]
		else:
			raise Exception('Wrong aggregate')
	return lines


def sort_lines(args, lines):														#Aggregating file lines if it needs
	if args.order_by:
		if "=" in args.order_by:
			parameter = args.order_by.split('=')[0]
			method = args.order_by.split('=')[1]
		else:
			raise Exception("Wrong order_by parameter, there is no '=' separator")
		if parameter not in lines[0].keys():
			raise Exception("Wrong order_by parameter, it's not in csv keys")
		if method == "desc":
			try:
				lines.sort( key = lambda element: float( element[parameter] ), reverse=True )
			except:
				raise Exception("Can't sort this type")
		elif method == "asc":
			try:
				lines.sort( key = lambda element: float( element[parameter] ) )
			except:
				raise Exception("Can't sort this type")
		else:
			raise Exception('Wrong sort method')
	return lines