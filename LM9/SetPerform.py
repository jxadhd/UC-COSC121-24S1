from time import perf_counter

def count_occurrences(start, end, collection):
    """Count how many of the numbers from start to end are in the given
       collection. Print the time taken.
    """
    start_time = perf_counter()
    count = 0
    for i in range(start, end + 1):
        if i in collection:
            count += 1

    time_taken = perf_counter() - start_time
    print(count, 'found')
    print('Took {:.3} secs'.format(time_taken))
    return time_taken

def main():
    """Compare times to search a list and a set"""

    # A list of numbers from 9000 to 40000
    numbers = list(range(9000, 40000))

    print("Searching a list")
    list_time = count_occurrences(0, 10000, numbers)

    # Now do it again with a set
    print("Searching a set")
    numbers_set = set(numbers)
    set_time = count_occurrences(0, 10000, numbers_set)
    factor = list_time / set_time
    print("Sets were faster by a factor of {:.1f}".format(factor))

main()
