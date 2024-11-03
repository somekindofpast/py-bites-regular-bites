from string import ascii_lowercase

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)

def binary_search(sequence, target):
    if sequence is None or target is None or len(sequence) == 0:
        return None
    sequence.sort()
    return recur(sequence, 0, len(sequence), target)

def recur(sequence, start, end, target):
    mid = int((start + end) / 2)
    if sequence[mid] == target:
        return mid
    elif sequence[mid] < target:
        if mid == end:
            return None
        return recur(sequence, mid + 1, end, target)
    elif target < sequence[mid]:
        if mid == start:
            return None
        return recur(sequence, start, mid - 1, target)

print(binary_search(PRIMES, 2))
print(binary_search(PRIMES, 59))
print(binary_search(PRIMES, 5))
print(binary_search(PRIMES, 61))
print(binary_search(PRIMES, 18))
print(binary_search(ALPHABET, 'u'))
print(binary_search(ALPHABET, 'a'))
print(binary_search(ALPHABET, 'z'))