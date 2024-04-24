# creates a new array
result = ["4"] + ["7"]
print(result)  # ['4', '7']

path = ['4']
# concat operator does not mutate the array in place
print(path + [str('6')])  # ['4', '6']

# mutates the 'path' array in place
path.append('7')
print(path)  # ['4', '7']
