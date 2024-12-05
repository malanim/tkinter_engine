import math
from vec3 import vec3

class Camera:
    def __init__(self, position=vec3(0, 0, 0), angle=0):
        """Инициализация камеры."""
        self.position = position
        self.angle = angle
        
    def rotate(self, delta_time):
        """Вращение камеры."""
        self.angle += delta_time * 0.5
        if self.angle >= 2 * math.pi:
            self.angle = 0
            
    def get_transform_matrix(self):
        """Получение матрицы трансформации для текущего положения камеры."""
        return {
            'cos_angle': math.cos(self.angle),
            'sin_angle': math.sin(self.angle)
        }
