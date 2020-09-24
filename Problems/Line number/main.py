# read sample.txt and print the number of lines
my_file = open("sample.txt", mode="r")
lines = my_file.readlines()
print(len(lines))
my_file.close()