#��ӡ��100���ڵ�쳲���������

L = [1,1]
for x in range(2, 100):
    y = L[x-1] + L[x-2]
    if y >= 100:
        break
    x = x + 1
    L.append(y)
print(L)
