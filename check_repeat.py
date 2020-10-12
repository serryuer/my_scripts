import os, sys, json, re

japanese = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u3100-\u312F\u3400-\u4DBF\u4e00-\u9fbf]')
english = re.compile(r'[a-zA-Z]')
digit = re.compile(r'[0-9]')

with open(sys.argv[1], mode='r') as f:
    for line in f:
        flag = False
        data = json.loads(line)
        text = data[sys.argv[2]]
        last = None
        count = 0
        for ch in text:
            if ch == last:
                count += 1
            else:
                last = ch
                count = 0
            if count == 3:
                flag = True
                if int(sys.argv[3]) == 1:
                    print(line.strip())
                break
        if not flag and int(sys.argv[3]) == 0:
            print(line.strip())

