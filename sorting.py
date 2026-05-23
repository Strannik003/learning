# Sorting ex
# input: 4 2 6 1
# output: 1 2 4 6


input = [4, 2, 6, 1]
output = []
if __name__ == "__main__":
    while input != []:
        minimal_index=input.index(min(input))
        x=input.pop(minimal_index)
        output.append(x)
        
    print(output)




  
