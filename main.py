# Execute your methods here.
from src import *



def filter_males(filter_list):
    new_list = list(filter(lambda m: m['sex'] == 'male', filter_list))
    return new_list

def calc_BMI():


def main():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    #sort_people(people_list, 'weight', 'desc')
    #print(sort_people)
    
    #new_list = filter_males(people_list)
    #print(new_list)
    
    
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    

if __name__ == '__main__':
    main()
