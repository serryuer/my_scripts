import os, sys, json

with open(sys.argv[1], mode='r') as f:
	for line in f:
		data = json.loads(line)
		new_data = {}
		for key in sys.argv[2:]:
			new_data[key] = data[key]
		print(json.dumps(new_data, ensure_ascii=False))
		
