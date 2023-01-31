dict_1 = {"alpha": 1, "bravo": 2, "charlie": 3, "delta": 4}
dict_2 = {"alpha": 1, "bravo": 2, "charlie": 3, "delta": 3}

def my_func(test_dict, n):
    sorted_items_list = sorted(test_dict.items(), key=lambda x:x[1], reverse=True) # sorting values in descending order
    req_item = sorted_items_list[n - 1] # finding nth highest item
    req_key = ''
    for key, value in test_dict.items():
        if value == req_item[1]:
            if req_key == '' or key < req_key: # if multiple keys has same nth highest value, get the key that is alphabetically lowest
                req_key = key
    return req_key


assert my_func(dict_1, 1) == 'delta'
assert my_func(dict_1, 3) == 'bravo'
assert my_func(dict_2, 1) == 'charlie'
assert my_func(dict_2, 2) == 'charlie'
print('passed')