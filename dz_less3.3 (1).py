# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
#
things = {'палатка': 250, 'спальный мешок': 75, 'консерва': 10, 'нож': 10,
          'термос': 50, 'аптечка': 50, 'бутылка': 50, 'бинокль': 100, 'спички': 30,
          'ружье': 240, 'уголь': 100, 'топор': 100, 'одежда': 100, 'Самокат': 1200}

weight_limit = 1100
temp_keys = []
temp_values = []
result = []
tools_keys = list(things.keys())
tools_values = list(things.values())

print(tools_keys)
print(tools_values)

for i in range(len(tools_keys)):
    if tools_values[i] <= weight_limit:
        temp_keys = []
        temp_values = []
        for j in range(i, len(tools_keys)):
            if sum(temp_values) + tools_values[j] <= weight_limit:
                temp_values.append(tools_values[j])
                temp_keys.append(tools_keys[j])
                print(temp_keys)