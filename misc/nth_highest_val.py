dict_1 = {"alpha": 1, "bravo": 2, "charlie": 3, "delta": 4}
dict_2 = {"alpha": 1, "bravo": 2, "charlie": 3, "delta": 3, "claim":3, 'zealous':3}

def my_func(test_dict, n):
    # sorting values in descending order if there are duplicate values then sort based on keys in alphabetically
    sorted_items_list = sorted(test_dict.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_items_list)
    return sorted_items_list[n-1][0]

assert my_func(dict_1, 1) == 'delta'
assert my_func(dict_1, 3) == 'bravo'
assert my_func(dict_2, 1) == 'charlie'
assert my_func(dict_2, 2) == 'claim'
print('passed')

# External Reference Used:
# https://stackoverflow.com/questions/5212870/sorting-a-python-list-by-two-fields


# req_item = sorted_items_list[n - 1] # finding nth highest item
# req_key = ''
# for key, value in test_dict.items():
#     if value == req_item[1]:
#         if req_key == '' or key < req_key: # if multiple keys has same nth highest value, get the key that is
#         alphabetically lowest
#             req_key = key
# return req_key

