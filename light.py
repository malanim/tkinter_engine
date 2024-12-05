from vec3 import vec3

class Light:
    def __init__(self, direction: vec3):
        """Инициализация источника света."""
        self.direction = direction.normalize()
        
    def get_intensity(self, normal: vec3):
        """Вычисление интенсивности освещения для данной нормали."""
        return max(0, normal.dot(self.direction))
