# используется для сортировки
from operator import itemgetter

class Computer:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class HDD:

    def __init__(self, id, name,size, id_of_computer):
        self.id = id
        self.name = name
        self.size = size
        self.comp_id = id_of_computer

class HDD_Computer:
    
    def __init__(self, id_of_computer, id_of_HDD):
        self.id_of_computer = id_of_computer
        self.id_of_HDD = id_of_HDD

# Отделы


Computer = [
    Computer(1, 'Первый компьтер'),
    Computer(2, 'Второй компьютер'),
    Computer(3, 'Третий компьютер'),


    Computer(33, 'Мощный компьютер'),
    Computer(11, 'Главный компьютер'),
    Computer(22, 'Удаленный компьютер')
]

# Сотрудники
HDD = [
    HDD(1,'Amsung',  1000, 1),
    HDD(2,'ASEAGATE', 2500, 3),
    HDD(3,'TOSHIBA', 500, 3),
    HDD(4,'HITACHI', 5000, 2),
    HDD(5,'WESTERN DIGITAL', 3000, 3)
]

HDD_Computer = [
    HDD_Computer(1,1),
    HDD_Computer(2,2),
    HDD_Computer(3,3),
    HDD_Computer(3,4),
    HDD_Computer(5,5),

    

    HDD_Computer(11,1),
    HDD_Computer(22,2),
    HDD_Computer(33,3),
    HDD_Computer(33,4),
    HDD_Computer(33,5)
]

def main():
    

    
    one_to_many = [( b.name, b.size, a.name) 
        for a in Computer 
        for b in HDD 
        if b.comp_id == a.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, d.id_of_computer, d.id_of_HDD) 
        for c in Computer 
        for d in HDD_Computer 
        if c.id == d.id_of_computer]
    
    many_to_many = [(b.name, b.size, name_of_computer) 
        for name_of_computer, id_of_computer, id_of_HDD in many_to_many_temp
        for b in HDD if b.id== id_of_HDD]

    print('Задание В1')
    first_res = {} 

    for l in HDD:
        if 'A' == l.name[0]:
            hdd = list((filter(lambda i: i[0] == l.name, one_to_many)))
            l_comp_names = [f[2] for f in hdd]
            first_res[l.name] = l_comp_names

    print(first_res)
    
    
    
    print('\nЗадание B2')
    second_res_unsort = []
    
    for d in Computer:
        
        hdd = list(filter(lambda i: i[2]==d.name, one_to_many))
         
        if len(hdd) > 0:
            second_res_unsort.append((d.name, min([a[1] for a in hdd])))
    second_res = sorted(second_res_unsort, key=itemgetter(1))
    print(second_res)

    print('\nЗадание B3')
    third_res = sorted(many_to_many, key=itemgetter(0))
    print(third_res)


if __name__ == '__main__':
    main()
