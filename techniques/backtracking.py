def dfs(nums, path, res, index):
    res.append(path[:])  # Append the current subset to the results
    for i in range(index, len(nums)):
        path.append(nums[i])  # Include the current element
        dfs(nums, path, res, i + 1)  # Recurse
        path.pop()  # Backtrack, remove the element before the next iteration


def subsets(nums):
    res = []
    dfs(nums, [], res, 0)
    return res


# Example usage
nums = [1, 2, 3]
print(subsets(nums))
