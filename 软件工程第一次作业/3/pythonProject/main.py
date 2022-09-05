# 提取文档并处理噪音
def getText():
    txt = open("Hamlet.txt", 'r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, ' ')  # 将文本中的特殊字符替换为空格
    return txt

readtxt = getText()
words = readtxt.split()  # 获得分割完成的单词列表
counts = {}  # 创建空字典，存放词频统计信息
for word in words:
    if len(word) <= 3:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())  # 将无序的字典类型转换为有序的列表类型
items.sort(key=lambda x: x[1], reverse=True)  # 从高到低排序
for i in range(10):
    word, count = items[i]
    print("{0:<6}{1:>5}".format(word, count))   # 格式化输出结果

phrase = []
l = len(words)
p=0
q=1
counts2 = {}
for p in range(l-1):
    phrase.append(words[p] +' '+ words[q])
    q+=1
for word in phrase:
    counts2[word] = counts2.get(word, 0) + 1
items = list(counts2.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<20}{1:>5}".format(word, count))   