import scipy
import numpy

#1 )  Даны две  независимые выборки. Не соблюдается условие нормальности
#x1  380,420, 290
#y1 140,360,200,900
#Сделайте вывод по результатам, полученным с помощью функции
print ("Задача 1")
print ()

x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

print(scipy.stats.mannwhitneyu(x1,y1))
print("pvalue > alfa(0.05). Отсутствие статистически значимых различий между выборками позволяет нам принять нулевую гипотезу.")

#2 ) Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут.
# Есть ли статистически значимые различия?
#1е измерение до приема препарата: 150, 160, 165, 145, 155
#2е измерение через 10 минут: 140, 155, 150,  130, 135
#3е измерение через 30 минут: 130, 130, 120, 130, 125
print ()
print ("Задача 2")
print ()

x_one = 150, 160, 165, 145, 155
x_two = 140, 155, 150,  130, 135
x_three = 130, 130, 120, 130, 125
print(scipy.stats.friedmanchisquare(x_one, x_two, x_three))
print("pvalue < alfa(0.05). Соответственно статистически значимые различия имеются. Препарат оказывает влияние на давление.")

#3 ) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
print ()
print ("Задача 3")
print ()

print(scipy.stats.wilcoxon(x_one, x_two))
print("pvalue > alfa(0.05). Соответственно статистически значимых различий нет. Препарат не оказывает влияние на давление.")

#4) Даны 3 группы  учеников плавания. Сделайте вывод по различиям.
#В 1 группе время на дистанцию 50 м составляют:
#56, 60, 62, 55, 71, 67, 59, 58, 64, 67
#Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
#Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
print ()
print ("Задача 4")
print ()

one = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
two = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
three = [57, 67, 49, 48, 47, 55, 66, 51, 54]
print(scipy.stats.kruskal(one, two, three))
print("pvalue > alfa(0.05). Соответственно статистически значимых различий нет.")

#5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения.
# Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
print ()
print ("Задача 5")
print ()

array = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
mean = numpy.mean(array)
std = numpy.std(array, ddof=1)
t = (mean - 2.5) / (std/numpy.sqrt(10))
print(scipy.stats.t.ppf(0.025,9),"<",t,"<",scipy.stats.t.ppf(0.975,9),"Соответственно нулевая гипотеза верна: среднее арифметическое деталей = 2,5 см.")