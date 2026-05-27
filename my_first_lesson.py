# 我的第一个 Git 练习
  print("Hello, AI Engineering!")

  # 这是一个简单的感知机实现
  def perceptron(x, w):
      return 1 if sum(xi * wi for xi, wi in zip(x, w)) >= 0 else 0
  
