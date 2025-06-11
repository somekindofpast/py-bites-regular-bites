def extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """
    res = []
    nested = []
    ip = None
    mask = None
    for i in range(len(data)):
        if isinstance(data[i], list):
            if 0 < i and len(data[i]) == 1 and isinstance(data[i][0], str):
                val = str(data[i][0]).strip('"')
                if data[i-1] == "ip" and len(val.split('.')) == 4:
                    parts = val.split('.')
                    for j in range(len(parts)):
                        if not parts[j].isnumeric():
                            break
                        if j == len(parts) - 1:
                            ip = val
                elif data[i-1] == "mask" and val.isnumeric():
                    mask = val
            else:
                nested.extend(extract_ipv4(data[i]))
    if ip and mask:
        res.append((ip, mask))
    res.extend(nested)
    return res


if __name__ == '__main__':
    # [] - empty_list
    print(extract_ipv4([]))
    # [] - list_no_match
    print(extract_ipv4(['ip']))
    # [] - nested_list_no_match
    print(extract_ipv4([['ip', 'mask']]))
    # [] - nested_list_no_ip
    print(extract_ipv4([['TEST', ['ip', [None], 'mask', ['24'], 'type', ['ip_mask']], 'id']]))
    # [] - nested_list_not_an_ip
    print(extract_ipv4([['TEST', ['ip', ['"not.an.ip.address"'], 'mask', ['24'], 'type', ['ip_mask']], 'id']]))
    # [] - nested_list_no_mask
    print(extract_ipv4([['TEST', ['ip', ['"1.1.1.0"'], 'mask', [None], 'type', ['ip_mask']], 'id']]))
    # [('172.16.0.0', '12')]
    print(extract_ipv4(['ip', ['"172.16.0.0"'], 'mask', ['12'], 'type', ['ip_mask']]))
    # [('192.168.1.0', '24'), ('10.0.0.0', '8')]
    print(extract_ipv4(['TEST', 'parent', [], 'uuid', '"khk-yyas4h-323223-wewe-343er-3434-www"', 'display_name', '"services"', 'IPV4', [['ip', ['"192.168.1.0"'], 'mask', ['24'], 'type', ['ip_mask']], ['ip', ['"10.0.0.0"'], 'mask', ['8'], 'type', ['ip_mask']]]]))
    # [('1.1.1.0', '20'), ('2.2.2.2', '32')]
    print(extract_ipv4([['TEST', ['parent', [], 'uuid', ['"khk-yyas4h-323223-wewe-343er-3434-www"'], 'display_name', ['"services"'], 'IPV4', [[['ip', ['"1.1.1.0"'], 'mask', ['20'], 'type', ['ip_mask']], ['ip', ['"2.2.2.2"'], 'mask', ['32'], 'type', ['ip_mask']]]]]]]))