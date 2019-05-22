'''__call__方法和可调用对象'''
class Student():
    salary = 30000
    def __call__(self, *args, **kwargs):
        print("发工资了")
        yearSalary = Student.salary*12
        daySalary = Student.salary//22.5
        hourSalary = daySalary//8
        return dict(yearSalary =yearSalary,daySalary = daySalary,hourSalary = hourSalary)


stu1 = Student()
print(stu1())