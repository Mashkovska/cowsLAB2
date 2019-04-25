from math import floor

# перевіряє чи можемо ми розмістити так, щоб мінімальна  відстань між ними
# була більшою за змінну distance
def can_find_lower_value(stalls, cows_number, distance):
    # кількість корів яку потрібно розмістити по стайнях
    cows_number -= 1
    # номер стайні для теперішньої корови

    current_stall = stalls[0]

    for i in range(1, len(stalls)):
        # номер стайні для наступної корови
        next_stall = stalls[i]
        if next_stall - current_stall >= distance:
            cows_number -= 1
            if cows_number == 0:
                return True
            current_stall = next_stall
    return False


def find_min_distance(stalls, cows_number):
    stalls.sort()

    begin_stall = stalls[0]
    end_stall = stalls[-1]

    # Обрахунок максимально можливої дистанції
    # Значення distance кожну ітерацію або збільшується, або зменшується, щоб знайти правильне значення
    while end_stall - begin_stall > 1:
        distance = begin_stall + floor((end_stall - begin_stall) / 2)

        # якщо ми не можемо розмістити корів так, щоб мінімальна  відстань між ними
        # була більшою за змінну distance
        if can_find_lower_value(stalls, cows_number, distance):
            # відстань збішуємо
            begin_stall = distance
        else:
            # відстань зменшуємо
            end_stall = distance
    print(begin_stall)


#main function
n, c = map(int, input().split(' '))
stack = []

for j in range(n):
    stack.append(int(input()))

find_min_distance(stack, c)
