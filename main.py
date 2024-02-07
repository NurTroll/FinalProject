""" Это основной модуль программы"""

import tkinter as tk
import time
from tkinter import ttk, messagebox
from sorting_module import sorting_module


def sort_numbers():
    """Функция сортировки списка в зависимоти от выбраного метода сортировки
    :return str
    """
    # Получаем введенные числа и выбранный тип сортировки
    sorted_numbers = []
    numbers = numbers_entry.get()
    sort_type = sort_type_combobox.get()

    if not numbers or not sort_type:
        messagebox.showerror("Ошибка", "Введите числа и выберите тип сортировки")
        return

    # Преобразуем строку с числами в список
    try:
        numbers = list(map(int, numbers.split(',')))
    except ValueError:
        messagebox.showerror("Ошибка", "Вводите только числа, разделенные запятой")
        return

    # Засекаем время начала сортировки
    start_time = time.time()

    # Выполняем сортировку
    match sort_type:
        case 'Сортировка пузырьком':
            sorted_numbers = sorting_module.bubble_sort(numbers)
        case 'Сортировка подсчетом':
            k = max(numbers)
            sorted_numbers = sorting_module.counting_sort(numbers, k)
        case 'Пирамидальная сортировка(Heap Sort)':
            sorting_module.heap_sort(numbers)
            sorted_numbers = numbers
        case 'Сортировка слиянием':
            sorted_numbers = sorting_module.marge_sort(numbers)
        case 'Быстрая сортировка':
            sorted_numbers = sorting_module.quicksort(numbers)
        case 'Поразрядная сортировка(Radix Sort)':
            sorted_numbers = sorting_module.radix_sort(numbers)
        # Вычисляем затраченное время
    elapsed_time = time.time() - start_time
    minutes, rem = divmod(elapsed_time, 60)
    seconds, milliseconds = divmod(rem, 1)
    # Выводим отсортированные числа и затраченное время
    result_label.config(text=f"Отсортированные числа: {sorted_numbers}\n"
                             f"Время сортировки: {int(minutes)} минут {int(seconds)} секунд "
                             f"{float(milliseconds*1000)} миллисекунд")


def clear_entry():
    """Функция очистки поля ввода списка из чисел"""
    numbers_entry.delete(0, 'end')


root = tk.Tk()
root.title("Сортировка чисел")
root.geometry("600x400")
# Создаем элементы интерфейса
numbers_label = tk.Label(root, text="Введите числа, разделенные запятой:")
numbers_entry = tk.Entry(root, width=50)
clear_button = tk.Button(root, text="Очистить", command=clear_entry)
sorting_label = tk.Label(root, text='Выберите сортировку:')
sort_type_combobox = ttk.Combobox(root, values=["Сортировка пузырьком",
                                                "Сортировка подсчетом",
                                                "Пирамидальная сортировка(Heap Sort)",
                                                "Сортировка слиянием",
                                                "Быстрая сортировка",
                                                "Поразрядная сортировка(Radix Sort)"], width=40)
sort_button = tk.Button(root, text="Сортировать", command=sort_numbers)
result_label = tk.Label(root)


# Размещаем элементы на форме
numbers_label.pack()
numbers_entry.pack()
clear_button.pack()
sorting_label.pack()
sort_type_combobox.pack()
sort_button.pack()
result_label.pack()

root.mainloop()
