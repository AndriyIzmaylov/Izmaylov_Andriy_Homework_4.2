# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.#
# Не забудьте, що перший елемент масиву має індекс 0.#
# Для порожнього масиву результат завжди 0.#
# Пояснення:
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

def sum_of_elements_with_even_indices(incoming_list):
    if not incoming_list:
        return 0

    even_indices_sum = sum(incoming_list[index] for index in range(0, len(incoming_list), 2))
    return even_indices_sum * incoming_list[-1]


test_cases = [
    [],
    [6],
    [1, 3, 5],
    [0, 1, 7, 2, 4, 8]
]

for case in test_cases:
    print(f"Entry list: {case}")
    print(f"Result: {sum_of_elements_with_even_indices(case)}")
    print("-" * 40)
