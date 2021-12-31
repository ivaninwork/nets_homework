from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser('admin', 'admin@admin.ru', '123456aa')
User.objects.create_user(
    username='tomas',
    email='admin@admin.ru',
    password='123456aa',
    first_name='tomas',
    last_name='edison'
)
