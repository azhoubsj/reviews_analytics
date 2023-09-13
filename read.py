data = []
count = 0
length = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		length += len(data[count]) #用 length += len(line) 也可以
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