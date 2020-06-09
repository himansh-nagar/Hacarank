##########     kangaroo


def kangaroo(x1, v1, x2, v2):
    while True:
        if v1<v2 and x1<x2:
            return "NO"
        k1,k2=x1+v1,x2+v2
        if k1==k2:
            return "YES"
        x1+=v1
        x2+=v2
print(kangaroo(0 ,2 ,5 ,3))