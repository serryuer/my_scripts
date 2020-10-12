import os, sys, json, re

japanese = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u3100-\u312F\u3400-\u4DBF\u4e00-\u9fbf]')
english = re.compile(r'[a-zA-Z]')
digit = re.compile(r'[0-9]')
json_ = sys.argv[1].endswith('json')
query_index = sys.argv[2] if json_ else int(sys.argv[2])
def symbol(c):
    if re.match(japanese, c) or re.match(english, c) or c.isdigit() or c == ' ' or c == '\u3000' or c == '+':
        return False
    return True
with open(sys.argv[1], mode='r') as f:
    for line in f:
        flag = False
        if json_:
            data = json.loads(line)
        else:
            data = line.strip().split('\t')
        text = data[query_index]
        for ch in text:
            if symbol(ch):
                flag = True
                if int(sys.argv[3]) == 1:
                    print(line.strip())
                break
        if not flag and int(sys.argv[3]) == 0:
            print(line.strip())

