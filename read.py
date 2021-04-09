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
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d) #good.append(d) 原封不動d裝含good字串裡面 ,如果是good.append(1) 遇到good都會改裝 1
# print('一共有', len(good) ,'筆留言提到good')

# 快寫法
# 第一個d = append的d
#			運算			  變數		清單				篩選條件
# out = [(number-1) for number in reference if number %2 == 0]
good = [d for d in data if 'good' in d]
# print(good)

# bad in d True or false
bad = ['bad' in d for d in data]
print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)
# count_1 = 0