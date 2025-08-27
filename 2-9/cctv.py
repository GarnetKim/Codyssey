import zipfile
import os
import glob
import cv2
import pygame
import numpy as np


# 📁 현재 스크립트 경로 기준
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

# 🖼️ 이미지 파일 불러오기 (대소문자 구분 없이 다양한 확장자 허용)
image_files = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
    image_files.extend(glob.glob(os.path.join(extract_path, ext)))
image_files = sorted(image_files)

# 🔍 이미지 유무 확인
if not image_files:
    print("❌ 이미지가 없습니다.")
    exit()
else:
    print(f"✅ {len(image_files)}장의 이미지가 있습니다.")

# 3. pygame 초기화
pygame.init()
pygame.display.set_caption("📷 CCTV Viewer")
screen = pygame.display.set_mode((800, 600))  # 임시 사이즈 (첫 이미지에 맞춰 다시 조정 가능)
idx = 0
running = True

def show_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print(f"⚠️ 이미지 불러오기 실패: {img_path}")
        return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (800, 600))  # 고정 크기
    surface = pygame.surfarray.make_surface(np.rot90(img))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

# 4. 이벤트 루프
show_image(image_files[idx])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RIGHT:
                idx = (idx + 1) % len(image_files)
                show_image(image_files[idx])
            elif event.key == pygame.K_LEFT:
                idx = (idx - 1) % len(image_files)
                show_image(image_files[idx])

pygame.quit()