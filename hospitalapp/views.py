from django.shortcuts import render
from hospitalapp.models import Menu
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy

from .forms import CreateMenuForm
def index(request):
    menuParents = Menu.objects.filter(id_parent=0)

    context = {
        'parents': menuParents
    }
    return render(request, 'home/index.html', context)

class ListMenuView(ListView):
    model = Menu
    paginate_by = 2
    def get(self, request, *args, **kwargs):
        template_name = 'menus/list-menu.html'  # sẽ được tạo ở phần dưới
        # Rename Model objects default to namenew
        obj = {
            'menus': Menu.objects.all()
        }
        return render(request, template_name, obj)


class CreateMenuView(SuccessMessageMixin, CreateView):
    template_name = 'menus/create-menu.html'
    form_class = CreateMenuForm
    success_message = 'Create Menu successfully!'


class UpdateMenuView(SuccessMessageMixin, UpdateView):
    template_name = 'menus/update-menu.html'
    model = Menu
    fields = ['name', 'description', ]
    success_message = 'Update Menu successfully!'

    def get_success_url(self):
        return reverse('list-menus', kwargs={})


class DetailMenuView(SuccessMessageMixin, DetailView):
    # Default model is object
    model = Menu
    template_name = 'menus/detail-menu.html'


# Profiles
# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(View):
    def get(self, request):
        #object_list = ProfileEditView.objects.all()
        return render(request, 'home/home.html', )


class SiteLoginView(LoginView):
    template_name = 'profile/login.html'

class SiteLogoutView(LogoutView):
    next_page='/'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('full_name', 'address', 'dob', 'gender', 'about', 'phone_number')
    template_name = 'profile/profile.html'
    success_url = reverse_lazy('profile')  # Trả về 1 chuỗi, chuỗi đó là đường dẫn và chuyển tới trang profile

    def get_object(self, queryset=None):
        return self.request.user