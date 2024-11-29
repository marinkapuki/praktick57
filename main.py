import random
import string
from collections import defaultdict

def input_data():
    """Ввод данных вручную."""
    return input("Введите текст: ")

def generate_random_data(length=50):
    """Генерация случайных данных заданной длины."""
    return ''.join(random.choices(string.ascii_lowercase + ' ', k=length))

def find_anagrams(text):
    """Находит анаграммы в заданном тексте."""
    words = text.split()
    anagrams = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return {key: value for key, value in anagrams.items() if len(value) > 1}

def display_results(results):
    """Выводит результаты выполнения алгоритма."""
    if results:
        print("Найденные анаграммы:")
        for key, value in results.items():
            print(f"{', '.join(value)}")
    else:
        print("Анаграммы не найдены.")

def main_menu():
    """Главное меню приложения."""
    text = None
    results = None

    while True:
        print("\nМеню:")
        print("1) Ввод исходных данных")
        print("2) Выполнение алгоритма")
        print("3) Вывод результата")
        print("4) Завершить работу программы")

        choice = input("Выберите опцию: ")

        if choice == '1':
            option = input("Выберите способ ввода (1 - вручную, 2 - случайно): ")
            if option == '1':
                text = input_data()
            elif option == '2':
                length = input("Введите длину генерируемого текста (по умолчанию 50): ")
                try:
                    length = int(length) if length else 50
                    text = generate_random_data(length)
                    print(f"Сгенерированный текст: {text}")
                except ValueError:
                    print("Пожалуйста, введите корректное число.")
            else:
                print("Неверный выбор.")
            results = None  # Сбрасываем результаты при вводе новых данных
        
        elif choice == '2':
            if text is None:
                print("Сначала введите текст.")
            else:
                results = find_anagrams(text)
                print("Алгоритм выполнен.")
        
        elif choice == '3':
            display_results(results)
        
        elif choice == '4':
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main_menu()