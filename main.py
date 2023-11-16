import math


# Функция чтения выборки из файла sample.txt
def read_sample():
    data = open("sample.txt").readlines()
    data = list(map(lambda value: float(str(value).replace("\n", "")), data))
    return data


# Функция формирования вариационного ряда выборки
def get_variational_series(sample):
    return sorted(sample)


# Функция определения размаха выборки
def get_range(sample):
    return max(sample) - min(sample)


# Функция формирования статистического ряда выборки
def get_statistic_series(sample):
    sample = get_variational_series(sample)
    variants = []
    frequencies = []
    relative_frequencies = []

    for value in sample:
        if value in variants:
            frequencies[variants.index(value)] += 1
        else:
            variants.append(value)
            frequencies.append(1)

    for frequency in frequencies:
        relative_frequencies.append(frequency / len(sample))

    return [variants, frequencies, relative_frequencies]


# Функция определения кол-ва интервалов выборки
def get_interval_count(sample):
    return math.ceil(1 + math.log2(len(sample)))


# Функция определения длины интервала выборки
def get_interval_length(sample):
    return (max(sample) - min(sample)) / (1 + math.log2(len(sample)))


# Функция формирования интервального статистического ряда
def get_interval_statistic_series(sample):
    sample = get_variational_series(sample)
    intervals = []
    frequencies = []

    h = get_interval_length(sample)

    for i in range(get_interval_count(sample)):
        if i == 0:
            intervals.append([min(sample) - h / 2, min(sample) + h / 2])
        else:
            intervals.append([intervals[i - 1][1], intervals[i - 1][1] + h])

    for interval in intervals:
        counter = 0
        for value in sample:
            if interval[0] <= value < interval[1]:
                counter += 1
        frequencies.append(counter)

    return [intervals, frequencies]


# Функция формирования эмперической функции распределения выборки
def get_empirical_function(sample):
    statistic_series = get_statistic_series(sample)
    relative_frequencies = statistic_series[2]

    function_values = [0]

    for relative_frequency in relative_frequencies:
        function_values.append(function_values[-1] + relative_frequency)

    return function_values


# Функция определения математического ожидания выборки
def get_expected_value(sample):
    statistic_series = get_statistic_series(sample)
    values = statistic_series[0]
    relative_frequencies = statistic_series[2]

    expected_value = 0

    for i in range(len(values)):
        expected_value += values[i] * relative_frequencies[i]

    return expected_value


# Функция определения дисперсии выборки
def get_dispersion(sample):
    statistic_series = get_statistic_series(sample)
    values = statistic_series[0]
    relative_frequencies = statistic_series[2]
    expected_value = get_expected_value(sample)

    dispersion = 0

    for i in range(len(values)):
        dispersion += (values[i] - expected_value) ** 2 * relative_frequencies[i]

    return dispersion


# Функция определения исправленной выборочной дисперсии
def get_fixed_dispersion(sample):
    statistic_series = get_statistic_series(sample)
    values = statistic_series[0]
    frequencies = statistic_series[1]
    expected_value = get_expected_value(sample)

    fixed_dispersion = 0

    for i in range(len(values)):
        fixed_dispersion += (values[i] - expected_value) ** 2 * frequencies[i]
    fixed_dispersion /= len(sample) - 1

    return fixed_dispersion

# Функция определения среднеквадратичного отклонения выборки
def get_standard_deviation(sample):
    return get_dispersion(sample) ** 0.5


# Функция определения исправленного среднеквадратичного отклонения
def get_fixed_standard_deviation(sample):
    return get_fixed_dispersion(sample) ** 0.5


sample = read_sample()
# print("Выборка:", sample)
#
# print("Вариационный ряд:", get_variational_series(sample))
#
# print("Размах:", get_range(sample))
#
# print("Статистический ряд:")
# statistic_series = get_statistic_series(sample)
# print("Варианты:", statistic_series[0])
# print("Частоты:", statistic_series[1])
# print("Относительные частоты:", statistic_series[2])
# print("Интервальный статистический ряд:")
# interval_statistic_series = get_interval_statistic_series(sample)
# print("Промежутки:", interval_statistic_series[0])
# print("Кол-во наблюдений:", interval_statistic_series[1])

print(get_empirical_function(sample))

print(get_expected_value(sample))

print(get_dispersion(sample))

print(get_standard_deviation(sample))