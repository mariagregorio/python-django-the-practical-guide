from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'Eat healthy',
    'february': 'Don\'t drink too much alcohol',
    'march': 'Save someone\'s life',
    'april': 'Buy flowers for mum',
    'may': 'Learn to swim better',
    'june': 'Get a better job',
    'july': 'Study harder',
    'august': 'Visit a new country',
    'september': None,
    'october': 'Don\'t do coke',
    'november': 'Try a different bathing suit',
    'december': 'Have a merry christmas'
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month == 0 or month > len(months):
        raise Http404()

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # first param is url name from urlpatterns path

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'text': challenge_text
        })
    except:
        raise Http404()