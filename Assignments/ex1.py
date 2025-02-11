def main():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    sort_people(people_list, 'weight', 'desc')
    print(people_list)

def sort_people(people_sort, type, sort):
    people_sort.sort(key=lambda p: p[type])
    if sort == 'desc':
        people_sort.sort(key=lambda p: p[type], reverse = True)
    return people_sort

if __name__ == '__main__':
    main()
