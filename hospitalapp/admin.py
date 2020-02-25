from django.contrib import admin
from .models import Menu, Categories

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'prior', 'id_parent')


admin.site.register(Menu, MenuAdmin)


# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('code', 'id_parent', 'status', 'sort_order')
    search_fields = ['code', ]
    none_type = type(None)

    def get_form(self, request, obj=None, **kwargs):
        request.obj = obj

        if isinstance(obj, self.none_type) is True:
            self.exclude = ("sort_order",)
        else:
            self.exclude = None

        return super(CategoriesAdmin, self).get_form(request, obj, **kwargs)


User = get_user_model()
@admin.register(User)
class ProfilesUserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'gender', 'phone_number')

    # Tuỳ biến quản trị user, override bỏ 2 trường firt_name, last_name
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'full_name',
            'email',
            'phone_number',
            'gender',
            'address',
            'about',
        )
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)