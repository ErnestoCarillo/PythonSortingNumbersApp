
def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers[-n:]

nums = [506,1024,2137,5,123,53,555]

largest  = get_largest_numbers(nums, 2)
print(nums)