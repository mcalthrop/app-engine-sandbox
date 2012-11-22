__author__ = 'mcalthrop'

import male
import female
import mcalthrop

matt = male.Male("matt")
siobhan = female.Female("siobhan")
people = [matt, siobhan, mcalthrop.MCalthrop()]

for person in people:
    print person.name, person.sex

# EOF