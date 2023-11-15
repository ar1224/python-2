def main():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    new_people_list = list(map(calc_bmi, people_list))
    print(new_people_list)

def calc_bmi(people_list):
    new_dict = {
        'id':people_list['id'],
        'name': people_list['name'],
        'weight_kg':people_list['weight_kg'],
        'height_meters': people_list['height_meters'],
        'bmi': round(people_list['weight_kg'] / people_list['height_meters'] ** 2, 1)
    }
    return new_dict


if __name__ == '__main__':
    main()