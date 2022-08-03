from pyexpat import model
from django import forms
from .models import Card

class CardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields=["wilaya", "madina", "title", "count"]

  def __init__(self, *args, **kwargs):
    super(CardForm, self).__init__(*args, **kwargs)
    for key, value in self.fields.items():
      value.widget.attrs['class'] = "form-control text-right  mb-2"
      if key == "title":
        value.widget.attrs['placeholder'] = "مثال: بريد, مستشفى"
