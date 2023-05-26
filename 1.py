s = input()
s=s.split()
a = 'уеыаоэяию'
h=[0]*len(s)
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] in a:
            h[i]+=1
f=True
for i in range(len(h)-1):
    if h[i]!=h[i+1]:
        f=False
        break
if f:
    print('Парам пам-пам')
else:
    print('Пам парам')