# Instruction Detection System (Yolo 알고리즘을 이용한 침입자 감지 시스템)

## 요약
Yolo 알고리즘을 이용하여 카메라에 확인된 침입자(객체)를 판단하고 이를 웹사이트로 전송하여 사용자가 확인 가능하게 한다.

## 설치 및 사용방법

### Yolo를 이용한 탐지기

1. 가상 환경 활성화
    ```bash
    venv\Scripts\activate
    ```

2. 필수 패키지 설치
    ```bash
    pip install -r requirements.txt
    ```

3. 웹캠으로 탐지 실행
    ```bash
    python detect.py --source 0
    ```

### 서버 설정

1. 가상 환경 활성화
    ```bash
    myvenv\Scripts\activate
    ```

2. 관리자 계정 생성
    ```bash
    python manage.py createsuperuser
    ```

3. 서버 실행
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    테스트는 가능하지만 실제 서비스에서는 리버스 프록시를 둘 것을 추천합니다.



## 데모이미지

- YOLO알고리즘을 이용하여 카메라에 객체가 인식됩니다. 객체의 종류와 예측 퍼센트까지 확인가능합니다.
    
![image](https://github.com/GoByeonghu/Intrusion-Detection-System/assets/92240138/aae1edee-a229-447e-8ae1-d7909887dbac)
  
![image](https://github.com/GoByeonghu/Intrusion-Detection-System/assets/92240138/a1311b99-3142-4531-85f5-27a257604f6d)

- 여러가지 객체도 동시에 판단 가능합니다.
  
![image](https://github.com/GoByeonghu/Intrusion-Detection-System/assets/92240138/14713758-c645-45be-b566-23484f3198bd)

- 이렇게 객체(침입자)가 탐지되면 사용자의 웹사이트에 전송되어 표기됩니다.
  
![image](https://github.com/GoByeonghu/Intrusion-Detection-System/assets/92240138/1d5900ca-5cda-45a9-9c7f-feb7b033e8fb)

## 데모영상
[데모영상 유튜브 링크](https://youtu.be/P-s2lrPAxfA)

![Instruction-detection-system-Demo-ezgif com-video-to-gif-converter](https://github.com/GoByeonghu/Intrusion-Detection-System/assets/92240138/9605cf2f-991a-497d-92c6-00de3834c6ec)

## Yolo 원본 리포지토리
[Yolov5 GitHub Repository](https://github.com/ultralytics/yolov5)