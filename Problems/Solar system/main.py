# create the planets.txt
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
my_file = open("planets.txt", mode="w", encoding="utf-8")
my_file.writelines([planet + "\n" for planet in planets])
my_file.close()