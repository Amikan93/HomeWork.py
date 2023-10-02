#Задание 1

def is_palindrome(s):
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]

user_input = input("Введите строку: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")

#Задание 2

def change_case(text, reserved_words):
    words = text.split()
    for i in range(len(words)):
        if words[i].lower() in reserved_words:
            words[i] = words[i].upper()
    return ' '.join(words)

user_text = input("Введите текст: ")
user_reserved_words = input("Введите зарезервированные слова через пробел: ").split()

result_text = change_case(user_text, user_reserved_words)
print("Измененный текст:")
print(result_text)

#Задание 3

def count_sentences(text):
    sentences = text.split('.')  # Предполагаем, что точка - конец предложения
    return len(sentences)

user_text = input("Введите текст: ")
sentence_count = count_sentences(user_text)
print("Количество предложений в тексте:", sentence_count)