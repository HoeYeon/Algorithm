def solution(name_list):
    name_dict = {}
    for name in name_list:
        tmp = "".join(sorted(list(set(list(name_list)))))
        if tmp in name_dict:
            return True
        name_dict[tmp] = 1
    return False
