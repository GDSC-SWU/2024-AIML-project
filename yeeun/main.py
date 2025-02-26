from fastapi import FastAPI, File, UploadFile
import torch
from PIL import Image
import io
import uvicorn
from ultralytics import YOLO

# FastAPI 앱 생성
app = FastAPI()

# YOLOv8 모델 로드
model_path = "best.pt"
model = YOLO(model_path)  # YOLOv8 모델 로드

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    # 이미지 로드
    image = Image.open(io.BytesIO(await file.read()))

    # 모델 예측 수행
    results = model(image)

    detections = []
    for r in results:
        for box in r.boxes.data:
            x1, y1, x2, y2, conf, cls = box.tolist()
            detections.append({
                "bbox": [round(x1, 2), round(y1, 2), round(x2, 2), round(y2, 2)],  # 바운딩 박스 좌표
                "confidence": round(conf, 2),  # 신뢰도
                "class": int(cls)  # 클래스 ID
            })

    return {"detections": detections}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
