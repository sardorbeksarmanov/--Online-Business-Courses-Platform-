from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import requests

class HomeView(View):
    def get(self, request):
        serves = requests.get('http://127.0.0.1:8002/api/serves/').json()
        advises = requests.get('http://127.0.0.1:8002/api/advisers/').json()
        clients = requests.get('http://127.0.0.1:8002/api/clients/').json()
        comments = requests.get('http://127.0.0.1:8002/api/comments/').json()
        features = requests.get('http://127.0.0.1:8002/api/features/').json()
        faqs = requests.get('http://127.0.0.1:8002/api/faqs/').json()

        context = {
            "serves": serves,
            "advises": advises,
            "clients": clients,
            "comments": comments,
            "features": features,
            "faqs": faqs,
        }
        return render(request, 'index.html', context)

class ServesView(View):
    def get(self, request):
        serves = requests.get('http://127.0.0.1:8002/api/serves/').json()
        context = {
            "serves": serves
        }
        return render(request, 'service.html', context)

class ServesDetailView(View):
    def serve_detail(request, slug):
        serve = get_object_or_404(ServesView, slug=slug)
        return render(request, 'serves_detail.html', {'serve': serve})
class AdviseView(View):
    def get(self, request):
        advises = requests.get('http://127.0.0.1:8002/api/advisers/').json()
        context = {
            "advises": advises
        }
        return render(request, 'advise.html', context)

class AdviseDetailView(View):
    def get(self, request):
        return render(request, 'advise-detail.html')

class ClientsViev(View):
    def get(self, request):
        clients = requests.get('http://127.0.0.1:8002/api/clients/').json()
        context = {
            "clients": clients
        }
        return render(request, 'clients.html', context)

class CommentView(View):
    def get(self, request):
        comment = requests.get('http://127.0.0.1:8002/api/comments/').json()
        context = {
            "comment": comment
        }
        return render(request, 'comment.html', context)

class FeatureView(View):
    def get(self, request):
        features = requests.get('http://127.0.0.1:8002/api/features/').json()
        context = {
            "features": features
        }
        return render(request, 'feature.html', context)

class FAQView(View):
    def get(self, request):
        faqs = requests.get('http://127.0.0.1:8002/api/faqs/').json()
        context = {
            "faqs": faqs
        }
        return render(request, 'FAQ.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')