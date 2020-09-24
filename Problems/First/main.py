# read test_file.txt
my_file = open("test_file.txt", mode="r", encoding="utf-16")
lines = my_file.readlines()
print(lines[0])
my_file.close()