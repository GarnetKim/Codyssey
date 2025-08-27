import os
import zipfile
import glob
import pygame
import cv2
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

# 🖼️ 이미지 파일 목록
image_files = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
    image_files.extend(glob.glob(os.path.join(extract_path, ext)))
image_files = sorted(image_files)

if not image_files:
    print("❌ 이미지가 없습니다.")
    exit()
else:
    print(f"✅ {len(image_files)}장의 이미지가 있습니다.")

# 🔍 사람 탐지기 (얼굴, 전신, 상반신)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')  # 전신
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')  # 상반신

# 🎮 pygame 초기화
pygame.init()
pygame.display.set_caption("📷 CCTV Viewer")
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 36)
idx = 0
running = True
search_mode = False

# 📸 이미지 표시 및 상반신 감지 함수
def detect_and_display(img_path, detect=False):
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ 이미지 불러오기 실패: {img_path}")
        return 0, None

    count = 0
    if detect:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(gray, 1.1, 3)
        count = len(bodies)
        if count > 0:
            print(f"🧍 사람 감지됨: {os.path.basename(img_path)}")
        for (x, y, w, h) in bodies:
            # 🔴 빨간 사각형
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return count, img

# 🎮 pygame 화면에 이미지 출력
def display(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (800, 600))
    surface = pygame.surfarray.make_surface(np.rot90(img))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

# 🔁 메인 루프
while running:
    # ✅ 이미지 인덱스 초과 방지
    if idx >= len(image_files):
        print("✅ 모든 이미지 탐색 완료")
        running = False
        break

    if not search_mode:
        _, current_img = detect_and_display(image_files[idx])
        display(current_img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_RIGHT:
                idx = (idx + 1) % len(image_files)

            elif event.key == pygame.K_LEFT:
                idx = (idx - 1) % len(image_files)

            elif event.key == pygame.K_RETURN:
                search_mode = True
                found = False
                print("🔎 사람 탐색 시작...")

                for i in range(idx, len(image_files)):
                    count, detected_img = detect_and_display(image_files[i], detect=True)
                    if count > 0:
                        idx = i + 1
                        display(detected_img)
                        found = True
                        break

                if not found:
                    screen.fill((0, 0, 0))
                    msg = font.render("🔚 사람을 찾지 못했습니다. (검색 종료)", True, (255, 255, 255))
                    screen.blit(msg, (100, 250))
                    pygame.display.flip()
                    idx = len(image_files)  # 👉 강제 종료

                search_mode = False

print("✅ 모든 이미지 탐색 완료")
pygame.quit()