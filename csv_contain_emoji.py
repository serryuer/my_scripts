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

with open(sys.argv[1], mode='r') as f:
    for line in f:
        data = line.split('\t')
        text = data[sys.argv[2]]
        flag = False
        for ch in text:
            if ch in emoji_dict:
                flag = True
                if int(sys.argv[3]) == 1:
                    print(line.strip())
                break
        if not flag and int(sys.argv[3]) == 0:
            print(line.strip())
