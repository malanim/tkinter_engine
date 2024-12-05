import math
from vec3 import vec3

class Object3D:
    def __init__(self, position: vec3):
        """Базовый класс для 3D объектов."""
        self.position = position
        
    def draw(self, canvas, camera, lights):
        """Метод отрисовки объекта."""
        pass

class Sphere(Object3D):
    def __init__(self, position: vec3, radius: float):
        """Инициализация сферы."""
        super().__init__(position)
        self.radius = radius
        
    def draw(self, canvas, camera, lights):
        """Отрисовка сферы с учетом освещения."""
        transform = camera.get_transform_matrix()
        
        for i in range(-self.radius, self.radius):
            for j in range(-self.radius, self.radius):
                if i**2 + j**2 <= self.radius**2:
                    x = i
                    y = j
                    z = math.sqrt(self.radius**2 - i**2 - j**2)

                    normal = vec3(x, y, z).normalize()
                    
                    # Поворот нормали с учетом положения камеры
                    rotated_normal = vec3(
                        normal.x * transform['cos_angle'] + normal.z * transform['sin_angle'],
                        normal.y,
                        -normal.x * transform['sin_angle'] + normal.z * transform['cos_angle']
                    )
                    
                    # Вычисление суммарной интенсивности от всех источников света
                    total_intensity = sum(light.get_intensity(rotated_normal) for light in lights)
                    total_intensity = min(1.0, total_intensity)  # Ограничиваем максимальную яркость
                    
                    if total_intensity > 0:
                        blue = int(255 * total_intensity)
                        other = int(128 * total_intensity)
                        color = f'#{other:02x}{other:02x}{blue:02x}'
                        
                        screen_x = self.position.x + i
                        screen_y = self.position.y + j
                        canvas.create_rectangle(
                            screen_x, screen_y,
                            screen_x + 1, screen_y + 1,
                            fill=color, outline=""
                        )
