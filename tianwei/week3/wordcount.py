#��һ��Ӣ�ĵĴ��ı��ļ���ͳ�����еĵ��ʳ��ֵĸ���


with open(r'E:\GitHub\python-14\tianwei\week3\python.txt', ) as file:
    str = file.read()

words = str.split()
word = set(words)

#print(word)

number=[]

for i in word:
    number.append(words.count(i))

wordcont = zip(word, number)

print(wordcont)





