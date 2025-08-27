import zipfile
import os
import glob
import cv2
import pygame
import numpy as np

# 📁 기본 경로 설정
base_dir = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(base_dir, "cctv.zip")
extract_path = os.path.join(base_dir, "cctv")

# 📦 압축 해제
if not os.path.exists(extract_path):
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"✅ 압축 해제 완료: {extract_path}")
    else:
        raise FileNotFoundError(f"❌ {zip_path} 파일이 존재하지 않습니다.")
else:
    print(f"📂 {extract_path} 폴더가 이미 존재합니다.")

# 🖼️ 이미지 파일 필터링
image_files = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
    image_files.extend(glob.glob(os.path.join(extract_path, ext)))
image_files = sorted(image_files)

if not image_files:
    print("❌ 이미지가 없습니다.")
    exit()
else:
    print(f"✅ {len(image_files)}장의 이미지가 있습니다.")

# 🧠 HOG 사람 탐지기 세팅
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 🎮 pygame 초기화
pygame.init()
pygame.display.set_caption("🔎 사람 탐지 CCTV")
screen = pygame.display.set_mode((800, 600))

# ▶️ 이미지 순차 탐색
for idx, img_path in enumerate(image_files):
    img = cv2.imread(img_path)
    if img is None:
        print(f"⚠️ 이미지 불러오기 실패: {img_path}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects, _ = hog.detectMultiScale(gray, winStride=(4, 4), padding=(8, 8), scale=1.05)

    if len(rects) > 0:
        print(f"🧍‍♀️ 사람 감지됨: {os.path.basename(img_path)}")

        # 🔺 사람 위치에 빨간 사각형 그리기
        for (x, y, w, h) in rects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Pygame 화면에 출력
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb = cv2.resize(img_rgb, (800, 600))
        surface = pygame.surfarray.make_surface(np.rot90(img_rgb))
        screen.blit(surface, (0, 0))
        pygame.display.flip()

        # ⏸️ 엔터 키 기다리기
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
    else:
        print(f"🚫 사람 없음: {os.path.basename(img_path)}")

print("🔍 모든 이미지 탐색 완료")
pygame.quit()