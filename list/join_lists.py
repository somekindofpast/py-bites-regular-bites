from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) == 0:
        return None
    result_lst = []
    for lst in lst_of_lst:
        if 0 < len(result_lst):
            result_lst.append(sep)
        result_lst.extend(lst)
    return result_lst