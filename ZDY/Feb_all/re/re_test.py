# re_test.py
import re
import sys
PORT = sys.argv[1]
f = open("1.txt")
# 找到端口所在的对应段落
while True:
    data = ''
    for line in f:
        if line != '\n':
            data += line
        else:
            break
    if not data:
        print("No port")
        break
    # 通过首单词比对是否为目标端
    try:
        port = re.match(r'\S+',data).group()
    except Exception:
        continue
    if PORT == port:
        # 匹配address is
        # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
        # 匹配Internet address is 增强一下排他性
        pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'
        address = re.search(pattern,data).group(1)
        print(address)
        break 
f.close()