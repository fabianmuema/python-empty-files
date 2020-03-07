f = input("Input file name: ")

file = open(f, "r+")

file.truncate(0)
