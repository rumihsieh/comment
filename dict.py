data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有',len(data),'筆資料')

wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典
for word in wc:
	if wc[word] > 100000:
		print(word,wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字？')
	if word == 'q':
		break
	if word in wc:
	print(word,'出現的次數為：', wc[word])
else:
	print('這個字沒有出現過喔！')
print('感謝使用本查詢功能')