def print_integers_in_range(start, stop):
    for i in range(start, stop + 1):
        print(i)

def print_squares_to_number(number):
    if number < 1:
        print("ERROR: number must be at least 1")
    else:
        for i in range(1, number + 1):
            print(f"{i} * {i} = {i**2}")

def set_lowercase(strings):
    for i in range(len(strings)):
        strings[i] = strings[i].lower()

items = [0.0, 3.2, 7.6, 5.9, 1.4]
for (i, num) in enumerate(items):
    items[i] = round(num)


def my_enumerate(items):
    result = []
    index = 0
    for item in items:
        result.append((index, item))
        index += 1
    return result

def countdown321(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [3, 2, 1]:
            return True
    return False

def print_points(point_tuples):
    for index, (x, y) in enumerate(point_tuples):
        print(f"Point {index}: x = {x}, y = {y}")

def get_column(game, col_num):
    return [game[0][col_num], game[1][col_num], game[2][col_num]]

def diagonals(game):
    # Top-left to bottom-right diagonal
    diag1 = [game[i][i] for i in range(3)]
    # Top-right to bottom-left diagonal
    diag2 = [game[i][2-i] for i in range(3)]
    return (diag1, diag2)

def row_sums(square):
    sums = []
    for row in square:
        row_sum = 0
        for num in row:
            row_sum += num
        sums.append(row_sum)
    return sums

def column_sums(square):
    return [sum(column) for column in zip(*square)]

def print_daily_totals(rainfalls):
    for day, daily_rain in enumerate(rainfalls):
        total = 0
        for rain in daily_rain:
            total += rain
        print(f"Day {day} total: {total}")

rain_readings = [
    0.0, 0.0, 3.4, 33.8, 3.8, 0.0, 0.0, 0.0, 
    0.0, 0.0, 25.2, 12.2, 5.4, 0.4, 0.0, 0.0, 
    0.2, 0.0, 0.0, 1.6, 5.6, 25.8, 0.2, 0.0, 
        .2, 0.4, 0.0, 0.2, 0.0, 15.6, 0.0, 0.0
]
        
total = 0
for i in range(0, len(rain_readings), 2):
    total += rain_readings[i]
        
def n_halves(n):
    count = int()
    while n > 1:
        n /= 2
        count += 1
    return count

def print_cumulative_elements(elements):
    i = 0
    cumulative = ''
    while i < len(elements):
        cumulative += elements[i] + ' '
        print(cumulative.strip())
        i += 1
        

def print_names2(names_list):
    i = 0
    while i < len(names_list):
        name_str = ' '.join(names_list[i])
        print(name_str)
        i += 1

def print_names2(names_list):
    i = 0
    while i < len(names_list):
        name_str = ' '.join(names_list[i])
        print(name_str)
        i += 1

def guess_my_number(target_number, lower_bound, upper_bound):
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    guess = int(input("Make a guess: "))
    while guess != target_number:
        print("That is not my number. Enter another.")
        guess = int(input("Make a guess: "))
    print("Congratulations! You guessed my number!")


def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Calculates the number of rushes Herbert needs to reach the top of the slope."""
    current_height = 0
    num_rushes = 0

    while current_height < slope_height:
        num_rushes += 1
        current_height += rush_height_gain  # Herbert rushes up the slope

        # Check if Herbert has reached or exceeded the slope height
        if current_height >= slope_height:
            break  # Herbert has reached the top, no need to slide back

        current_height -= back_sliding  # Slope settles, Herbert slides back

    return num_rushes

def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Calculates the number of rushes Herbert needs to reach the top of the slope,
       accounting for the 5% reduction in height gain and back sliding on each rush."""
    current_height = 0
    num_rushes = 0
    rush_factor = 0.95

    while current_height < slope_height:
        num_rushes += 1
        current_height += rush_height_gain  # Herbert rushes up the slope

        # Check if Herbert has reached or exceeded the slope height
        if current_height >= slope_height:
            break  # Herbert has reached the top, no need to slide back

        current_height -= back_sliding  # Slope settles, Herbert slides back

        # Apply the 5% reduction for the next rush
        rush_height_gain *= rush_factor
        back_sliding *= rush_factor

    return num_rushes

# Example usage:
ans = num_rushes(100, 15, 7)
print(ans)  # Output: 19

ans = num_rushes(10, 10, 9)
print(ans)  # Output: 1

