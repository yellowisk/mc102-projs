# RA: 245293
# https://github.com/guilhermevleite/mc102_24-1

from datetime import date
import sys

class Data:
    '''
    Data
    --------
    Represents dates in the format dd/mm/yyyy.
    '''
    def __init__(self: 'Data', dia: int, mes: int, ano: int) -> None:
        self._dia = dia
        self._mes = mes
        self._ano = ano

    @property
    def dia(self: 'Data') -> int:
        return self._dia
    @dia.setter
    def dia(self: 'Data', dia: int) -> property:
        self._dia = int(dia)
    
    @property
    def mes(self: 'Data') -> int:
        return self._mes
    @mes.setter
    def mes(self: 'Data', mes: int) -> property:
        self._mes = int(mes)
    
    @property
    def ano(self: 'Data') -> int:
        return self._ano
    @ano.setter
    def ano(self: 'Data', ano: int) -> property:
        self._ano = int(ano)
    
    def __str__(self: 'Data') -> str:
        return f'{self._dia}/{self._mes}/{self._ano}'
    
    @staticmethod
    def get_from_string(string: str) -> 'Data':
        dia, mes, ano = map(int, string.split('/'))
        return Data(dia, mes, ano)
    
    @classmethod
    def __date__(self: 'Data') -> date:
        return date(self._ano, self._mes, self._dia)

    @classmethod  
    def __dateformat__(self: 'Data') -> str:
        return "{:02d}/{:02d}/{:04d}".format(self._dia, self._mes, self._ano)

class Voo:
    '''
    Voo
    -
    Represents a flight with a number, destination, departure date and price.
    '''
    def __init__(self: 'Voo', number: str, destination: str, departure: Data, price: float) -> None:
        self._number = number
        self._destination = destination
        self._departure = departure
        self._price = price

    @property
    def number(self: 'Voo') -> str:
        return self._number
    @number.setter
    def number(self: 'Voo', number: str) -> property:
        self._number = number
    
    @property
    def destination(self: 'Voo') -> tuple:
        return self._destination
    @destination.setter
    def destination(self: 'Voo', destination: str) -> property:
        self._destination = destination
    
    @property
    def departure(self: 'Voo') -> Data:
        return self._departure
    @departure.setter
    def departure(self: 'Voo', departure: Data) -> property:
        if isinstance(departure, Data):
            self._departure = departure
        else:
            raise ValueError('Departure must be a Data object')
    
    @property
    def price(self: 'Voo') -> float:
        return self._price
    @price.setter
    def price(self: 'Voo', price: float) -> property:
        self._price = float(price)

    def __str__(self: 'Voo') -> str:
        return f'{self._number} {self._destination[0]} {self._destination[1]} {self._departure} {self._price}'
    
    @staticmethod
    def register(number: str, destination: str, departure: str, price: float) -> 'Voo':
        date = Data.get_from_string(departure).__date__()
        voo = Voo(number, (destination.split()), date, float(price))
        return voo

    @classmethod
    def alter(self: 'Voo', price: float) -> None:
        former_price = self._price
        self._price = float(price)
        print(f'{self._number} valor alterado de {former_price} para {self._price}')

    @staticmethod
    def sum_flights_cost(flight_come: 'Voo', flight_leave: 'Voo') -> float:
        return flight_come.price + flight_leave.price

    @staticmethod
    def get_possible_flights(origin: str, dates: str, flights_list: list) -> list:
        dt_date_start, dt_date_end = map(Data.__date__, map(Data.get_from_string, dates.split()))
        come_froms = [flight for flight in flights_list if flight.destination[0] == origin and flight.departure >= dt_date_start]
        leave_froms = [flight for flight in flights_list if flight.destination[1] == origin and flight.departure <= dt_date_end]
        possible_flights = []

        for come in come_froms:
            for leave in leave_froms:
                if (leave.departure - come.departure).days >= 4 and (come,leave) not in possible_flights:
                    possible_flights.append((come, leave))
        return possible_flights

    @staticmethod
    def get_cheapest_flight(flights_list: list) -> tuple:
        cheapest = Voo.sum_flights_cost(flights_list[0][0], flights_list[0][1])
        for flight in flights_list:
            if Voo.sum_flights_cost(flight[0], flight[1]) <= cheapest:
                pass
            else:
                flights_list.remove(flight)
        return flights_list[0]

    @staticmethod
    def plan(origin: str, dates: str, flights_list: list) -> None:
        possible_flights = Voo.get_possible_flights(origin, dates, flights_list)

        cheapest_flight = Voo.get_cheapest_flight(possible_flights)

        print(cheapest_flight[0].number, cheapest_flight[1].number, sep='\n')

def menu(action: str) -> None:
    if action == "registrar":
        data = [input() for _ in range(4)]
        new_voo = Voo.register(*data)
        voos.append(new_voo)

    if action == "alterar":
        number, price = input().split()
        for voo in voos:
            if voo.number == number:
                voo.alter(price)
    if action == "cancelar":
        number = input()
        for voo in voos:
            if voo.number == number:
                voos.remove(voo)
    if action == "planejar":
        Voo.plan(input(), input(), voos)

voos = []

for line in sys.stdin:
    menu(line.strip())