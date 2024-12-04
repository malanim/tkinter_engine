import tkinter as tk
import math
import time
from vec3 import vec3

def draw_sphere(canvas, center, radius, light_direction, camera_angle):
    """Функция для рисования 3D шара с учетом освещения."""
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            if i**2 + j**2 <= radius**2:  # Проверка, находится ли точка внутри шара
                # Вычисление координат точки на поверхности шара
                x = i
                y = j
                z = math.sqrt(radius**2 - i**2 - j**2)

                # Создание нормали для текущей точки (относительно центра шара)
                normal = vec3(x, y, z).normalize()

                # Поворот нормали вокруг оси Y
                rotated_normal = vec3(
                    normal.x * math.cos(camera_angle) + normal.z * math.sin(camera_angle),
                    normal.y,
                    -normal.x * math.sin(camera_angle) + normal.z * math.cos(camera_angle)
                )

                # Вычисление интенсивности освещения
                intensity = rotated_normal.dot(light_direction)
                
                # Отрисовываем только освещенные пиксели
                if intensity > 0:
                    # Вычисление цвета с учетом базового цвета (синего)
                    # Интенсивность определяет как сильно цвет будет отличаться от черного
                    blue = int(255 * intensity)
                    other = int(128 * intensity)  # Другие компоненты для создания градиента
                    color = f'#{other:02x}{other:02x}{blue:02x}'

                    # Отрисовка пикселя
                    screen_x = center[0] + i
                    screen_y = center[1] + j
                    canvas.create_rectangle(screen_x, screen_y, screen_x + 1, screen_y + 1, 
                                         fill=color, outline="")

def main():
    # Создание основного окна
    root = tk.Tk()
    root.title("Координатная плоскость")

    # Настройка канваса
    canvas = tk.Canvas(root, width=400, height=400, bg="black")
    canvas.pack()

    # Настройка начальных параметров
    fps_label = tk.Label(root, text="FPS: 0", font=("Arial", 12))
    fps_label.pack()
    frame_count = 0
    center = (200, 200)  # Центр шара
    radius = 50  # Радиус шара
    camera_angle = 0  # Угол поворота камеры
    
    # Фиксированное направление света (сверху и слегка сбоку)
    light_direction = vec3(0.5, -1, 0.5).normalize()

    def update_sphere():
        nonlocal camera_angle, frame_count
        canvas.delete("all")  # Очистка канваса

        # Рисование шара
        draw_sphere(canvas, center, radius, light_direction, camera_angle)

        # Обновление угла камеры
        camera_angle += 0.5  # Увеличиваем скорость вращения
        if camera_angle >= 2 * math.pi:
            camera_angle = 0

        # Обновление счетчика кадров
        frame_count += 1
        if frame_count % 30 == 0:  # Обновление FPS каждые 30 кадров
            fps_label.config(text=f"FPS: {frame_count}")
            frame_count = 0

        # Запланировать следующий кадр
        root.after(8, update_sphere)  # ~120 FPS

    # Запуск анимации
    update_sphere()

    # Запуск главного цикла
    root.mainloop()

if __name__ == "__main__":
    main()
