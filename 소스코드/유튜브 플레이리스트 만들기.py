// 메모장에 내가 원하는 노래의 제목과, 유튜브 링크 입력하기
import datetime
main = """
  1. 플레이 리스트 리셋하여 새로 만들기
  2. 플레이 리스트에 노래 추가하기
  3. 저장하기 OR 그만두기
"""
print("-"*25 + "메뉴" + "-"*25)
print(main)
print("-"*54)

def create():
  memo = input("""
추가하고 싶은 노래의 제목과 유튜브 링크를 입력해주세요
' '(공백)으로 구분하여 입력해주세요! >> """)
  with open('playlist.txt','w') as f:
    f.write(f'{memo}\n')
def append():
  memo = input("""
추가하고 싶은 노래의 제목과 유튜브 링크를 입력해주세요
' '(공백)으로 구분하여 입력해주세요! >> """)
  with open('playlist.txt','a') as f:
    f.write(f'{memo}\n')

while True:
  menu = int(input("- 메뉴를 선택하세요 - "))
  if menu == 1:
    create()
  elif menu == 2:
    append()
  else:
    print("저장했습니다!")
    break
  print("\n<현재 나의 플레이 리스트>\n")
  with open('playlist.txt','r') as f:
    for line in f.readlines():
      print(line,end='') 
      print("\n")
      
 // 유튜브 영상 화면에 띄우기
from IPython.display import YouTubeVideo, display 

with open('playlist.txt','r') as f:
  for line in f.readlines():
    mysong = line.split(' ')[1]
    mysonglink = mysong.split('v=')[1]
    mysonglink2 = mysonglink.split('\n')[0]
    video = YouTubeVideo(mysonglink2, width=500) 
    display(video)
