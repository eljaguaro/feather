from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth import login
from .models import User
from django.shortcuts import render



# def SignUp(request):
#     # context = {}
#     if request.method == 'POST':
#         form = CreationForm(request.POST)
#         if form.is_valid():
#             form.first_name = form.cleaned_data.get('first_name')
#             form.last_name = form.cleaned_data.get('last_name')
#             form.username = form.cleaned_data.get('username')
#             form.email = form.cleaned_data.get('email')
#             form.logo = form.cleaned_data.get('logo')
#             form.country = form.cleaned_data.get('country')
#             # login(request, User)
#             form.save()
#             return reverse_lazy('posts:index')
#         # else:
#             # form = context['creation_form'] = form
#     else:
#         form = CreationForm
#         # context['creation_form'] = form
#     return render(request, 'users/signup.html', {'form':form})
#     #     return render(request, 'posts/create_post.html', {'form': form})
#     # form = CreationForm()
#     # return render(request, 'users/signup.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
