class Employee:
    def __init__(self, name, surname, pin, work_time, pay=None):
        self.name = name
        self.surname = surname
        self.pin = pin
        self.pay = pay
        self.work_time = work_time
        self.effciency = (self.work_time * 100) / 40

    def show_info(self):
        return f'---------------------- \n' \
               f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Персональный номер: {self.pin}\n' \
               f'ЗП: {self.pay}\n' \
               f'Рабочие часы {self.work_time}\n' \
               f'Эффективность  {self.effciency} %\n' \
               f'----------------------'


class Addtional_secteraty(Employee):
    def __init__(self, name, surname, pin, work_time, ):
        self.name = name
        self.surname = surname
        self.pin = pin
        self.work_time = work_time
        self.effciency = (self.work_time * 100) / 40
        self.result = work_time * 100

    def show_info(self):
        return f'---------------------- \n' \
               f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Персональный номер: {self.pin}\n' \
               f'ЗП: {self.result}\n' \
               f'Рабочие часы {self.work_time}\n' \
               f'Эффективность  {self.effciency} %\n' \
               f'----------------------'


class Salesman(Employee):
    def __init__(self, name, surname, pin, work_time, pay, sales):
        self.name = name
        self.surname = surname
        self.pin = pin
        self.pay = pay
        self.work_time = work_time
        self.sales = sales
        self.effciency = (self.work_time * 100) / 40
        self.result = self.pay + self.sales * 50

    def show_info(self):
        return f'---------------------- \n' \
               f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Персональный номер: {self.pin}\n' \
               f'ЗП: {self.result}\n' \
               f'Рабочие часы {self.work_time}\n' \
               f'Эффективность  {self.effciency} %\n' \
               f'----------------------'


class Manager(Employee):
    pass


class Secretary(Employee):
    pass


class Shop_worker(Employee):
    def __init__(self, name, surname, pin, work_time, ):
        self.name = name
        self.surname = surname
        self.pin = pin
        self.work_time = work_time
        self.effciency = (self.work_time * 100) / 40
        self.result = work_time * 100

    def show_info(self):
        return f'---------------------- \n' \
               f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Персональный номер: {self.pin}\n' \
               f'ЗП: {self.result}\n' \
               f'Рабочие часы {self.work_time}\n' \
               f'Эффективность  {self.effciency} %\n' \
               f'----------------------'


manager = Manager('Бакыт', 'Канатакулов', 1, 18, 45000)
secretary = Secretary('Алымкул', "Тилекбаев", 2, 38, 2000)
salesman = Salesman('Айпери', 'Шалымбекова', 3, 38, 20000, 20)
worker1 = Shop_worker('Бакыт', "Рустамов", 4, 25)
worker2 = Shop_worker('Алтынай', "Ширинбаева", 5, 40)
add_secratary = Addtional_secteraty('Жанар', 'Рыскулов', 6, 33)

for worker in (manager, secretary, worker2, worker1, salesman,add_secratary):
    print(worker.show_info())

print(f'Сумма всех выплат {manager.pay + secretary.pay + worker2.result + worker1.result + salesman.result + add_secratary.result}')

workers_effiency = {}

for worker in (manager, secretary, worker2, worker1, salesman,add_secratary):
    workers_effiency.update({worker.surname: worker.effciency})

sort_effiency = sorted(workers_effiency.items(), key=lambda x: x[1])

min_effiency = sort_effiency[0]
max_effiency = sort_effiency[-1]
print(f'Самый продуктивный работник {max_effiency}, наименее продуктивный {min_effiency}')
