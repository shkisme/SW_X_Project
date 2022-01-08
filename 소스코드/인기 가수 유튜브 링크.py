// 영어 번역을 위한 설치!
sudo apt install tesseract-ocr
!pip install pytesseract
!sudo apt install tesseract-ocr-kor
!pip install googletrans==4.0.0-rc1

// 유튜브 링크 제공
import pytesseract
import cv2
from google.colab.patches import cv2_imshow
import googletrans
from googletrans import Translator

translator = Translator()

for i in max_singer_list:
  print("%s 가수의 유튜브 영상 링크 : " % i , end = '')
  trans = translator.translate(i,src='ko',dest='en')
  url = 'https://www.youtube.com/results?search_query=' + trans.text.replace(' ','')
  print(url)
  print("\n")
