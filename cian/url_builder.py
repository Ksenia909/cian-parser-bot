from typing import Dict, List

from cian.metro import METRO


class URLBuilder:
    def __init__(self, data: Dict[str, any]):
        self.params = {
            'currency': '2',
            'deal_type': 'rent',
            'engine_version': '2'
        }

        if 'time' in data:
            self.add_time(data['time'])
        if 'price' in data:
            self.add_price(data['price_max'], is_max=True)
        if 'metro' in data:
            self.add_metro(data['metro'])
        if 'price' in data:
            self.add_price(data['price_min'], is_max=False)
        self.params['offer_type'] = 'flat'
        if 'time' in data:
            self.add_only_food()
        if 'rooms' in data:
            self.add_rooms(data['rooms'])
        self.params['sort'] = 'creation_date_desc'
        self.params['type'] = '4'

    def add_time(self, time: str):
        self.params['foot_min'] = time

    def add_price(self, price: str, is_max: bool):
        key = 'maxprice' if is_max else 'minprice'
        self.params[key] = price

    def add_metro(self, dict_metro: Dict[str, List[str]]):
        metro = []
        for line, stations in dict_metro.items():
            for station in stations:
                metro.append(METRO[line][station])
        for num, station in enumerate(sorted(metro, key=int)):
            self.params[f'metro%5B{num}%5D'] = station

    def add_only_food(self):
        self.params['only_foot'] = '2'

    def add_rooms(self, rooms: List[int]):
        for room in sorted(rooms, key=int):
            self.params[f'room{room}'] = '1'

    @property
    def url(self):
        return f'https://www.cian.ru/cat.php?{"&".join(f"{k}={v}" for k, v in self.params.items())}'



