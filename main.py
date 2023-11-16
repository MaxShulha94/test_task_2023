from itertools import chain


def encrypt_text(key, input_text):
    key = [int(digit) for digit in str(key)]  # Перетворив ключ з формату str на list і розділив на елементи
    text_list = [input_text[_:_ + 2] for _ in range(0, len(input_text))]  # Розділив текст на елементи в списку
    odd_list = [text_list[_] for _ in range(0, len(text_list), 3)]  # Витягнув непарні елементи
    even_list = [input_text[_] for _ in range(2, len(input_text), 3)]  # Витягнув парні елементи
    sum_lists = []
    for odd, even in zip(odd_list, even_list):  # Злив списки в необхідному порядку в один
        sum_lists.extend([odd, even])
    if len(odd_list) > len(even_list):
        sum_lists.append(odd_list[-1])
    result = [[] for _ in range(len(key))]  # Створив матрицю і заповнив її в порядку що вказує ключ а потім
    for index, element in enumerate(sum_lists):  # перетворив це в стрічку
        result[key[index % len(key)] - 1].append(element)
    return ''.join(chain.from_iterable(result))


if __name__ == '__main__':
    assert encrypt_text("41325",
                        "INCOMPLETECOLUMNARWITHALTERNATINGSINGLELETTERSANDDIGRAPHS") == "CECRTEGLENPHPLUTNANTEIOMOWIRSITDDSINTNALINESAALEMHATGLRGR"
    assert encrypt_text("12", "HELLOWORLD") == "HELOORDLWL"
    assert encrypt_text("3412", "THISISJUSTATEST") == "SITASTTHJUESIST"
    assert encrypt_text("165432", "WORKSMARTNOTHARDT") == "WONOTARDMRKSHART"
    assert encrypt_text("231", "LLOHE") == "HELLO"


def next_sequence_elements(sequence):
    count = 0  # Створив змінну для прорахунку ітерацій
    next_elements = []  # Створив список в якому будуть додаватись 3 наступні елементи секвенції
    elem1 = sequence[-2]  # Створив змінну з передостаннім елементом секвенції
    elem2 = sequence[-1]  # Створив змінну з останнім елементом секвенції
    diff = elem2 - elem1  # Отримав різницю двох елементів
    diffs = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]  # Створив список в з різниць елементів

    if elem1 and elem2 == sequence[0] and diff == 0:  # Варіант коли елементи секвенції однакові
        return [elem1] * 3

    if diff != 0 and diffs[0] == diffs[-1]:  # Варіант коли елементи секвенції мають сталу змінну
        while count < 3:
            elem1, elem2 = elem2, elem2 + diff
            next_elements.append(elem2)
            count += 1
        return next_elements
    else:  # Варіант коли елементи секвенції мають різницю що змінюється
        second_diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        while count < 3:
            elem1, elem2 = elem2, elem2 + diffs[-1] + second_diffs[-1]
            diffs.append(elem2 - elem1)
            next_elements.append(elem2)
            count += 1
        return next_elements


if __name__ == '__main__':
    assert next_sequence_elements([12, 14, 16, 18, 20]) == [22, 24, 26]
    assert next_sequence_elements([15, 32, 57, 90, 131, 180]) == [237, 302, 375]
    assert next_sequence_elements([1, 1, 1, 1, 1]) == [1, 1, 1]
