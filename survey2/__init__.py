from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender_new = models.StringField(label= "Gender", blank=True, defalt="no response")
    age_new = models.IntegerField(label= "Age", blank=True, default=0)



# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['gender_new', 'age_new']
    @staticmethod
    def vars_for_template(player: Player):
        import json
        answers = json.loads(player.participant.answers)
        return dict(answers=answers)
    

class Results(Page):
    pass


page_sequence = [MyPage, Results]
