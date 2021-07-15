good = []
for d in data:
  if 'good' in d:
    good.append(d)
print('一共有', len(good),'筆留言提到good')
print(good[0])
