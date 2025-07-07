from django.urls import path
from .views import main, personeria, contraloria, vote_candidate, results

urlpatterns = [
    path('votes/',main, name='main'),
    path('votes/personería',personeria, name='personería'),
    path('votes/contraloría',contraloria, name='contraloría'),
    path('vote_candidate/<int:candidate_id>/', vote_candidate, name='vote_candidate'),
    path('results/', results, name='results'),
]