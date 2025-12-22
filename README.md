# Лабораторная работа №1

## задание №1

![alt text](images/lab1/1.png)

## задание №2

![alt text](images/lab1/2.png)

## задание №3

![alt text](images/lab1/3.png)

## задание №4

![alt text](images/lab1/4.png)

## задание №5

![alt text](images/lab1/5.png)

#### -


# Лабораторная работа №2

## задание №1

![alt text](images/lab2/arrays.png)

## задание №2

![alt text](images/lab2/matrix.png)


## задание №3

![alt text](images/lab2/tuples.png)

#### -


# Лабораторная работа №3

## задание №1

![alt text](images/lab3/text.png)

## задание №2

![alt text](images/lab3/text_stats.png)

### вариант оформления задания №2 через таблицу

![alt text](images/lab3/text_stats_table.png)

#### -


# Лабораторная работа №4

## Задание №1

### Примеры вывода из мини теста:

![alt text](images/lab4/mini_test_lab4.png)

### Вывод в check.csv

![alt text](images/lab4/check.csv_lab4.png)

## Задание №2

### Здесь написан скрипт, который читает файл input и импортирует функции из lib (из ЛР3)

![alt text](images/lab4/text_report_lab4.png)

### Выполнив скрипт, который введен в консоль в файл report.csv я вывел следующую информацию:

![alt text](images/lab4/report.csv_lab4.png)

#### -


# Лабораторная работа №5

## Задание A

### пример ввода csv-файла:

![alt text](images/lab5/ввод_people.csv.png)

### вывод конвертации csv-файла в JSON:

![alt text](images/lab5/вывод_people_from_csv.json.png)

### также эти манипуляции модно провести и с JSON-файлом:

![alt text](images/lab5/ввод_people.json%20.png)

### пример вывода в csv-файл;:

![alt text](images/lab5/вывод_people_from_json.csv.png)

## Задание B

### вот тот же csv-файл:

![alt text](images/lab5/ввод_people.csv.png)

### проводим конвертацию в Excel-файл:

![alt text](images/lab5/вывод_people.xlsx.png)

#### -


# Лабораторная работа №6

## Модуль cli_text

### Выполнение команды Cat:

![alt text](images/lab6/команда_Cat.png)

### Выполнение команды Stats:

![alt text](images/lab6/команда_Stats.png)

### Оформление help:

![alt text](images/lab6/help_cli_text.png)

## Модуль cli_convert

### Работу функций из данного модуля можем увидеть в ЛР №5
### Поэтому приведу только оформление help:

![alt text](images/lab6/help_cli_convert.png)

#### -


# Лабораторная работа №7

## Тестирование кода:

### Тест кода из text_text (из ЛР №3):

![alt text](images/lab7/test_text.png)

### Тест кода из text_json_csv (из ЛР №5):

![alt text](images/lab7/test_json_csv.png)

## Покрытие кода:

![alt text](images/lab7/test_cover.png)

## Отчет форматирования проекта на стиль black:

![alt text](images/lab7/black_test.png)

#### -


# Лабораторная работа №8

## students to json:

### Запись json-файла, используя класс Student из модуля models.py:

![alt text](images/lab8/students_output.json.png)

## students_from_json:

### Чтение json-файла:

![alt text](images/lab8/students_input.json.png)

## Вывод информации в консоль:

![alt text](images/lab8/вывод_в_консоль.png)

#### -

# Лабораторная работа №9

## База данных на csv-файлах:

### пустая база данных с полями:

![alt text](images/lab9/пустая_база_данных.png)

### пример выполнения кода с выводами в консоль:

![alt text](images/lab9/вывод_в_консоль.png)

## база данных после выполнения кода:

![alt text](images/lab9/база_данных.png)

#### -



# Лабораторная работа №10

## Stack и Queue:

### Stack - принцип LIFO (Last In, First Out). Основные операции: push, pop, peek, is_empty.
### Queue - принцип FIFO (First In, First Out). Основные операции: enqueue, dequeue, peek, is_empty.

![alt text](images/lab10/lab10_structures.png)

### выводы по бенчмаркам:

#### Stack (list) — push/pop O(1), быстрые операции.
#### Queue (deque) — enqueue/dequeue O(1), быстрее, чем list (pop(0) → O(n)).

## SinglyLinkedList:

### - односвязный список. Основные операции: prepend, append, insert, remove, поиск.

![alt text](images/lab10/lab10_linked_list.png)

### выводы по бенчмаркам:

#### SinglyLinkedList — prepend/append O(1) при наличии tail, вставка/удаление в середине O(n), доступ по индексу O(n).