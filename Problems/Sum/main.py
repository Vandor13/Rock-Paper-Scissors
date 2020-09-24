# read sums.txt
my_file = open("sums.txt", mode="r")
lines = my_file.readlines()
for line in lines:
    numbers = [int(x) for x in line.split()]
    sum_num = 0
    for number in numbers:
        sum_num += number
    print(sum_num)
my_file.close()