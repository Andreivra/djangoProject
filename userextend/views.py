# from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from random import randint
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm, PasswordChangeNewForm
from userextend.models import History


class UserCreateView(CreateView):
    template_name = 'userextend/add_new_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            generate = randint(100000, 999999)
            new_user.username = f'{new_user.first_name.lower().strip()[0]}' \
                                f'{new_user.last_name.lower().replace(" ", "")}_{generate}'
            new_user.save()

            text = f"S-a adaugat un user nou in aplicatie cu urmatoarele informatii: first name este " \
                   f"{new_user.first_name}, last name-ul este {new_user.last_name} si mail {new_user.email}"

            History.objects.create(message=text, created_at=datetime.now(), updated_at=datetime.now())

            # Trimitere mail fara template
            # subject = 'Inregistrare in platforma cu success'
            # message = f'Felicitari, {new_user.first_name} {new_user.last_name}. Userul tau este {new_user.username}'
            # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # Trimitere mail cu template
            # details_user = {
            #     'full_name': f'{new_user.first_name} {new_user.last_name}',
            #     'username': new_user.username,
            #     'password': new_user.password,
            # }
            # subject = 'Creere cont nou cu succes'
            # message = get_template('mail.html').render(details_user)
            # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            # mail.content_subtype = 'html'
            # mail.send()

        return super().form_valid(form)


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    model = User
    form_class = PasswordChangeNewForm
    success_url = reverse_lazy('homepage')
