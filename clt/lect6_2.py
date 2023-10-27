#속성 출력

""" class person :
    name = 'python'
    age = 23
    number = '01012345678'
    
p = person()
print(p.name)
print(p.age)
print(p.number)

p1 = person()
print(p1.name)
print(p1.age)
print(p1.number) """


#메서드, 셀프

""" class person :
    name = 'python'
    age = 23
    number = "01012345678"
    
    def getIntroduce(self) :
        return f"My name is {self.name}"
    
    p = person()
    print(p.name)
    print(p.age)
    print(p.number)
    print(p.getintroduce) """
    
#클래스 초기화

""" class person :
    def __init__(self, name, age, number) :
        self.name = name
        self.age = age
        self.number = number
        
p = person("hello",24, "01087654321")
p1 = person("he", 21, "0108")
p2 = person("hee", 24, "028764321")

print(p.name)
print(p1.name)
print(p2.name) """

#클래스 변수 
""" 
class person :
	count = 0

	def __init__(self, name, age, number) :
		self.name = name
		self.age = age
		self.nmuber = number
		person.count += 1
  
	@classmethod
	def getCount(cls) : 
		return cls.count
  
p = person("hello", 24, "01087654321")
print(p.name)
print(p.getcount())
p1 = person("he", 32, "0108")
print(p1.name)
print(p1.getcount())
p2 = person("hee", 24,"028764321")
print(p2.name)
print(p2.getcount())
 """




