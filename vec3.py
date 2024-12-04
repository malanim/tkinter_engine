import math

class vec3:
    def __init__(self, x, y, z):
        """Инициализация 3D вектора."""
        self.x = x
        self.y = y
        self.z = z

    def _check_vector(self, other):
        """Проверка, является ли объект вектором.""" 
        if not isinstance(other, vec3):
            raise TypeError("Операция возможна только с объектами vec3.")
        # Удаляем ненужный возврат

    def operate(self, other, operation):
        """Выполняет операцию с вектором или скаляром."""
        if isinstance(other, vec3):
            if operation == 'add':
                return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
            elif operation == 'subtract':
                return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
            elif operation == 'multiply':
                return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
            elif operation == 'divide':
                if other.x == 0 or other.y == 0 or other.z == 0:
                    raise ValueError("Деление на ноль невозможно.")
                return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (int, float)):
            if operation == 'add':
                return vec3(self.x + other, self.y + other, self.z + other)
            elif operation == 'subtract':
                return vec3(self.x - other, self.y - other, self.z - other)
            elif operation == 'multiply':
                return vec3(self.x * other, self.y * other, self.z * other)
            elif operation == 'divide':
                if other == 0:
                    raise ValueError("Деление на ноль невозможно.")
                return vec3(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Операция возможна только с объектами vec3 или скалярами.")

    def length(self):
        """Возвращает длину вектора."""
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def normalize(self):
        """Нормализация вектора."""
        length = self.length()
        if length == 0:
            raise ValueError("Невозможно нормализовать нулевой вектор.")
        return self.operate(length, 'divide')

    def dot(self, other):
        """Скалярное произведение двух векторов."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """Векторное произведение двух векторов."""
        return vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __add__(self, other):
        """Перегрузка оператора сложения."""
        return self.add(other)

    def __sub__(self, other):
        """Перегрузка оператора вычитания."""
        return self.subtract(other)

    def __mul__(self, scalar):
        """Перегрузка оператора умножения."""
        return self.multiply(scalar)

    def __truediv__(self, scalar):
        """Перегрузка оператора деления."""
        return self.divide(scalar)

    def to_tuple(self):
        """Преобразование вектора в кортеж."""
        return (self.x, self.y, self.z)

    @classmethod
    def from_tuple(cls, tup):
        """Создание вектора из кортежа."""
        return cls(tup[0], tup[1], tup[2])

    def angle_between(self, other):
        """Вычисляет угол между двумя векторами в радианах."""
        self._check_vector(other)
        cos_angle = self.dot(other) / (self.length() * other.length())
        return math.acos(cos_angle)

    def distance_to(self, other):
        """Вычисляет расстояние между двумя векторами."""
        self._check_vector(other)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

    def reflect(self, normal):
        """Отражает вектор от поверхности, определяемой нормальным вектором."""
        self._check_vector(normal)
        dot_product = self.dot(normal)
        return vec3(
            self.x - 2 * dot_product * normal.x,
            self.y - 2 * dot_product * normal.y,
            self.z - 2 * dot_product * normal.z
        )

    def add_vectors(vectors):
        """Суммирует массив векторов."""
        result = vec3(0, 0, 0)
        for vector in vectors:
            result = result.operate(vector, 'add')
        return result

    def subtract_vectors(vectors):
        """Вычитает массив векторов из первого вектора."""
        if not vectors:
            raise ValueError("Список векторов не может быть пустым.")
        result = vectors[0]
        for vector in vectors[1:]:
            result = result.operate(vector, 'subtract')
        return result

    def normalize_vectors(vectors):
        """Нормализует массив векторов."""
        return [vector.normalize() for vector in vectors]
    
    def __repr__(self):
        """Строковое представление вектора."""
        return f"vec3({self.x}, {self.y}, {self.z})"
