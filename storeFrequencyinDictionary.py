data = [1, 2, 2, 3, 1, 2]
freq = {}

for x in data:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)  # {1: 2, 2: 3, 3: 1}
# this uses just if else to check and the values just itretate from the dict {} that's it


data = [1, 2, 2, 3, 1, 2]
freq = {}

for x in data:
    freq[x] = freq.get(x, 0) + 1

print(freq)
# check the list/array and add's the val and freq into the dict {}