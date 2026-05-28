import cv2
import os

# --- НАЛАШТУВАННЯ ---
#video_path = 'cars_video.webm'  # Назва завантаженого відео
#output_folder = 'frames_cars'   # Папка, куди полетять картинки
video_path = 'empty_video.webm'  # інше ім'я фонового відео
output_folder = 'frames_empty'   # Міняємо назву папки на 'empty'
frame_interval = 15             # Зберігаємо кожен 15-й кадр
max_frames = 400                # Кількість кадрів, які нам потрібні

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)
count = 0
saved_count = 0

print(f"Починаємо нарізку відео {video_path}...")

while cap.isOpened() and saved_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        break
        
    if count % frame_interval == 0:
        cv2.imwrite(os.path.join(output_folder, f"frame_{saved_count:04d}.jpg"), frame)
        saved_count += 1
        
    count += 1

cap.release()
print(f"Готово! Збережено рівно {saved_count} картинок у папку '{output_folder}'.")