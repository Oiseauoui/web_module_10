from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.


class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="hw_project:root")
        return super(RegisterView, self).dispatch(request, * args, ** kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Bітaю {username}. Ваш аккаунт ycпішно створено')
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})


class SignInView(LoginView):
    template_name = "users/signin.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('quotes:root')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('quotes:root')

    def form_invalid(self, form):
        messages.error(self.request, 'Неправильний логін або пароль.')
        return super().form_invalid(form)


class LogoutView(BaseLogoutView):
    template_name = "users/logout.html"
    next_page = 'hw_project:root'  # Update this with your login URL

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Ви успішно вийшли із системи.')
        return redirect(to=self.next_page)



