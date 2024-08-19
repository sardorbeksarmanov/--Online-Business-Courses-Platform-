from django.urls import path, include
from .views import HomeView, ServesView,  AdviseView, ClientsViev, CommentView, FeatureView, FAQView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('serves/', ServesView.as_view(), name='serves'),

    path('advise/', AdviseView.as_view(), name='advise'),

    path('clients/', ClientsViev.as_view(), name='clients'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('feature/', FeatureView.as_view(), name='feature'),
    path('FAQ/', FAQView.as_view(), name='FAQ'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('user/', include('user.urls')),

]
