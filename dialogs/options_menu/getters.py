from cian.metro import METRO


async def get_lines(**kwargs):
    lines = [
        (line, num) for num, line in enumerate(METRO.keys())
    ]
    return {'lines': lines}