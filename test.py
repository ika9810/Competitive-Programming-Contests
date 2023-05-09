import gdown
import os

# 다운로드 받을 Google Drive 파일의 ID를 입력합니다.
file_id = "1oz6a35gWzV4DC2AvX0ishtwbfea1NHRD"

# Google Drive 파일의 ID를 기반으로 파일을 다운로드합니다.
url = f"https://drive.google.com/uc?id={file_id}"
output = "output_video.mp4"
try:
  gdown.download(url, output, quiet=False)
except:
  print("test.py 실행 실패!") 
os.remove('./output_video.mp4')
print("test.py 실행 완료!")
