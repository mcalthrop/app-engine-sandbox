__author__ = 'mcalthrop'

import person

class Male(person.Person):
    def __init__(self, name):
        self.name = name
        person.Person.__init__(self, "male")

# EOF