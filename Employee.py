from main import Person
class Employee(Person):
    def __init__(self,name,money,healhRate,id,car,email,salary=None,distanceToWork=None):
        super().__init__(name,money,healhRate)
        self.id=id
        self.car=car
        self.email=email
        self.salary=salary
        self.distanceToWork=distanceToWork

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, a):
        if (a < 1000):
            raise ValueError("Sorry you salary not valid")
        self._salary = a

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("This doesn't look like an email address.")
        self._email = value


    def work(self,hour):

       if hour == 8:
          Person.mood='happy'
       elif hour > 8:
          Person.mood='tired'
       elif hour < 8:
          Person.mood='lazy'

    def drive(self):
        pass
    def refuel(self):
        pass

    def send_mail(self,t_m,f_m,subject,receiver_name):
        line = '\n'.join(['from: '+f_m,'to: '+t_m,'   ','to '+receiver_name,subject ])
        file =open("email.txt","a")
        line = line+"\n"
        file.write(line)
        file.close()
m = Employee("ali", 1000, 100,10,'BM', 'ali@mail', 1000, 100)
m.send_mail("amira","mohamed","hello","mohamed")
m.work(5)
print(m.mood)
print(m.salary)
print (m.email)


