import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import control as ctrl

# Вхідні дані
K = 0.62   # коефіцієнт передачі
To = 220   # сталий час (с)
tau = 70   # час запізнювання (с)

# Опис передатної функції
numerator = [K]   # чисельник
denominator = [tau, 1]  # знаменник для першого порядку
system = ctrl.TransferFunction(numerator, denominator)

# Апроксимація Паде для затримки часу
num_delay, den_delay = ctrl.pade(tau, 10)  # 10-й порядок апроксимації Паде
delay_system = ctrl.TransferFunction(num_delay, den_delay)

# Система з затримкою
system_with_delay = ctrl.series(delay_system, system)

# Симулюємо відповідь на крок
time = np.linspace(0, 1000, 1000)  # час від 0 до 1000 секунд
time_out, response = ctrl.step_response(system_with_delay, time)

# Показати графік розгону
plt.figure()
plt.plot(time_out, response, label="Розгін з запізнюванням")
plt.title("Крива розгону системи")
plt.xlabel("Час (с)")
plt.ylabel("Вихідна величина")
plt.legend()
plt.grid(True)
plt.savefig('response_plot.png')  # Зберегти графік у файл
plt.show()

# Передатна функція
print(f"Передатна функція об'єкта керування: G(s) = {K}/({tau}s + 1) * exp(-{tau}s)")
