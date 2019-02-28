""" Создадим класс с методом экзепляра (выполняются в контексте объекта) """

class Person(): # класс
    def __init__(self, that):
        # инициализатор - метод объекта, self - ссылка на объект, 
        # в контексте которого вызывается метод
        self.that = that + '!'

class Thing(): # еще один без __init__
    def some(self, this):
        return this + '?'

class Infinity(): # третий вовсе без метода
    lenght = 'not much' # свойство класса

person = Person('that') # экземпляры класса
thing = Thing()
infinity = Infinity()

# вызываем объекты
print(person.that + ' ' + thing.some('this') + ' ' + infinity.lenght) 


""" Динамическое присваивание """

class PersonDy():
    pass

def oneFunction(self, text):
    return text + ' ' + text + ' ' + text

# переопределим класс
PersonDy.summ = oneFunction 
persondy = PersonDy()
print(persondy.summ('letters'))


""" Наследование """

class NewPerson(Person): 
    def new(self): 
        # добавили новый метод
        return 'new'

class MultiPerson(Person, Thing, Infinity): # множественное наследование
    def multi(self): 
        return 'something new'

newperson = NewPerson('new multiperson')
multiperson = MultiPerson('new multiperson')

# вызовем объекты
print(newperson.that + ' ' + newperson.new())
print(multiperson.that + ' ' + multiperson.some('newthis') + ' ' + multiperson.lenght + ' ' + multiperson.multi())


""" Добавим новый параметр и используем метод из родителя """

class Help(Person):
    def __init__(self, that, thatnew):
        # перегрузили метод и добавили новый параметр
        super().__init__(that) # обратились к родителю за that
        self.thatnew = thatnew

helpthis = Help('what', 'alive')

print(helpthis.that)

# обрабатываем первый аргумент в родителе, второй в подклассе
print(helpthis.thatnew)


""" Специальные методы доступа """

class AccessExamp():
    def __init__(self, val):
        self._val = val

    def getvalue(self):
        #  геттер - получаем значение аттрибута
        return self._val
    
    def setvalue(self, val):
        # устанавливаем значение аттрибута
        self._val = val

    def delvalue(self):
        # удаляем значение аттрибута
        del self._val

    val = property(getvalue, setvalue, delvalue)

access = AccessExamp('fatality')
print(access.val)
access.val = 'finality'
print(access.val)


""" Сделаем новый класс со скрытым атрибутом """

class Special():
    def __init__(self, that):
        # атрибут __that доступен только внтури класса
        # можно использовать _that, но в таком случае
        # доступ не будет закрыт - это соглашение
        self.__that = that
    @property
    # геттер через декоратор
    def that(self):
        return self.__that
    @that.setter
    # сеттер через декоратор
    def that(self, that):
        self.__that = that

hidden = Special('something')

print(hidden.that) # внутри геттера

hidden.that = 'something new' # определяем новый аргумент для сеттера

print(hidden.that) # внутри сеттера

try:
    print(hidden.__that) # аргумент недоступен вне класса
except:
    print("AttributeError: 'Special' object has no attribute '__that'")

print(hidden._Special__that) # и все-таки доступ есть


""" Создадим класс с методом класса (выполняются в контексте класса) """

class ClassMethod():
    scream = 0
    def __init__(self):
        ClassMethod.scream += 1 # определили объект (атрибут класса)
    @classmethod
    # все что дальше определяет метод класса
    def aditional(cls):
        # определили метод класса, cls - первый параметр, 
        # эквивалентно ClassMethod
        return cls.scream

first_scream = ClassMethod()

second_scream = ClassMethod()

thierd_scream = ClassMethod()

print(ClassMethod.aditional()) #вызываем сам класс


""" Создадим класс со статическим методом """

class Static():
    @staticmethod
    # декоратор, определяющий статический метод
    def aditional():
        # при инициализации метода начальные параметры self, cls не используются
        return 'something'

# обращаемся к статическому методу. Создавать экземпляр не обязательно
print(Static.aditional())


""" Утиная типизация """

class Source():
    def __init__(self, att):
        self.att = att
    def func(self):
        # можно вызвать этот метод для любых объектов, включающих этот метод
        return self.att

class SubSource(Source):
    def func(self):
        return self.att

class Duck(): # новый класс, не являющийся подклассом Source
    def func(self):
        return 'Duck'

source = Source('why')

subsource = SubSource('because')

duck = Duck()

def Duck_revelation(obj):
    # запускаем метод для разных объектов, в т.ч. для 
    # несвязанных с методом, инициализирующим func()
    return obj.func()

print(Duck_revelation(source))

print(Duck_revelation(subsource))

print(Duck_revelation(duck)) # вуаля


""" Ассоциация (агрегация и композиция) """

# агрегация
class Content1():
    def __init__(self, post1):
        self.post1 = post1

class Content2():
    def __init__(self, post2):
        self.post2 = post2
        
class Agregator():
    def __init__(self, position1, position2):
        self.position1 = position1
        self.position2 = position2

    def summary(self):
        return 'this page have ' + self.position1 + ' and ' + self.position2

content1 = Content1('Yeeep')
content2 = Content2('Zzzap')
agregator = Agregator(content1.post1, content2.post2) # агрегируем свойства

print(agregator.summary()) # обращаемся к методу summary

# композиция

class Autor():
    def __init__(self, shidewr):
        self.shidewr = 'Luciano ' + shidewr

    def fullname(self):
        return self.shidewr

class Plagiathor():
    def __init__(self, shidewr, somethingbad):
        self.somethingbad = somethingbad
        self.autor = Autor(shidewr) # компонуем из другого класса
 
    def result(self):
        return 'I think ' + self.autor.fullname() + ' is better than ' + self.somethingbad
 
plagiathor = Plagiathor('Pavarotti', 'Baskov')
print(plagiathor.result())