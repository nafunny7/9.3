first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = zip(len(x) - len(y) for x, y in zip(first, second) if not len(x) == len(y))
print(list(first_result))
second_result = [bool(len(first[i]) == len(second[i])) for i in range(min(len(first), len(second)))]
print(list(second_result))
