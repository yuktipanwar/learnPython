class student:

    def __init__(self, name, major, cgpa, is_on_probation):
        self.name= name
        self.major= major
        self.cgpa = cgpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.cgpa >=6.5:
            return True
        else:
            return False
