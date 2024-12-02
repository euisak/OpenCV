# 라이브러리
import cv2
import numpy as np

# 이미지를 읽어 NumPy 배열 형식으로 반환
inputImage = cv2.imread("QR1.jpg")
# 이미지가 너무 크거나 처리 속도가 느려지는 문제 해결 위해 이미지의 크기를 20%로 축소
inputImage = cv2.resize(inputImage, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
 
# OpenCV에서 QR 코드를 검출하고 해석하는 기능은 QRCodeDetector 클래스에 구현되어 있음
# QR코드를 검출하거나 해석위해 QRCodeDetector 객체를 생성
qrDecoder = cv2.QRCodeDetector()
 
# QR코드를 찾고 디코딩
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)

# QR 코드가 인식된 경우 
if len(data)>0:
    print("Decoded Data : {}".format(data))

# QR 코드가 인식되지 않았을 경우 
else:
    print("QR Code not detected")

