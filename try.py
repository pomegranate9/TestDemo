import torch
x, y = [], []
with open(r"data_old/try", "r", encoding="utf-8") as f:
    for line in f:
        # 按行读取，如果最后一个字符是换行，那就从头读到尾
        if line[-1] == "\n":
            line = line[:-1]
        # 将读到的句子分词，存到列表x里
        # split函数：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表
        # 所以 x 里存的是字符串列表？
        x.append(line.split()[0].split(":")[0])
        y.append(line.split()[1:])

print(x)
print(y)

