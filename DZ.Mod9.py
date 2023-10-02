#Задание 1

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            print(f"Файл 1: {line1.strip()}")
            print(f"Файл 2: {line2.strip()}")
            print("")

# Пример использования
file1_path = 'file1.txt'
file2_path = 'file2.txt'
compare_files(file1_path, file2_path)

#Задание 2

def generate_statistics(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()

    num_chars = len(content)
    num_lines = content.count('\n')
    num_vowels = sum(1 for char in content if char.lower() in 'aeiou')
    num_consonants = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiou')
    num_digits = sum(1 for char in content if char.isdigit())

    statistics = (
        f"Количество символов: {num_chars}\n"
        f"Количество строк: {num_lines}\n"
        f"Количество гласных букв: {num_vowels}\n"
        f"Количество согласных букв: {num_consonants}\n"
        f"Количество цифр: {num_digits}\n"
    )

    with open(output_file_path, 'w') as output_file:
        output_file.write(statistics)

# Пример использования
input_file_path = 'input.txt'
output_file_path = 'statistics_output.txt'
generate_statistics(input_file_path, output_file_path)

#Задание 3

def remove_last_line(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(lines[:-1])

# Пример использования
input_file_path = 'input.txt'
output_file_path = 'output_without_last_line.txt'
remove_last_line(input_file_path, output_file_path)

#Задание 4

def find_longest_line_length(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    max_length = max(len(line) for line in lines)
    return max_length

# Пример использования
file_path = 'text_file.txt'
longest_line_length = find_longest_line_length(file_path)
print(f"Длина самой длинной строки: {longest_line_length}")

#Задание 5

def count_word_occurrences(file_path, target_word):
    with open(file_path, 'r') as file:
        content = file.read()

    occurrences = content.lower().count(target_word.lower())
    return occurrences

# Пример использования
file_path = 'text_file.txt'
target_word = 'python'
word_occurrences = count_word_occurrences(file_path, target_word)
print(f"Слово '{target_word}' встречается {word_occurrences} раз.")

#Задание 6

def replace_word(file_path, target_word, replacement):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content.replace(target_word, replacement)

    with open(file_path, 'w') as file:
        file.write(updated_content)

# Пример использования
file_path = 'text_file.txt'
target_word = 'old_word'
replacement = 'new_word'
replace_word(file_path, target_word, replacement)