def main():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    print(get_people(people_list))

def get_people(people_list):
    new_list = [p['name'] for p in people_list if p['age'] > 14]
    return new_list

if __name__ == '__main__':
    main()
