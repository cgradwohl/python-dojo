def length_of_longest_substring(s):
    char_map = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Test cases
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("candidate"))  # Output: 5
