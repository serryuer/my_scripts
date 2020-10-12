import os, sys, json
print_fields = []
if len(sys.argv) != 2:
    print_fields = sys.argv[2:]
with open(sys.argv[1], mode='r') as f:
    for line in f:
        data = json.loads(line)
        if print_fields:
            print('\t'.join([str(data[field]) for field in print_fields]))
        else:
            print('\t'.join([str(data[key]) for key in data]))

