path = ["1->2"]
print("path before", path)

new_path = path + [str(3)]
print("path after", path)
print("new_path", new_path)

new_path2 = [*path, str(3)]
print("path after after", path)
print("new_path2", new_path2)
