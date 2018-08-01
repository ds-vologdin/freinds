from django.views.generic import ListView, DetailView

from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/users_detail.html'
