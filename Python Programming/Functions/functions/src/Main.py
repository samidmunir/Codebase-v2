def capitalize_name(name) -> str:
    return name.title()

name = 'sami munir'
print(f'name: {name}')
print(f'\ncalling capitalize_name({name}):\n--> {capitalize_name(name)}')