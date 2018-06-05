from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AllNotesList.as_view(), name='home'),
    url(r'^add_note$', views.AddNote.as_view(), name='add_note'),
    url(r'^success$', views.success, name='success'),
]
