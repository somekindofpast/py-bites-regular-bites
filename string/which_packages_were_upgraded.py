def changed_dependencies(old_reqs: str, new_reqs: str) -> list[str]:
    """Compare old vs new requirement multiline strings
    and return a list of dependencies that have been upgraded
    (have a newer version)
    """
    old_req_dict = {}
    new_req_dict = {}
    for req in old_reqs.splitlines():
        if req.strip() == '':
            continue
        old_req_dict[req.split("==")[0].strip()] = req.split("==")[1].split('.')
    for req in new_reqs.splitlines():
        if req.strip() == '':
            continue
        new_req_dict[req.split("==")[0].strip()] = req.split("==")[1].split('.')

    res = []
    for key, old_values in old_req_dict.items():
        new_values = new_req_dict[key]
        if not new_values:
            continue
        for i in range(len(old_values)):
            if len(new_values) <= i:
                break
            old_num = int(old_values[i])
            new_num = int(new_values[i])
            if old_num < new_num:
                res.append(key)
                break
            if new_num < old_num:
                break
    return sorted(res)


if __name__ == '__main__':
    other_old_reqs = """
    twilio==6.23.1
    urllib3==1.21.1
    Werkzeug==0.12.1
    WTForms==1.19.0
    """
    other_new_reqs = """
    twilio==6.3.0
    urllib3==1.21.1
    Werkzeug==0.14.1
    WTForms==2.1
    """
    print(changed_dependencies(other_old_reqs, other_new_reqs))