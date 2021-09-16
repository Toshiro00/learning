data = ['Hello World\n', 'I\'m Omer\n', 'from Medium']

file = open('new_file.txt', 'w')
file.writelines(data)
file.close()

my_file = open('new_file.txt', 'r')
lines = my_file.readlines()

for line in lines:
    print(line)
