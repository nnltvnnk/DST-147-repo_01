"""
    Игра "Угадай число"
    Компьютер сам загадывает и отгадывает число за меньше, чем 20 попыток.
    (Фактически требуется не более 7 попыток, т.к. отгадывание происходит 
    путем послетовательного деления 100 на 2 (100 < 2**7).
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Функция, отгадывающая число

    Args:
        number (int, optional): Загаданное число (по умолчанию равно 1)

    Returns:
        int: Число попыток
    """

    count = 0 # Счетчик количества попыток
    predict_number = 50 # Предполагаемое число (= 100/2)
    half_range = 25 # Число, на которое будет увеличиваться или уменьшаться предполагаемое число

    while True:
        count += 1    
        
        if predict_number > number:
            predict_number -= half_range

        elif predict_number < number:
            predict_number += half_range
        
        else:
            break # Конец игры, выход из цикла
        
        half_range = np.ceil(half_range/2) # Последовательное деление предполагаемого числа на 2 с округлением результатта вверх
        
    return count

def score_game(game_core_v3) -> int:
    """Функция, проверяющая эффективность функции game_core_v3 (возвращает среднее число попыток)

    Args:
        game_core_v3([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток.")


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
