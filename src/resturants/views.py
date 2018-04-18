from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import ResturantLocation
from .forms import ResturantLocationCreateForm

class ContactTemplateView(TemplateView):
	template_name = "contact.html"
	def get_context_data(self, *args, **kwargs):
		context = {"author" : "devBOX",
				"name": "Debasish Padhi",
				"no" : "7008154472",}
		return context

class Home(TemplateView):
	template_name = "home.html"

class About(TemplateView):
	template_name = "about.html"
	def get_context_data(self, *args, **kwargs):
		context = {"author" : "devBOX",
				"description" : "I am a web developer and along with that i'm a machine learning enthusiast."}
		return context

class SearchResturantList(ListView):

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = ResturantLocation.objects.filter(
				Q(category__iexact = slug) |
				Q(category__icontains = slug)
				)
			
		else:
			queryset = ResturantLocation.objects.all()
		return queryset

class ResturantDetailView(DetailView):
	queryset = ResturantLocation.objects.all()
	
	# def get_object(self, *args, **kwargs):
	# 	pk = self.kwargs.get("pk")
	# 	obj = get_object_or_404(ResturantLocation, pk=pk)
	# 	return obj
class ResturantCreateView(LoginRequiredMixin, CreateView):
    form_class = ResturantLocationCreateForm
    login_url = '/login/'
    template_name = 'resturants/form.html'
    success_url = "/resturants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ResturantCreateView, self).form_valid(form)