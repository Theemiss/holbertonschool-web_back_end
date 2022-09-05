#!/usr/bin/env python3
"""
0x02. Asynchronous Programming
"""


import random


async def async_generator():
    """The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    for i in range(10):
        yield random.random()*10
