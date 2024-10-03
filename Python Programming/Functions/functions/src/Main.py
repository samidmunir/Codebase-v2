def capitalize_name(name) -> str:
    return name.title()

name = 'sami munir'
print(f'name: {name}')
print(f'\ncalling capitalize_name():\n--> {capitalize_name(name)}')

from datetime import datetime

"""
    A function that gets the current time and returns it as a string.
    
    :Example:
    >>> get_time()
    "08:08:15"
"""
def get_time() -> str:
    now: datetime = datetime.now()
    return f'{now:%X}'

print(f'\ncalling get_time():\n--> {get_time()}')

from collections.abc import Iterable
def get_total_discount(prices: Iterable[float], percent: float) -> float:
    """
        Calculates the total price after applying a discount.
    
        This function calculates the total sum of prices in the provided
         list and then applies a discount based on the given discount rate.
         If the discount rate is invalid (e.g., negative or greater than 1),
         the function raises a ValueError.
     
        :param prices: A list of item prices.
        :type prices: list[float]
        :param percent: The discount rate to apply. Default is 0.1 (10%).
        :type percent: float, optional
        :return: The total price after applying the discount.
        :rtype: float
        :raises ValueError: If the discount_rate is not between 0 and 1
            inclusive, or if prices contain non-numeric values.
    
        :Example:
        >>> get_total_discount([100.0, 50.0, 25.0], 0.2)
        140.0
    """
    # validate input
    if not (0 <= percent <= 1):
        raise ValueError(f'Invalid discount rate: {percent}. Must be [0, 1] inc.')
    
    if not all(isinstance(price, (int, float)) and price >= 0 for price in prices):
        raise ValueError('All prices must be non-negative numbers.')
    
    total: float = sum(prices)
    
    return total * (1 - percent)

print(f'\ncalling get_total_discount():\n--> {get_total_discount([100.0, 50.0, 25.0], 0.2)}')