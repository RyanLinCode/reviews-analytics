data = []
count = 0 ;
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')



sum_len = 0
for d in data:
	#d 一個單獨留言 字串 data是清單
	sum_len += len(d)

print('留言的平均長度為：', sum_len/len(data))

# 篩選 長度低於100
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new) ,'筆留言長度小於100')
print(new[0])
print(new[1])


# 篩選 good字串
good = []
for d in data:
	if 'good' in d:
		good.append(d) #good.append(d) 原封不動d裝含good字串裡面 ,如果是good.append(1) 遇到good都會改裝 1
print('一共有', len(good) ,'筆留言提到good')

# 快寫法 list comprehension
# 第一個d = append的d
# 			運算			  變數		清單				篩選條件
# out = [(number-1) for number in reference if number %2 == 0]
# good = [d for d in data if 'good' in d]

# # bad in d True or false
# bad = ['bad' in d for d in data]
# print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)
# count_1 = 0


# 文字計數
words_count = {}

for d in data:
	words = d.split() #預設 split遇到空白鍵會自動忽略 若不使用預設空白鍵則會跳一格空白鍵
	# print(words)
	for word in words:
		if word in words_count: #若字有出現在words_count裡面
			words_count[word] +=1
		else:
			words_count[word] = 1 # 新增KEY在words_count字典裡面
	

for word in words_count:
	if words_count[word] >1000000: 
			print(word,words_count[word])

print(len(words_count)) #k字典的長度 總共有幾個key
print(words_count['Allen'])

while True:
	word = input('請問你要查什麼字：')
	if word == 'q':
		break
	if word in words_count:
			print(word, '出現過的次數為：', words_count[word])
	else:
		print('這個字沒有出現過')

print('感謝使用本查詢功能')


