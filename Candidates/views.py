from django.shortcuts import render, redirect
from .forms import VoteForm
from Users.models import Candidates, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def main(request):
    return render(request, 'Candidates/main.html')

@login_required(login_url='login')
def personeria(request):
    ombudsmans = Candidates.objects.filter(position='Personero')
    return  render(request, 'Candidates/personeria.html',{
        'ombudsman' : ombudsmans,
    })

@login_required(login_url='login')
def contraloria(request):
    comptrollers = Candidates.objects.filter(position='Contralor')
    return  render(request, 'Candidates/contraloria.html',{
        'comptrollers' : comptrollers,
    })

@login_required(login_url='login')
def vote_candidate(request, candidate_id):
    if request.method != 'POST':
        return redirect('main')
    ombudsmans = Candidates.objects.filter(position='Personero')
    comptrollers = Candidates.objects.filter(position='Contralor')
    try:
        candidate = Candidates.objects.get(id=candidate_id)
    except Candidates.DoesNotExist:
        messages.warning(request, 'El candidato no existe.')
        return redirect('main')
    data = dict()
    data['candidate_id'] = candidate_id
    form = VoteForm(data)
    if not form.is_valid():
        messages.warning(request, 'Error al enviar la votación.')
        return redirect('main')
    profile = Profile.objects.get(user=request.user)
    if candidate.position == 'Personero':
        
        if profile.voted_personero:
            messages.warning(request, 'Ya has votado por un personero.')
            return render(request, 'Candidates/main.html', {
                'ombudsman': ombudsmans,
            })
        candidate.votes += 1
        candidate.save()
        profile.voted_personero = True
        profile.save()
    elif candidate.position == 'Contralor':
        if profile.voted_contralor:
            messages.warning(request, 'Ya has votado por un contralor.')
            return render(request, 'Candidates/main.html', {
                'comptrollers': comptrollers,
            })
        candidate.votes += 1
        candidate.save()
        profile.voted_contralor = True
        profile.save()
    return redirect('main')

@login_required(login_url='login')
def results(request):
    if request.method != 'GET':
        return redirect('main')
    if not request.user.is_superuser:
        messages.warning(request, 'No tienes permiso para ver los resultados.')
        return redirect('main')
    ombudsmans = Candidates.objects.filter(position='Personero')
    comptrollers = Candidates.objects.filter(position='Contralor')
    
    votes_personero = sum(candidate.votes for candidate in ombudsmans)
    votes_contralor = sum(candidate.votes for candidate in comptrollers)
    
    for candidate in ombudsmans:
        if votes_personero > 0:
            candidate.percentage = (candidate.votes / votes_personero) * 100
        else:
            candidate.percentage = 0
        candidate.save()
    
    for candidate in comptrollers:
        if votes_contralor > 0:
            candidate.percentage = (candidate.votes / votes_contralor) * 100
        else:
            candidate.percentage = 0
        candidate.save()
        
    return render(request, 'Candidates/results.html', {
        'ombudsmans': ombudsmans,
        'comptrollers': comptrollers,
        })