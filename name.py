#使用方法修改字符串的大小写
name = 'ada lovelace'
print(name.title()) #注意.title后需要加括号 将每个单词的首字母大写

print(name.lower()) #将所有字母都变成小写

print(name.upper()) #将所有字母都变成大写
xiaoming = '嗨'
names = f"{xiaoming} {name} xiao"
print(type(names))