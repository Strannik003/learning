# Sorting ex
# input: 4 2 6 1
# output: 1 2 4 6


input = [4, 2, 6, 1, 10, 5, -1]
output = []
if __name__ == "__main__":
    for i in range(len(input)):
        min_index=i
        for j in range(i,len(input)):
            if input[j] < input[min_index]:
                min_index = j
        input[i], input[min_index]=input[min_index], input[i]
    print(input)