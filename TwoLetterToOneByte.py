def mapp(i):
    if i<=57 and i>=48:
        return i-48
    else:
        return i-55

def to(b0,b1):
    return mapp(b1)+(mapp(b0)<<4)

for i in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']:
    for j in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']:
        print to(ord(i),ord(j)),"=",int("0x"+i+j,16),'\n'
