import string
import random

class Robot(object):
    def __init__(self):
        self.gen_letter = random.choice(string.ascii_letters).upper()
        self.gen_digit = random.randint(0,9)
        self.name = "".join([random.choice(string.ascii_letters).upper(), random.choice(string.ascii_letters).upper(),
        str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))])
    
    def reset(self):
        self.name = "".join([random.choice(string.ascii_letters).upper(), random.choice(string.ascii_letters).upper(),
        str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))])