def filter_duplicates(data):
    seen = set() #creation of an empty set to stock duplicate numbers
    result = []  #creation fo an empty list to stock the unique numbers
    for item in data:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
#exemple
data = [1, 2, 3, 2, 2,2,2,2]
filtered_data = filter_duplicates(data)
print(filtered_data)
