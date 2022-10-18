class Employee(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_salary(self):
        return 0


class Manager(Employee):

    def __init__(self, name, hour):
        # 继承父类，括号中为父类的形参
        super().__init__(name)
        self.working_hour = hour

    def get_salary(self):
        return 15000


class Programmer(Employee):

    def __init__(self, name, hour):
        super(Programmer, self).__init__(name)
        self.working_hour = hour

    def get_salary(self):
        return 60 * self.working_hour


emps = [
    {'姓名': '刘备', '职位': 'Manager', '工作时间': 160},
    {'姓名': '张飞', '职位': 'Programmer', '工作时间': 200},
    {'姓名': '赵云', '职位': 'Programmer', '工作时间': 180}
]


def classify(emps):
    for i in emps:
        if i['职位'] == 'Programmer':
            # 传参实例化
            a = Programmer(i['姓名'], i['工作时间'])
            # 调用方法
            print(f'姓名：{a.get_name()}，薪资：{a.get_salary()}')
        else:
            b = Manager(i['姓名'], i['工作时间'])
            print(f'姓名：{b.get_name()}，薪资：{b.get_salary()}')


classify(emps)
