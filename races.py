import dictionaries

class Race():
    def __init__(self):
        self.scoreincrease = dictionaries.stats
        self.speed = 0
        self.proficiency = dictionaries.skills

class Goliath(Race):
    def __init__(self):
        Race.__init__(self)
        self.name = 'Goliath'

    def set_stats(self):
