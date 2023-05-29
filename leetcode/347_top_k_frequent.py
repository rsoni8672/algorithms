def get_freq_map(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    return freq_map

def get_frequency_wise_map(freq_map):
    temp_map = {}
    for freq in freq_map:
        val = freq_map[freq]

        temp = temp_map.get(val, [])
        temp.append(freq)
        temp_map[val] = temp
    return temp_map

def top_k_frequent(nums, k):

    freq_map = get_freq_map(nums)
    temp_map = get_frequency_wise_map(freq_map)
    frequencies = sorted(temp_map.keys(), reverse=True)[:k]
    output = []
    index = 0
    while index < k:
        output.extend(temp_map[frequencies[0]])
        index += len(temp_map[frequencies[0]])
        if len(output) > k:
            return output[:k]
        frequencies = frequencies[1:]
    print(output)
    return output

if __name__ == '__main__':
    print("output - ", top_k_frequent([1,1,1,2,2,3], 2))