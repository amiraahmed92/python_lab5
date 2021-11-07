class Person:
    mood=('happy','tired','lazy')
    def __init__(self,name,money,healthRate):
        self.name = name
        self.money = money
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, b):
        if b > 100:
            raise ValueError("Sorry you healthRate  not valid")
        elif b < 0:
            raise ValueError("Sorry you healthRate  not valid")
        self._healthRate =b

    def sleep(self,hour):
        if hour==7:
            Person.mood=Person.mood[0]
            #Person.mood='happy'
        elif hour<7:
            Person.mood=Person.mood[1]
            # Person.mood='tired'
        elif hour>7:
            Person.mood = Person.mood[2]
            # Person.mood='lazy'


    def eat(self,meals):
        if meals==3:
            self.healthRate=100
        elif meals==2:
            self.healthRate=75
        elif meals==1:
            self.healthRate=50

    def buy(self,no_item):
        l=list(range(0,no_item))
        for i in l :
            print(i)
            self.money=self.money-10
print (Person.mood[0])
e=Person("amira",100,100)
print(e.healthRate)
e.buy(2)
print(e.money)
e.sleep(7)
print(e.mood)
e.eat(3)
print(e.healthRate)









