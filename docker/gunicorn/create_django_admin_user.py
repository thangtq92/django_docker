from django.contrib.auth.models import User
import os

if not User.objects.filter(username=os.environ.get('admin')):
    User.objects.create_superuser(
        os.environ.get('admin'),
        os.environ.get('admin@gmail.com'),
        os.environ.get('123456a@'),
    )
    print('Admin user was created.')
else:
    print('Admin user is existed.')