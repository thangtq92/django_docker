from django.urls import path
from hospitalapp import views
from hospitalapp.views import (
    ListMenuView,
    CreateMenuView,
    UpdateMenuView,
    DetailMenuView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', ListMenuView.as_view(), name='list-menus'),
    path('create-menu/', CreateMenuView.as_view(), name='create-menu'),
    path('update-menu/<int:pk>', UpdateMenuView.as_view(), name='update-menu'),
    path('detail-menu/<int:pk>/', DetailMenuView.as_view(), name='detail-menu'),
    path('login/', views.SiteLoginView.as_view(), name='login'),
    path('logout/', views.SiteLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileEditView.as_view(), name='profile'),
]
