import time
import random

class Sleep(object):

    @staticmethod
    def random_sleep(min_value=0, max_value=1):
        time.sleep(min_value+(max_value-min_value)*random.random())


    