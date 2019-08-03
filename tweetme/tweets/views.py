from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
	DetailView,ListView,CreateView,UpdateView,DeleteView)
from .forms import TweetModelForm
from django.db.models import Q
# Create your views here.
from .models import Tweet
from .mixins import FormUserNeededMixin,UserOwnerMixin

class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
	template_name = "tweets/create_view.html"
	form_class = TweetModelForm
	#success_url = "/tweet/create/"
	login_url = "/admin"

	"""def form_valid(self,form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user
			return super(TweetCreateView,self).form_valid(form)
		else:
			form.errrs[forms.forms.NON_FILED_ERRORS] = ErrorList(["User must be logged in to Continue"])
			return self.form_invalid(form)

def tweet_create_view(request):
	form = TweetModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	context ={
	"form":form
	}
	return render(request,'tweets/create_view.html',context)
"""
class TweetDetailView(DetailView):
	template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()

	"""def get_object(self):
		pk = self.kwargs.get("pk")
		return Tweet.objects.get(id=pk)"""

class TweetListView(ListView):
	template_name = "tweets/list_view.html"

	def get_queryset(self,*args,**kwargs):
		qs = Tweet.objects.all()
		query = self.request.GET.get('q',None)
		if query:
			qs = qs.filter(Q(content__icontains=query) | 
						   Q(user__username__icontains=query))
		return qs

	def get_context_data(self,*args,**kwargs):
		context = super(TweetListView,self).get_context_data(*args,**kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy("tweet:create")
		return context


"""def tweet_detail_view(request,id=1):
	obj = Tweet.objects.get(id=id)
	context = {
	"object":obj
	}
	return render(request,"tweets/detail_view.html",context)

def tweet_list_view(request):
	queryset = Tweet.objects.all()
	context = {
	"object_list":queryset
	}
	return render(request,"tweets/list_view.html",context)"""

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = "tweets/update_view.html"
	success_url = "/tweet/"

class TweetDeleteView(LoginRequiredMixin,DeleteView):
	model = Tweet
	template_name = "tweets/delete_confirm.html"
	success_url = reverse_lazy("tweet:list")
