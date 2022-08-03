from django.db import models
from django.core.validators import MinValueValidator 
from card.templatetags.card_templates import substract_time
from datetime import datetime, timezone

class Card(models.Model):
    states_list = [x for x in range(1, 59)]
    states = []
    for state in states_list:
        states.append([("0" + str(state))[-2:],("0" + str(state))[-2:]])
    wilaya = models.CharField( max_length=50, choices=states)
    madina = models.CharField( max_length=50, )
    title = models.CharField( max_length=200)
    count = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.wilaya.capitalize()}, {self.madina.capitalize()}, {self.title}, {self.count}"

    def wilaya_in_str(self):
        states = ["", "أدرار","الشلف","الأغواط","أم البواقي","باتنة","بجاية","بسكرة","بشار","البليدة","البويرة","تمنراست","تبسة","تلمسان","تيارت","تيزي وزو","الجزائر","الجلفة","جيجل","سطيف","السعيدة","سكيكدة","سيدي بلعباس","عنابة","قالمة","قسنطينة","المدية","مستغانم","المسيلة","معسكر","ورقلة","وهران","البيض","إليزي","برج بوعريريج","بومرداس","الطارف","تندوف","واد سوف","خنشلة","سوق اهراس","تيبازة","ميلة","عين الدفلى","النعامة","عين تموشنت","غرادية","غليزان","تيميمون","برج باجي مختار","أولاد جلال","بني عباس","عين صالح","عين قزام","توقرت","ولاية جانت","ولاية المغير","ولاية المنيعة",]
        return states[int(self.wilaya)]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.created_at:
            delta = substract_time(datetime.now(timezone.utc), self.created_at)
            if isinstance(delta, int):
                if delta > 1440 :
                    self.delete()
