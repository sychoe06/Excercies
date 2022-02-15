def check_factor(num_list_, factor):
    multiples_ = []
    for i in num_list_:
        if i % factor == 0:
            multiples_.append(i)
    return multiples_


# main routine
num_list = [1, 4, 6, 7, 15, 22, 35]
print(check_factor(num_list, 5))
print(check_factor(num_list, 2))
