import tkinter as tk
from camera import Camera
from light import Light
from objects import Object3D

class Scene:
    def __init__(self, width=400, height=400):
        """Инициализация сцены."""
        self.root = tk.Tk()
        self.root.title("3D viewer")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="black")
        self.canvas.pack()
        
        self.fps_label = tk.Label(self.root, text="FPS: 0", font=("Arial", 12))
        self.fps_label.pack()
        
        self.width = width
        self.height = height
        self.objects = []
        self.lights = []
        self.camera = None
        
    def add_object(self, obj: Object3D):
        """Добавление объекта на сцену."""
        self.objects.append(obj)
        
    def add_light(self, light: Light):
        """Добавление источника света."""
        self.lights.append(light)
        
    def set_camera(self, camera: Camera):
        """Установка камеры."""
        self.camera = camera
        
    def render(self, render_mode='lighting'):
        """Отрисовка всей сцены."""
        self.canvas.delete("all")
        if self.camera:
            for obj in self.objects:
                obj.draw(self.canvas, self.camera, self.lights, render_mode)
                
    def run(self):
        """Запуск главного цикла."""
        self.root.mainloop()
