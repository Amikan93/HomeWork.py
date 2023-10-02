def common_elements_in_all_tuples(tuple1, tuple2, tuple3):
    common_elements = set(tuple1) & set(tuple2) & set(tuple3)
    return list(common_elements)

def unique_elements_in_each_tuple(tuple1, tuple2, tuple3):
    unique_elements = set(tuple1) ^ set(tuple2) ^ set(tuple3)
    return list(unique_elements)

def common_elements_at_same_position(tuple1, tuple2, tuple3):
    common_elements = []
    min_length = min(len(tuple1), len(tuple2), len(tuple3))

    for i in range(min_length):
        if tuple1[i] == tuple2[i] == tuple3[i]:
            common_elements.append(tuple1[i])

    return common_elements

# Пример использования
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 3, 4, 5, 6)
tuple3 = (3, 4, 5, 6, 7)

# Задание 1
result1 = common_elements_in_all_tuples(tuple1, tuple2, tuple3)
print("Общие элементы во всех кортежах:", result1)

# Задание 2
result2 = unique_elements_in_each_tuple(tuple1, tuple2, tuple3)
print("Уникальные элементы в каждом кортеже:", result2)

# Задание 3
result3 = common_elements_at_same_position(tuple1, tuple2, tuple3)
print("Общие элементы на той же позиции в каждом кортеже:", result3)