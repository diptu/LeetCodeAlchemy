def compute_lps_array(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for the given pattern.
    """
    length = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Searches for the pattern within the text using the KMP algorithm.
    Prints the indices where the pattern is found.
    """
    N = len(text)
    M = len(pattern)

    lps = compute_lps_array(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            print(f"Found pattern at index {i - j}")
            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


# --- Example Usage ---
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"Searching for '{pattern}' in '{text}':")
kmp_search(text, pattern)
