
class Names:

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    def all(self):
        return '{} {}'.format(self.first, self.last)

scrum_member_1 = Names('Brayden', 'Basinger', 11)
scrum_member_2 = Names('Carter', 'Quartararo', 11)
scrum_member_3 = Names('Ryan', 'Mogdhaddas', 11)
scrum_member_4 = Names('Noah', 'Ahooja', 11)
scrum_member_5 = Names('Max', 'Wang', 10)



print(scrum_member_1.all())