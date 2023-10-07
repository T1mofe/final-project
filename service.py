import random
import time 


def random_number():
    return random.randint(2,10)


def start_timer():
    start_time = random_number()
    for i in range(start_time):
        time.sleep(1)
        