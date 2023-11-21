import numpy as np
import pandas as pd
from scipy import stats

f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sh= np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# Сформулируем нулевую гипотезу:
#  средний рост спортсмена не зависит от вида спорта, которым он занимается(из представленных трех).
# Альтернативная гипотеза:
# средний рост спортсмена зависит от выбранного им спорта.

# Воспользуемся встроенным методом однофакторного дисперсионного анализа библиотеки scipy:
stats.f_oneway(f, h, sh)

# F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698693)

# Получили значение pvalue=0.010482 на уровне статистической значимости альфа = 0.05 отвергаем нулевую гипотезу. 
# Т.е. средний рост футболистов, хоккеистов и штангистов различен.
# При этом на уровне значимости альфа = 0,01 нулевую гипотезу отвергнуть не можем