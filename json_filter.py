import os, sys, json

with open(sys.argv[1], mode='r') as f:
    for line in f:
        data = json.loads(line)
        conditions = sys.argv[2:]
        conditions = [[conditions[i * 2], conditions[i * 2 + 1]] for i in range(int(len(conditions)/2))]
        if all([data[item[0]] == (item[1] if not item[1].isdigit() else int(item[1])) for item in conditions]):
            print(line.strip())

