# посмотрим как устроена композиция

class Address:
    """
    Мы реализовали базовый класс адресов, который содержит обычные компоненты для адреса. 
    Сделали атрибут street2 необязательным, поскольку не все адреса будут иметь этот компонент.
    Реализовали __str__(), чтобы обеспечить красивое представление Address

    Когда вы выводите на экран переменную address, вызывается специальный метод __str__(). 
    Поскольку мы перегрузили метод, чтобы вернуть строку, отформатированную как адрес, 
    мы получили хорошее, читаемое представление.
    """
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

"""
Мы инициализируем атрибут address в классе Employee значением None на данный момент, чтобы сделать его необязательным, 
но, сделав это, теперь можно назначить Address для Employee. В модуле employee нет ссылки на модуль contacts
"""