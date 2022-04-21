#maybe an encryption service?
import re

text = input("please input a word in lowercase characters to encrypt: ", )

a = re.sub("a", "b", text)
b = re.sub("b", "c", text)
c = re.sub("c", "d", text)
d = re.sub("d", "e", text)
e = re.sub("e", "f", text)
f = re.sub("f", "g", text)
g = re.sub("g", "h", text)
h = re.sub("h", "i", text)
i = re.sub("i", "j", text)
j = re.sub("j", "k", text)
k = re.sub("k", "l", text)
l = re.sub("l", "m", text)
m = re.sub("m", "n", text)
n = re.sub("n", "o", text)
o = re.sub("o", "p", text)
p = re.sub("p", "q", text)
q = re.sub("q", "r", text)
r = re.sub("r", "s", text)
s = re.sub("s", "t", text)
t = re.sub("t", "u", text)
u = re.sub("u", "v", text)
v = re.sub("v", "w", text)
w = re.sub("w", "x", text)
x = re.sub("x", "y", text)
y = re.sub("y", "z", text)
z = re.sub("z", "a", text)
print(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z)



letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
