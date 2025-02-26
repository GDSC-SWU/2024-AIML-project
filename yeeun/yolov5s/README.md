
## 👕 옷을 구별해주는 AI 서비스 
![스트림릿 실행](https://github.com/user-attachments/assets/9c560a4b-2c99-4456-a0c5-e0d08d22ee7b)

## Introduction
- 다양한 옷 이미지를 업로드하면 Outerwear(겉옷), knitwear(니트 재질), Sweatshirts(맨투맨, 후드티, 후드집업), Tees(티셔츠), Pants(하의), Headwear(모자), accessories(액세서리) 중 하나로 선택되어 옷을 구별해줍니다.


## Goal
- 이미지를 촬영하면 이 옷의 브랜드가 무엇인지 인식해주는 프로그램으로 발전시키고 싶다.
- 옷의 재질이 무엇인지 구별해주는 서비스를 만들어보면 어떨까?

## Technology Stack 
- Yolov5s
- Python
- PyTorch
- Streamlit
  
1. 이미지 크롤링
   (teket 의류 브랜드의 이미지를 이용했다.)
2. 이미지 라벨링
    [Outerwear, knitwear, Sweatshirts, Tees, Pants, Headwear, accessories] 7개 클래스로 라벨링

    ***reference (https://github.com/HumanSignal/labelImg)***

4. train데이터와 val 데이터로 나눠서 훈련시키기
5. streamlit을 통해 데모 애플리케이션 만들기
   
## 📹 Demo video
![clothes_yolov5s_demo video](https://github.com/user-attachments/assets/dfb8f9e8-31d1-4b9f-8df3-ff5b844c6121)

