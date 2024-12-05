import time
import tkinter as tk
from vec3 import vec3
from scene import Scene
from camera import Camera
from light import Light
from objects import Sphere

def main():
    # Глобальная переменная для режима отрисовки
    render_mode = 'lighting'
    # Создание сцены
    scene = Scene(width=400, height=400)
    
    # Добавление камеры
    camera = Camera()
    scene.set_camera(camera)
    
    # Добавление источника света
    light = Light(vec3(0.5, -1, 0.5))
    scene.add_light(light)
    
    # Добавление сферы
    sphere = Sphere(vec3(200, 200, 0), 50)
    scene.add_object(sphere)
    
    # Обработчик переключения режима отрисовки
    def toggle_render_mode(event):
        nonlocal render_mode
        if render_mode == 'lighting':
            render_mode = 'outline'
        else:
            render_mode = 'lighting'
    
    # Привязка клавиши 'R' к переключению режима
    scene.root.bind('r', toggle_render_mode)
    
    # Настройка анимации
    frame_count = 0
    last_time = time.time()
    fps_last_time = time.time()
    
    def update():
        nonlocal frame_count, last_time, fps_last_time
        
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        # Обновление камеры
        camera.rotate(delta_time)
        
        # Отрисовка сцены с текущим режимом
        scene.render(render_mode)
        
        # Обновление FPS
        frame_count += 1
        if current_time - fps_last_time >= 1:
            scene.fps_label.config(text=f"FPS: {frame_count}")
            fps_last_time = current_time
            frame_count = 0
            
        scene.root.after(8, update)
    
    # Запуск анимации
    update()
    
    # Запуск главного цикла
    scene.run()

if __name__ == "__main__":
    main()
