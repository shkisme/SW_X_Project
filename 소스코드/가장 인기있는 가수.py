// 차트에 있는 가수 세기
singer_list = []
singer_num = []

len = 0

for i in range(100):
  if ',' in singer[i]:
    tmp = singer[i].split(', ')
    for j in tmp:
      singer_list.append(j)
      len += 1
  else:
    singer_list.append(singer[i])
    len += 1

n_singer_list = []

for i in range(len):
  cnt = 1
  for j in range(i+1,len):
    if (singer_list[i] == singer_list[j]) & (singer_list[i] != 0) :
      cnt += 1
      singer_list[j] = 0
  if singer_list[i] != 0:
    singer_num.append(cnt)
    n_singer_list.append(singer_list[i])
    
// 폰트 설치
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

// 데이터를 시각화하여 그래프로 나타내기

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.font_manager as fm
 

plt.rc('font', family='NanumBarunGothic') 

len2 = 0

for i in n_singer_list:
  len2 += 1

x = np.arange(len2)
plt.bar(x,singer_num)
plt.xticks(x,n_singer_list)
plt.xticks(rotation = - 45 )
plt.show()

max = 0
index = 0
max_singer_list = []

for i in range(len2):
  if singer_num[i] >= max:
    max = singer_num[i]
    index = i

if singer_num.count(max)>1:
  j=0
  for i in range(len2):
    if singer_num[i] == max:
      max_singer_list.append(n_singer_list[i])
else :
  max_singer_list.append(n_singer_list[index])

print("현재 멜론 차트 TOP 100 에 가장 많은 비중을 차지하고 있는 가수는 %s 입니다." % max_singer_list)
