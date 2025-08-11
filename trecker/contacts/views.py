from django.shortcuts import render
from django.views.generic import FormView
from .forms import ReviewForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
# Create your views here.


class ContactsView(FormView):
    template_name = "contacts/contacts.html"
    form_class = ReviewForm
    success_url = reverse_lazy("contacts")
    def form_valid(self, form):
        response = super().form_valid(form)

        user_message = form.cleaned_data['message']
        username = self.request.user.username

        send_mail(
            subject=f"Відгук про сайт",
            message=f"Вам надійшов відгук від {username}!\n\n{user_message}",
            from_email="qrprojectdjangoteam2@gmail.com",
            recipient_list=["artemvaschenko83@gmail.com"],
            fail_silently=False
        )

        return response