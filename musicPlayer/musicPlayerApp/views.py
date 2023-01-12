from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album

# Create your views here.


class homeView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class login(LoginView):
    template_name = 'login.html'

    def loginfunc(request):
        if request.method == 'POST':
            username2 = request.POST.get('username')
            password2 = request.POST.get('password')
            user = authenticate(
                request, username=username2, password=password2)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'ユーザ名またはパスワードが間違っています。'})
        return render(request, 'login.html')


class logout(LogoutView):
    template_name = 'logout.html'

    def logoutfunc(request):
        logout(request)


class upload(LoginRequiredMixin, CreateView):
    template_name = 'upload.html'
    model = Album
    fields = ('album_title', 'artist', 'album_jacket',
              'audio_file', 'song_lyric')
    success_url = reverse_lazy('home')


class detail(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Album


class delete(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Album
    success_url = reverse_lazy('home')
