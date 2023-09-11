from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView

from config import settings
from users.forms import UserForm, UserRegisterForm
from users.models import User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        email_confirm_key = self.object.email_confirm_key
        email_confirm_url = self.request.build_absolute_uri(
            reverse("users:verify_email", kwargs={"key": email_confirm_key}))
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Для завершения регистрации, пожалуйста, перейдите по ссылке: {email_confirm_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )
        return redirect(self.success_url)

