import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver

# 이미지를 저장할 폴더를 설정합니다.
download_folder = "./downloaded_images"
os.makedirs(download_folder, exist_ok=True)

# 크롬 드라이버 설정
driver = webdriver.Chrome()  # 크롬 드라이버 경로 설정

for page_num in range(1, 10):
    driver.get(f"https://te-ket.com/product/list.html?cate_no=46&page={page_num}")

    # 페이지 소스 가져오기
    html = driver.page_source

    # BeautifulSoup으로 HTML 분석
    soup = BeautifulSoup(html, "html.parser")

    # 모든 이미지 태그 선택
    img_tags = soup.find_all("img")

    # 모든 이미지 저장
    for idx, img_tag in enumerate(img_tags):
        img_url = img_tag.get("src")

        if not img_url.startswith("http"):  # 상대 경로일 경우 https 추가
            img_url = "https:" + img_url

        # 이미지 다운로드 경로 설정
        img_path = os.path.join(download_folder, f'image_{page_num}_{idx+1}.jpg')
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(img_path, "wb") as f:
                f.write(response.content)
            print(f"이미지 저장 완료: {img_path}")
        else:
            print(f"이미지 저장 실패: {img_url}")

# 브라우저 종료
driver.quit()
