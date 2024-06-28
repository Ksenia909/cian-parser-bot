from aiogram_dialog import DialogManager

from cian.metro import METRO
from dialogs.options_menu.constants import SCROLLING_HEIGHT, NUMBER_OF_ROOMS


async def get_menu(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.current_context().dialog_data
    menu_info = {
        'metro': 'не задано',
        'time': 'не задано',
        'rooms': 'не задано',
        'price': 'не задано'
    }

    if 'metro' in data:
        menu_info['metro'] = '\n'.join(
            [f'{line} - {", ".join(metro_stations)}' for line, metro_stations in data['metro'].items()]
        )

    if 'time' in data:
        menu_info['time'] = data['time']

    if 'rooms' in data:
        rooms_name = list(NUMBER_OF_ROOMS.keys())
        menu_info['rooms'] = ', '.join(
            [rooms_name[int(num)] if num != '9' else rooms_name[0] for num in data['rooms']]
        )

    if 'price' in data:
        price_range = sorted(data['price'])
        menu_info['price'] = f'от {price_range[0]} до {price_range[1]}'

    return menu_info


async def get_lines(**kwargs):
    lines = [
        (line, num) for num, line in enumerate(METRO.keys())
    ]
    return {'lines': lines}


async def get_stations(dialog_manager: DialogManager, **kwargs):
    index_line = int(dialog_manager.current_context().dialog_data.get('line'))
    line = list(METRO.keys())[index_line]
    stations = []
    len_line = len(METRO[line])

    for num, station in enumerate(METRO[line]):
        stations.append((station, num))

        if (num + 1) % (SCROLLING_HEIGHT - 1) == 0 or num+1 == len_line:
            stations.append(('✅ Подтвердить ✅', 'back_to_menu'))

    return {
        'name_line': line,
        'stations': stations
    }


async def get_rooms(**kwargs):
    rooms = [(rooms, num) for rooms, num in NUMBER_OF_ROOMS.items()]
    rooms.append(('✅ Подтвердить ✅', 'back_to_menu'))
    return {'rooms': rooms}


