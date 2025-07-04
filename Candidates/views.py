from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Users.models import Personero, Contralor, Profile

# Create your views here.
@login_required(login_url='login')
def main(request):
    return render(request, 'Candidates/main.html')

@login_required(login_url='login')
def personeria(request):
    candidates = Contralor.objects.all()
    return  render(request, 'Candidates/personeria.html',{
        'candidates' : candidates,
    })

@login_required(login_url='login')
def contraloria(request):
    candidates = Personero.objects.all()
    return  render(request, 'Candidates/contraloria.html',{
        'candidates' : candidates,
    })

@login_required(login_url='login')
def vote_candidate(request, candidate_id):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        try:
            candidate = Personero.objects.get(id=candidate_id)
            if profile.voted_personero:
                return render(request, 'Candidates/personeria.html', {'error': 'Ya has votado por personería.'})
            profile.voted_personero = True
        except Personero.DoesNotExist:
            candidate = Contralor.objects.get(id=candidate_id)
            if profile.voted_contralor:
                return render(request, 'Candidates/contraloria.html', {'error': 'Ya has votado por contraloría.'})
            profile.voted_contralor = True
        except Contralor.DoesNotExist as e:
            return render(request, 'Candidates/main.html', {'error': str(e)})
        profile.save()
        if profile.voted_personero and profile.voted_contralor:
            profile.user.is_active = False
            profile.user.save()
            candidate.votes += 1
            candidate.save()
            return render(request, 'Candidates/error.html', {'error': 'Ya has votado para ambos condidatos, no puedes votar dos veces.'})
        candidate.vote += 1
        candidate.save()
        return redirect('main')