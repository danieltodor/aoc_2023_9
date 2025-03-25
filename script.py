""" Solution for part one """

from itertools import pairwise


def get_values():
    """ Read values from file and convert them to integers """
    result = []
    with open('values.txt', encoding='utf-8') as values:
        for line in values.readlines():
            items = line.split()
            values = [int(item) for item in items]
            result.append(values)
    return result


def process_history(history):
    """ Calculate the next value for a history """
    def get_difference(part):
        result = []
        for left, right in pairwise(part):
            result.append(right - left)
        return result

    def all_zero(part):
        for item in part:
            if item != 0:
                return False
        return True

    def extrapolate():
        index = len(result) - 1
        for current in reversed(result):
            previous = result[index + 1:]
            current_last_value = current[-1]
            previous_last_value = previous[0][-1] if previous else 0
            current.append(current_last_value + previous_last_value)
            index -= 1

    result = [history]
    while not all_zero(result[-1]):
        result.append(get_difference(result[-1]))
    extrapolate()
    return result


def get_total(processed_histories):
    """ Sums all the next values from the history differences """
    values = []
    for items in processed_histories:
        next_value = items[0][-1]
        values.append(next_value)
    return sum(values)


def main():
    histories = get_values()
    processed = []
    for history in histories:
        processed.append(process_history(history))
    print(get_total(processed))


if __name__ == '__main__':
    main()
