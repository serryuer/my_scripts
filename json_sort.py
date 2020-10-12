import os, sys, json

json_ = sys.argv[1].endswith('json')
sorted_index = sys.argv[2] if json_ else int(sys.argv[2])

with open(sys.argv[1], mode='r') as f:
    indexes = []
    all_data = []
    count = 0
    for line in f:
        if json_:
            data = json.loads(line)
        else:
            data = line.strip().split('\t')
        indexes.append([float(data[sorted_index]), count])
        #count += 1
        all_data.append(line.strip())
        count += 1
    indexes = sorted(indexes)
    for item in indexes:
        print(all_data[item[1]])


