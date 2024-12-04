import tkinter as tk
import time

def draw_circle(canvas, x, y, r):
    """Функция для рисования заполненного круга."""
    # Создание градиента
    for i in range(r):
        color_value = int(255 * (1 - i / r))  # Вычисление значения цвета
        color = f'#{color_value:02x}{color_value:02x}{255:02x}'  # Градиент от синего к прозрачному
        canvas.create_oval(x - r + i, y - r + i, x + r - i, y + r - i, fill=color, outline="")

def main():
    # Создание основного окна
    root = tk.Tk()
    root.title("Координатная плоскость")

    # Настройка канваса
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Настройка начальных параметров круга и FPS
    fps_label = tk.Label(root, text="FPS: 0", font=("Arial", 12))
    fps_label.pack()
    frame_count = 0  # Счетчик кадров
    elapsed_time = 0
    x, y, r = 200, 200, 50
    speed = 50  # Скорость движения в пикселях в секунду
    dx, dy = 2, 1  # Начальные значения направления
    last_time = time.time()  # Время последнего обновления
    last_update_time = 0  # Время последнего обновления FPS

    def update_circle():
        nonlocal x, y, dx, dy, frame_count, last_update_time, last_time
        canvas.delete("all")  # Очистка канваса
        draw_circle(canvas, x, y, r)  # Рисование круга

        # Обновление координат на основе времени
        current_time = time.time()
        delta_time = current_time - last_time  # Время, прошедшее с последнего обновления
        last_time = current_time  # Обновление времени последнего обновления
        x += dx * speed * delta_time  # Обновление координаты X
        y += dy * speed * delta_time  # Обновление координаты Y

        # Проверка границ канваса
        if x - r <= 0 or x + r >= 400:
            dx = -dx  # Изменение направления по оси X
        if y - r <= 0 or y + r >= 400:
            dy = -dy  # Изменение направления по оси Y

        # Увеличение счетчика кадров
        frame_count += 1

        # Обновление FPS каждые 60 кадров
        current_time = int(time.time() * 1000)  # Get current time in milliseconds
        if current_time - last_update_time >= 1000:  # Каждую секунду
            fps_label.config(text=f"FPS: {frame_count}")  # Обновление метки FPS
            frame_count = 0  # Сброс счетчика кадров
            last_update_time = current_time  # Обновление времени последнего обновления

        # Запланировать следующий кадр
        root.after(8, update_circle) # Примерно 120 FPS

    # Запуск анимации
    update_circle()

    # Запуск главного цикла
    root.mainloop()

if __name__ == "__main__":
    main()
