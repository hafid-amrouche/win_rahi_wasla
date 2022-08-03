from django.shortcuts import render, redirect
from card.forms import CardForm
from card.models import Card
from datetime import datetime as dt, timezone


def home(request):
    if request.method == 'GET':
        context={
            "form" : CardForm,
            "cards" : Card.objects.all(),
            "dt" : dt.now(timezone.utc),
        }
        return render(request, "base.html", context)

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context={
            "form" : form,
            }
            return render(request, "base.html", context)

def search(request):
    wilaya = request.GET.get('wilaya')
    madina = request.GET.get('madina')
    title = request.GET.get('title')
    cards = None
    card = Card
    if card.objects.filter(wilaya=wilaya):
        cards = card.objects.filter(wilaya=wilaya)
        print("hhh1")
    if card.objects.filter(wilaya=wilaya, madina__icontains=madina):
        cards = card.objects.filter(wilaya=wilaya, madina__icontains=madina)
        print("hhh2")
    if card.objects.filter(wilaya=wilaya, madina__icontains=madina, title__icontains=title):
        cards = card.objects.filter(wilaya=wilaya, madina__icontains=madina, title__icontains=title)
        print("hhh3")

    context={
            "form" : CardForm,
            "cards" : cards,
            "dt" : dt.now(timezone.utc),
        }
    return render(request, "base.html", context)
