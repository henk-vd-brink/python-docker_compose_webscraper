from itertools import count

class Page(object):

    def __init__(self, base_url, initial_page_number=0):
        self._base_url = base_url
        self.set_page_number(initial_page_number)

    def set_page_number(self, initial_page_number):
        if initial_page_number > 0:
            self._page_number = initial_page_number-1
        else:
            self._page_number = initial_page_number

    def __iter__(self):
        return self

    @property
    def __next__(self):
        self._page_number += 1
        
        if (page_number := self._page_number) == 1:
            return self._base_url
        else:
            return self._base_url+f"p/{page_number}/"