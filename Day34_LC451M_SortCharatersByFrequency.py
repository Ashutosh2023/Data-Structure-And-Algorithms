from collections import defaultdict
def frequencySort(s: str) -> str:
    result = ""
    hashmap = defaultdict(int)
    for x in s:
        hashmap[x] += 1
    sorted_items_desc = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items_desc:
        result += key*value
    return result

s = "tree"
print(frequencySort(s))