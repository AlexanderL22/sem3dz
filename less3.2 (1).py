# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = "Your advertisement could be here"
max_len = max(len(w) for w in text.split())
for i, item in enumerate(sorted(text.split()), start=1):
    print(f'{i} {item :>{max_len}}')