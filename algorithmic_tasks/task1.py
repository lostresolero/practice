numbers= [2,7,11,15]
target = 9

def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    number_index = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in number_index:
            return number_index[complement], index
        number_index[number] = index
    raise ValueError("No two sum solution")
        