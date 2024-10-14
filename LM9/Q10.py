def get_name(name_dict, id_num):
    """Module Question 10"""
    return name_dict.get(id_num, None)

test_dictionary = {11:'Fred', 2001:'Agnes'}
ans = get_name(test_dictionary, 10)
print(ans)