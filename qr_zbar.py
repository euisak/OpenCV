#pip install zbar-py
# 라이브러리
import zbar
import cv2
 
# 파일 경로 설정
file_path = "/Users/gim-uiyun/OpenCV/QR1.jpg"
 
# Zbar 라이브러리로 QR코드를 인식하기위해서 opcnCV로 이미지를 그레이 스케일로 읽음
# QR 코드 인식에 색상 정보가 필요 없어 이미지 데이터를 간단하게 만들어 인식 속도와 정확성을 높이기 위함
im = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
 
# QR 코드 데이터를 저장할 변수 초기화
qrcode_data = ""
 
# QR 코드와 바코드를 인식할 수 있는 객체 생성
scanner = zbar.Scanner()
# 이미지를 스캔하여 QR 코드를 찾고, 그 안의 데이터를 추출
results = scanner.scan(im)
# 한 사진에 여러 개의 QR 코드가 있을 수 있으므로 결과에서 각각의 QR 코드 데이터 추출
for result in results:
    qrcode_data = result.data.decode("utf-8")  # 바이트 문자열을 UTF-8로 디코딩
 

# QR 코드가 인식되지 않았을 경우 
if qrcode_data == "null":
    print("QR Code not detected")
else:
    # QR 코드가 인식되었을 경우, 인식된 QR 코드의 데이터를 출력
    print("Decoded Data : {}".format(qrcode_data))

