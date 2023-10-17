import numpy as np

def random_predict(number:int) -> int:
    """Угадываем число по методу. Суть метода в том, чтобы на каждой новой попвтке предполагать число,
    которое находится на середине верхней и нижней границы проверенных чисел.
    К примеру, если загаданное число больше, чем предполагаемое (например 36),
    то в следующей итерации предполагаем, что загаданное число будет в середине между 36 и 100 (68)
    если меньше 68, то берем середину между 36 и 68 и так далее
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """

    count = 0
    max_number = 100 # Устанавливаем первоначальные верхнюю и нижнюю границы
    min_number = 0
    predict_number = np.random.randint(1, 101)  # Впервые предполагаемое число берём случайное

    while True:
        count += 1

        if predict_number > number: # Изменяем границы в случае неугадывания
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2


        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2

        else:
            break  # Число совпадает, выходим из цикла

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, 1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
   

score_game(random_predict)