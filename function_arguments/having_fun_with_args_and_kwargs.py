def get_profile(name, age, *sports, **awards):
    if not name or not age:
        raise TypeError
    if not isinstance(age, int):
        raise ValueError
    if not sports and not awards:
        return {'name': name, 'age': age}
    if sports and 5 < len(sports):
        raise ValueError
    if sports and not awards:
        return {'name': name, 'age': age, 'sports': sorted(sports)}
    if not sports and awards:
        return {'name': name, 'age': age, 'awards': awards}
    return {'name': name, 'age': age, 'sports': sorted(sports), 'awards': awards}