import os, sys, json

json_ = sys.argv[1].endswith('json')
query_index = sys.argv[2] if json_ else int(sys.argv[2])

with open(sys.argv[1], mode='r')  as f:
    for line in f:
        if json_:
            data = json.loads(line)
        else:
            data = line.strip().split()
        text = data[query_index]
        if text.find('@') != -1 or text.find('#') != -1:
            if int(sys.argv[3]) == 1:
                print(line)
            continue
        if int(sys.argv[3]) == 0:
            print(line.strip())
