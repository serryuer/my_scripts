import os, sys, json, re

"""
param1: file
param2: key
param3: flag
"""

japanese = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u3100-\u312F\u3400-\u4DBF\u4e00-\u9fbf]')
english = re.compile(r'[a-zA-Z]')
digit = re.compile(r'[0-9]')

f = open('/data02/yujunshuai/mybin/emoji.dict')
emoji_file = f.read()
emoji_dict = eval(emoji_file)
f.close()

json_ = sys.argv[1].endswith('json')
query_index = sys.argv[2] if json_ else int(sys.argv[2])

with open(sys.argv[1], mode='r') as f:
    for line in f:
        if json_:
            data = json.loads(line)
        else:
            data = line.split('\t')
        text = data[query_index]
        flag = False
        for ch in text:
            if ch in emoji_dict:
                flag = True
                if int(sys.argv[3]) == 1:
                    print(line.strip())
                break
        if not flag and int(sys.argv[3]) == 0:
            print(line.strip())
