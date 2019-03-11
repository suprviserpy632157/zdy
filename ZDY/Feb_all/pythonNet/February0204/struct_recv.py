# struct_recv.py
from socket import *
import struct

s = socket(AF_INET,SOCK_DGRAM)
s.bind(("0.0.0.0",8895))

# 确定数据结构
st = struct.Struct("i16sf")
# 接收数据
while 1:
    data,addr = s.recvfrom(1024)
    # 数据解析
    data = st.unpack(data)
    print(data)
s.close()