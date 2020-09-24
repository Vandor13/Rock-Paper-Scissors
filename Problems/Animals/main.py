# read animals.txt
# and write animals_new.txt
my_file = open("animals.txt", mode="r")
animal_text = my_file.read()
my_file.close()
animals = animal_text.split("\n")
new_file = open("animals_new.txt", mode="w")
new_file.writelines([animal + " " for animal in animals])
new_file.close()
