def average(array):
    # your code goes here
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)