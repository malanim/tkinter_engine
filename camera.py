import math
from vec3 import vec3

class Camera:
    def __init__(self, position=vec3(0, 0, 0), up_vector=vec3(0, 1, 0), angle=0):
        """Инициализация камеры."""
        self.position = position
        self.look_at = vec3(0, 0, 0)  # Центр координат
        self.up_vector = up_vector
        self.angle = angle
        self.radius = 100  # Радиус вращения
        self.direction_vector = vec3(0, 0, -1)  # Вектор направления по умолчанию

    def rotate(self, delta_time):
        """Вращение камеры вокруг центра координат."""
        self.angle += delta_time * 0.5
        if self.angle >= 2 * math.pi:
            self.angle = 0
        
        # Обновление позиции камеры
        self.position.x = self.radius * math.cos(self.angle)
        self.position.y = self.radius * math.sin(self.angle)
        self.position.z = self.position.z  # Можно изменить, если нужно поднять камеру

        # Обновление вектора направления
        self.direction_vector = vec3(math.cos(self.angle), 0, math.sin(self.angle))

    def get_transform_matrix(self):
        """Получение матрицы трансформации для текущего положения камеры."""
        return {
            'cos_angle': math.cos(self.angle),
            'sin_angle': math.sin(self.angle)
        }
