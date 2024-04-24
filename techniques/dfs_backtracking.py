def dfs(nums, index, path, result):
    # Append the current subset to the result
    result.append(path[:])

    for i in range(index, len(nums)):
        # Include the current element
        path.append(nums[i])

        # Recursive call
        dfs(nums, i + 1, path, result)

        # Backtrack, remove the element before the next iteration
        path.pop()

    return result


def subsets(nums):
    return dfs(nums, 0, [], [])


# Example usage
nums = [1, 2, 3]
print(subsets(nums))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
