def capitalize_name(name) -> str:
    return name.title()

name = 'sami munir'
print(f'name: {name}')
print(f'\ncalling capitalize_name():\n--> {capitalize_name(name)}')

from datetime import datetime

def get_time() -> str:
    now: datetime = datetime.now()
    return f'{now:%X}'

print(f'\ncalling get_time():\n--> {get_time()}')