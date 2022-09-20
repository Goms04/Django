from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from customers import models as m



def index(request):
    return render(request, 'listings/content.html')

def Accueil(request):
    return render(request, 'listings/accueil.html')


def historique(request):
    locationns = m.Location.objects.select_related('client', 'voiture')
    context = {'loc': locationns}
    return render(request, 'listings/historique.html', context)


###################################  Ajout de voiture   ######################################
def ajouter(request):
    if(request.method == "POST"):

        # variable / champ html(name)
        marque = request.POST['marque']
        couleur = request.POST['couleur']
        annee = request.POST['annee']
        porte = request.POST['nb_portes']
        climatiser = request.POST['clim']
        energie = request.POST['energie']
        m.Voiture.objects.create(

            #nom_base_de_données / variable
            marque=marque,
            couleur=couleur,
            annee=annee,
            porte=porte,
            climatiser=climatiser,
            energie=energie,
        )
        return redirect('/customers/voitures')

    else:
        voiture = m.Voiture.objects.all()
        context = {'voitures': voiture}
        return render(request, 'listings/voiture.html', context)



###################################   suppression de voiture   ############################################
def supprimer_voiture(request, voiture_id):
    voiture = m.Voiture.objects.get(pk=voiture_id)
    msg = messages.add_message(request, messages.SUCCESS,'Voiture supprimée avec succès.', fail_silently=True)
    if request.method == 'POST':
        voiture.delete()
        context = {'messages': msg}
        return redirect('/customers/voitures/', context)


###################################  modification de voiture   ######################################

def modifier_voiture(request, voiture_id):
    voiture = m.Voiture.objects.get(pk=voiture_id)
    msg = messages.add_message(request, messages.SUCCESS,'Voiture modifiée avec succès.', fail_silently=True)
    if request.method == 'POST':
        voiture.marque = request.POST['marque']
        voiture.couleur = request.POST['couleur']
        voiture.annee = request.POST['annee']
        voiture.porte = request.POST['nb_portes']
        voiture.climatiser = request.POST['clim']
        voiture.energie = request.POST['energie']

        voiture.save()
        context = {'messages':msg}
        return redirect('/customers/voitures/', context)


##################################  Enregistrement d'une location de voiture   ######################################
def location(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenoms']
        sexe = request.POST['sexe']
        profession = request.POST['profession']
        credible = request.POST['credible']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        voiture_id = request.POST['voiture_id']
        m.Client.objects.create(
            nom=nom,
            prenoms=prenom,
            sexe=sexe,
            profession=profession,
            credible=credible )
        clt = m.Client.objects.latest('id')
        m.Location.objects.create(
            date_debut=date_debut,
            date_fin=date_fin,
            voiture_id=voiture_id,
            client_id=clt.id
        )
        msg = messages.add_message(request, messages.SUCCESS, 'Location enregistrée avec succès.', fail_silently=True)
        context = {'messages': msg}
        return redirect ('/customers/locations/', context)
    else:
        voiture = m.Voiture.objects.all()
        client = m.Client.objects.all()
        context = {'voitures': voiture, 'clients': client}
        return render(request, 'listings/location.html', context)





###################################  modification de Client   ######################################

def modifier_client(request, client_id):
    clt = m.Client.objects.get(pk=client_id)
    msg = messages.add_message(request, messages.SUCCESS,'Client modifié avec succès.', fail_silently=True)
    if request.method == 'POST':
        clt.nom = request.POST['nom']
        clt.prenoms = request.POST['prenoms']
        clt.profession = request.POST['profession']
        #clt.credible = request.POST['credible']
        clt.save()
        context = {'messages': msg}
        return redirect('/customers/locations/', context)


###################################  suppression de cient   ######################################


def supprimer_client(request, client_id):
    clt = m.Client.objects.get(pk=client_id)
    msg = messages.add_message(request, messages.SUCCESS, 'Client supprimé avec succès.', fail_silently=True)
    if request.method == 'POST':
        clt.delete()
        context = {'messages': msg}
        return redirect('/customers/locations/', context)

def details(request, client_id):
    locationns = m.Location.objects.select_related('client', 'voiture').filter(client_id=client_id)
    clt = m.Client.objects.get(pk=client_id)
    context = {'loc': locationns}
    return render(request, 'listings/details.html', context)



