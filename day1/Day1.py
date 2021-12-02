file = open("data.txt")
data = [int(i) for i in file.readlines()]


def part1(): 
    #count how many bigger
    bigger = 0 

    for i in range(len(data)-1): 
        n1 = data[i]
        n2 = data[i+1]

        if n1 < n2:
            bigger += 1
    return bigger

def part2(): 
    #count how many bigger
    bigger = 0 

    for i in range(len(data)-3): 
        sum1 = sum(data[i:i+3])
        sum2 = sum(data[i+1:i+4])

        if sum1 < sum2:
            bigger += 1
    return bigger


print(part2())

