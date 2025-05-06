def flatten(list_of_lists):
    res = []
    for elem in list_of_lists:
        if isinstance(elem, list) or isinstance(elem, tuple):
            res.extend(flatten(elem))
        else:
            res.append(elem)
    return res