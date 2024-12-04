def add(vec1, vec2):
    """Сложение двух векторов."""
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def subtract(vec1, vec2):
    """Вычитание второго вектора из первого."""
    return (vec1[0] - vec2[0], vec1[1] - vec2[1])

def multiply(vec, scalar):
    """Умножение вектора на скаляр."""
    return (vec[0] * scalar, vec[1] * scalar)

def divide(vec, scalar):
    """Деление вектора на скаляр."""
    if scalar == 0:
        raise ValueError("Деление на ноль невозможно.")
    return (vec[0] / scalar, vec[1] / scalar)
