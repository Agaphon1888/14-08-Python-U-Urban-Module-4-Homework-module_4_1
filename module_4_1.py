# Домашняя работа по уроку "Модули и пакеты".
# Задача "А как делить?"
# Главный модуль.

import fake_math as zero_m
import true_math as inf_m



fake_divide = zero_m.divide
true_divide = inf_m.divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)