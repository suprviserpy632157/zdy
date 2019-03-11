s="Welcome to 中国"
g=s.encode("gbk")
print(g)
b=b'Python\xe7\x89\x9bX'
s1=b.decode()
print(s1)

s2='HelloTarena'
f = open('tarena.txt','w+b')
f.write(s2.encode())
print(f.tell())
print(f.seek(0,0))
print(f.seek(5))
print(f.tell())
f.close()