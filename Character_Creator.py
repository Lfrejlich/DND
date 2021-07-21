import dictionaries
import random
import functions
import math

class Character():
    #Creates variables for each character
    def _init_(self):
        self.first_name = ''
        self.last_name = ''
        self.race = ''
        self.classes = ''
        self.mainstats = {}
        self.secondarystats = {}
        self.level = 0
        self.proficiencybonus = 0


    def get_name(self):
        #sets a random gender then pulls first and last name from name dictionaries
        get_gender = random.randint(0,1)
        if get_gender == 0:
            self.first_name = dictionaries.malefirstname[random.randint(1,8)]
        if get_gender == 1:
            self.first_name = dictionaries.femalefirstname[random.randint(1,8)]
        self.last_name = dictionaries.lastname[random.randint(1,8)]

    def get_race(self):
        #gets random race from dictionaries
        self.race = dictionaries.races[random.randint(1,9)]

    def get_classes(self):
        #gets random class from dictionaries
        self.classes = dictionaries.classes[random.randint(1,12)]

    def get_main_stats(self):
        #randomly generate stats for character. ***add in priority for classes after***
        self.mainstats = dictionaries.stats
        self.mainstats['Str'] = functions.roll_stat()
        self.mainstats['Dex'] = functions.roll_stat()
        self.mainstats['Con'] = functions.roll_stat()
        self.mainstats['Int'] = functions.roll_stat()
        self.mainstats['Wis'] = functions.roll_stat()
        self.mainstats['Chr'] = functions.roll_stat()
    
    def get_secondary_stats(self):
        #set secondary stats based on main stats and proficiency bonus
        self.secondarystats = {'Acrobatics': self.mainstats['Dex'], 'Animal Handling': self.mainstats['Wis'], 'Arcana': self.mainstats['Int'], 'Athletics': self.mainstats['Str'], 'Deception': self.mainstats['Chr'], 'History': self.mainstats['Int'], 'Insight': self.mainstats['Wis'], 'Intimidation': self.mainstats['Chr'], 'Investigation': self.mainstats['Int'], 'Medicine': self.mainstats['Wis'], 'Nature': self.mainstats['Int'], 'Perception': self.mainstats['Wis'], 'Performance': self.mainstats['Chr'], 'Persuasion': self.mainstats['Chr'], 'Religion': self.mainstats['Int'], 'Sleight of Hand': self.mainstats['Dex'], 'Stealth ': self.mainstats['Dex'], 'Survival': self.mainstats['Wis']}


    def get_level(self):
        self.level = 1

    def get_proficiency_bonus(self):
        self.proficiencybonus = int(math.ceil(1 + (self.level/4)))