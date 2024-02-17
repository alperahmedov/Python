#От конзолата се четат 3 реда:
#1.	Рекордът в секунди – реално число;
#2.	Разстоянието в метри – реално число;
#3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
#Изход
#Отпечатването на конзолата зависи от резултата:
#•	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
#o	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
#•	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
#o	"No, he failed! He was {недостигащите секунди} seconds slower."
#Резултатът трябва да се форматира до втория знак след десетичната запетая.

word_record_in_second = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

distance_for_swimming = distance_in_meters * time_in_seconds_for_one_meter
additional_time = int(distance_in_meters / 15) * 12.5
total_time = distance_for_swimming + additional_time

if total_time < word_record_in_second:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - word_record_in_second
    print(f"No, he failed! He was {diff:.2f} seconds slower.")