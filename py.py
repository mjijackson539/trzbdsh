import numpy as np
data_steps = np.array([ 8200, 11500, 9400, 7100, 10800, 8600, 12900, 45000, 9900, 9100, 7600, 11300,
                       8300, 9700, 10400, 8900, 12100, 6800, 10200, 9200, 200, 450, 8100, 11600, 7900,
                         9600, 10700, 8700, 12200, 6900 ])

print("Среднее значение:", np.mean(data_steps))
print("Медиана:", np.median(data_steps))
print("Стандартное отклонение:", np.std(data_steps))
print("Дисперсия:", np.var(data_steps))

print("Максимальное значение:", np.max(data_steps))
print("Минимальное значение:", np.min(data_steps))
print("Размах:", np.max(data_steps) - np.min(data_steps))

print("25-й перцентиль:", np.percentile(data_steps, 25)) 
print("50-й перцентиль:", np.percentile(data_steps, 50)) 
print("75-й перцентиль:", np.percentile(data_steps, 75)) 
print("90-й перцентиль:", np.percentile(data_steps, 90)) 
print("99-й перцентиль:", np.percentile(data_steps, 99))

Q1 = np.percentile(data_steps, 25) 
Q2 = np.percentile(data_steps, 50) 
Q3 = np.percentile(data_steps, 75)
print("Первый квартиль Q1:", Q1) 
print("Второй квартиль Q2:", Q2)
print("Третий квартиль Q3:", Q3)

IQR = Q3 - Q1
print("Межквартильный размах IQR:", IQR)
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
print("Нижняя граница:", lower_limit) 
print("Верхняя граница:", upper_limit)

outliers = data_steps[ (data_steps < lower_limit) | (data_steps > upper_limit) ]
print("Выбросы:", outliers)

A = np.array([ 8000, 12000, 9500, 7000, 11000, 8500, 13000, 6000, 10000, 9000, 7500,
               11500, 8200, 9800, 10500 ])
matrix = A.reshape(3, 5)
print("Матрица 3x5:") 
print(matrix)

print("Размерность матрицы:", matrix.shape)
print("Количество элементов:", matrix.size)
print("Сумма по строкам:", np.sum(matrix, axis=1))
print("Сумма по столбцам:", np.sum(matrix, axis=0))
print("Транспонированная матрица:") 
print(matrix.T)
print("Среднее значение:", np.mean(matrix)) 
print("Стандартное отклонение:", np.std(matrix))
print("Дисперсия:", np.var(matrix))
print("Первый квартиль:", np.percentile(matrix, 25)) 
print("Второй квартиль:", np.percentile(matrix, 50)) 
print("Третий квартиль:", np.percentile(matrix, 75))

days_less_8000 = np.sum(data_steps < 8000)
print("Количество дней где шагов меньше 8000:", days_less_8000)
