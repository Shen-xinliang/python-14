#��������һ���б�����ҳ�xԪ���Ƿ����б����棬������ڷ���1�������ڷ���0


def searchx(lis, x):
    for i in lis:
        if i == x:
            return 1
            break
    else:
        return 0

list = input ("list : ")
x = input ("x : ")
y = searchx(list, x)
print(y)

