# GDG on Campus 2024 AI/ML 개인 프로젝트

## 👕 옷을 구별해주는 AI 서비스
![Image](https://github.com/user-attachments/assets/bb0c31db-b5f2-4405-965f-7be7beda45de)

https://clothes-dectention-29f6gnp4nanr7vymeaqwxw.streamlit.app/

## Introduction
이 프로젝트는 YOLOv8과 Streamlit을 활용하여 실시간으로 의류 종류(Tshirt, jacketlong-dress, long-skirt, midi-dress, midi-skirt, pants, shirt, short, short-dress, short-skirt, skirt, sweater 등)를 분류하는 서비스입니다. 
웹캠을 통해 입력된 영상을 기반으로 모델이 의류를 감지하고 분류하며, 실시간 카메라를 이용해 인식이 가능합니다.

## Goal
고객이 입고 있는 옷을 실시간 카메라로 빠르게 감지하여 비슷한 제품을 자동 추천해줄 수 있다. 

## Technology Stack
- YOLOv8 – 실시간 객체 탐지 및 분류
- Streamlit – 간단한 웹 인터페이스 제공
- OpenCV – 영상 처리 및 웹캠 데이터 활용
- PyTorch – YOLO 모델 실행 및 추론
- streamlit-webrtc – 웹캠 스트리밍 처리
- FastAPI

  ## 공부한 것들
  FastAPI를 이용하여 서버를 배포하는 방법을 중점으로 공부할 수 있었다. 
