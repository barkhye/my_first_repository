""" #cls, self

class Myclass :
    count = 0
    
    def __init__(self,num) :
        self.count = num
        
    @classmethod
    def clsMethod(cls):
        cls.count += 1
        print(f"cls count = {cls.count}")
        
    def instMethod(self):
        self.count += 1
        print(f"instance = {self.count}")
        
MyClass.clsMethod()

obj = MyClass(10)
obj.instMethod()
print(obj.count)

print(Myclass.count)
print(Myclass.count) """


#
""" 
class Champion:
    1v = 1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.658
    
    def __init__(self, chmpNam, speed):
        self.hp = 100
        self.chmpNam = chmpNam
        self.level = 1
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()
        
    def setMovSpd(self):
        self.atkSpd = 0.658＊((1.0334)＊＊(Champion.1v - 1) )
    
    def beAtk(self, dem) :
        print("be attack", dem, 1-100.0/(100.0+100))
        self.dem = dem*(100.0/(100.0+100))
        print(self.dem)
        self.hp = self.hp-self.dem
        
    def setSpeed(self. sp):
        if (sp == 1):
            self.speed = 50
        else:
            self.speed = 0
            
    def setMovSpd(self):
        print("set Mov Spd")
        self.movSpd = (20 + self.speed)＊(1.00)*(100)
        
    def printStatus(self):
        print("champNam:%s, hp:%f, 1v%d, mvSpd:%f,atkSpd:%f % (self.champNam, self)")
        
ashe= Champion("ashe", 474.0)
mipo = Champion("mipo", 530.0)

ashe.printStatus()
mipo.printStatus()

mipo.beAtk(63.0)
mipo.printStatus() """

##
""" 
class champion :
    def ___init__(self, name) :
        self.name = name
        self.level = 1
        
class Yasuo(champion) :
    def getname(self) :
        print(self.name)
        
    def attack(self, key) :
        print(f"attack = {key}")
        
    def levelup(self) :
        self.level += 1
    
    def getlevel(self) :
        print(self.level)
        
class garen(champion) :
    def getname(self) :
        print(self.name)
        
        
class yasuo(champion) : ()

class garen(champion) : ()

user1 = yasuo("python")
user2 = garen("hello")

user1.getname()
user2.getlevel()

user2.getname()
user2.getlevel() """

##

""" def levelup(self) :
    self.level += 1
    
def getlevel(self) :
    print(self.level)
    
class yasuo(champion) :
    def attack(self, key):
        print(f"attack- {key} steel tempest")
        return
    
class garen(champion) :
    attack(self, key)
    print(f"attack- {key} demacian justice")
    return

user1 = yasuo ("python")
user2 = garen("hello")

user1.getname()
user2.getlevel()

user2.getname()
user2.getlevel() """


##

""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6) """
    
##
""" 
class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
user1 =Person("Alice", 30, "01011112222")

print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1.number)

user1._age = 21
user1.age = 23
print(user1.age) """


#
""" class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1 = Student("alice", 23, "01011112222")
user2 = Teacher("bob", 25, "01033334444")

print(getPersonName(user1))
print(getPersonName(user2)) """

#캡슐화

""" class Person : 
	def __init__(self, name, age, num) :
		self.name = name
		self.age = age
		self.number = num

	def getName(self) :
        return self.name

	def setName(self, newname) :
        return self.name = newname

	def getNumber(self) :
        return self.number

	def setNumber(self, newNum) :
        self.number = newnum
        return

p1= Person("python", 23, "01012345678")
p1.getNumber()
p2.getNumber()

p1.setNumber("11111111111")
p1.setNumber("22222222222") """


