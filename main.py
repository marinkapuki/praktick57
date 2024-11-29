import random
import string
from collections import defaultdict

def input_data():
    """Ввод данных вручную."""
    return input("Введите текст: ")

def generate_random_data():
    """Генерация случайных данных."""
    return ''.join(random.choices(string.ascii_lowercase + ' ', k=50))

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
                text = generate_random_data()
                print(f"Сгенерированный текст: {text}")
            else:
                print("Неверный выбор.")
            results = None  # Сбрасываем результаты при вводе новых данных
        
        elif choice == '2':
            results = find_anagrams(text)
            if results is not None:
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