def main():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    
    new_list = filter_males(people_list)
    print(new_list)


def filter_males(filter_list):
    new_list = list(filter(lambda m: m['sex'] == 'male', filter_list))
    return new_list



if __name__ == '__main__':
    main()
