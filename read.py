data = []
count = 0
length = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		# length += len(data[count]) #用 length += len(line) 也可以
		count += 1
		if count % 1000 == 0:
			print(len(data))


print('档案读取完了，总共有', len(data), '笔资料')


print('每笔资料平均长度为', length / count)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('长度小于100的资料总共有', len(new), '笔')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d) #这四行 等于 good = [d for d in data if 'good' in d]
print('含有good的资料总共有', len(good), '笔')


# 文字注解

wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key进wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('请问你想要查询什么字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出现过的次数为： ', wc[word])
	else:
		print('这个字没有出现过哦')

print('感谢使用本查询功能')

