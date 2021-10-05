from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):

#     login_url = "bases:login"
#     raise_exception = False
#     redirect_field_name = "redirect_to"

#     def handle_no_permission(self):
#         from django.contrib.auth.models import AnonymousUser
#         if not self.request.user == AnonymousUser():
#             self.login_url = 'bases:sin_privilegios'
#         return HttpResponseRedirect(reverse_lazy(self.login_url))


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name = "bases/sin_privilegios.html"

    
def home(request):

    return render(request, 'bases/index.html')
