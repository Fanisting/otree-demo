from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(label= "Gender")
    age = models.IntegerField(label= "Age")



# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['gender', 'age']


class Results(Page):
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import json
        answers = [player.gender, player.age] # make a list to store answers
        player.participant.answers = json.dumps(answers) # transform answers into string using json



        


page_sequence = [MyPage, Results]
