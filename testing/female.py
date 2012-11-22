__author__ = 'mcalthrop'

import person

class Female(person.Person):
    def __init__(self, name):
        self.name = name
        person.Person.__init__(self, "female")

# EOF