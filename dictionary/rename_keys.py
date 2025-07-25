from typing import Dict, Any


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    res = {}
    for item in data.items():
        key = item[0] if not isinstance(item[0], str) else item[0].lstrip('@')
        if isinstance(item[1], list):
            value = [elem if not isinstance(elem, dict) else rename_keys(elem) for elem in item[1]]
        elif isinstance(item[1], dict):
            value = rename_keys(item[1])
        else:
            value = item[1]
        res[key] = value
    return res


if __name__ == '__main__':
    from datetime import datetime
    input_dict = {'@contentUrl': 'contentUrl',
                         '@createdAt': datetime.strptime('2020-06-11T09:08:13Z', '%Y-%m-%dT%H:%M:%SZ'),
                          '@defaultViewId': 'defaultViewId',
                          '@encryptExtracts': False,
                          '@id': 'id',
                          '@name': 'Login',
                          '@showTabs': True,
                          '@size': 1,
                          '@updatedAt': datetime.strptime('2020-07-20T06:41:34Z', '%Y-%m-%dT%H:%M:%SZ'),
                          '@webpageUrl': 'webpageUrl',
                          'dataAccelerationConfig': {'@accelerationEnabled': False},
                          'owner': {'@id': 'id', '@name': 'name'},
                          'project': {'@id': 'id', '@name': 'name'},
                          'tags': {'tag': {'@label': 'label'}},
                          'views': {'view': [{'@contentUrl': 'contentUrl',
                                             '@createdAt': '2020-06-11T09:08:13Z',
                                              '@id': 'id',
                                              '@name': 'name',
                                              '@updatedAt': '2020-07-20T06:41:34Z',
                                              '@viewUrlName': 'Sheet1',
                                              'tags': {'tag': {'@label': 'label'}}},
                                             {'@contentUrl': 'contentUrl',
                                              '@createdAt': '2020-06-11T09:08:13Z',
                                              '@id': 'id',
                                              '@name': 'name',
                                              '@updatedAt': 'updatedAt',
                                              '@viewUrlName': 'viewUrlName',
                                              'tags': {'tag': {'@label': 'label'}}}]}}
    print(input_dict)
    print(rename_keys(input_dict))