import csv

SCHOOL_YEAR = 2020

def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    class_assignments = []
    for row in data:
        student_id = int(row[0])
        for i in range(2, len(row)):
            if row[i] != "":
                class_assignments.append(f"{row[i].split(' - ')[0]},{SCHOOL_YEAR},{student_id}")
    return class_assignments