from audioop import reverse
from operator import index
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, Comment
from django.views import generic 
from hitcount.views import HitCountDetailView
from .forms import NewUserForm, CommentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
# Create your views here.

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-updated_on')
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_count'] = self.queryset.count()
		print(context['post_count'])
		return context


class DetailView(HitCountDetailView):
  model = Post
  template_name = 'post_detail.html'
  count_hit = True

class AddPostView(generic.CreateView):
	model = Post
	template_name = 'add_post.html'
	fields = '__all__'

class AddCommentView(generic.CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
	success_url = reverse_lazy('home')
  
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")




