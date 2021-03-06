class Vector2D:
  def __init__(self, x, y):
      self.x = x
      self.y = y

  def __add__(self, otro):
      return Vector2D(self.x + otro.x, self.y + otro.y)

v1 = Vector2D(5, 7)
v2 = Vector2D(3, 9)
resultado = v1 + v2

print(resultado.x)  # 8
print(resultado.y)  # 16