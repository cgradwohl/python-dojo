def get_words(n: int):
    def dfs(idx, path):
        if idx == n:
            # append a reference to the 'path' list
            # note that 'path' is modified at the end of each for loop, and ultimately cleared to empty
            # result.append(path)

            # quick way to make a new list
            # result.append(list(path))

            result.append("".join(path))
            return None
        for char in ["a", "b"]:
            path.append(char)
            dfs(idx + 1, path)
            path.pop()
    result = []
    dfs(0, [])
    return result


print(get_words(2))
