names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    for i in range(len(names)):
        print('{}. {}{}{}'.format(i + 1, names[i], ' ' * (11 - len(names[i])), countries[i]))

enumerate_names_countries()