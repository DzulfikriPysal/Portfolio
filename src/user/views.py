from django.shortcuts import render
from django.http import HttpResponse
from user.forms import AccountAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.models import CustomUser
from django.views import generic
from blog.models import Blog
from django.contrib.auth.decorators import login_required

class PostDetail(generic.DetailView):
    model = Blog
    template_name = 'user/post_page.html'

@login_required(login_url='/user/login/')
def PostList(request):
	context = {}
	user = CustomUser.objects.filter()[:1].get()
	queryset = Blog.objects.filter(status=1).order_by('-created_on')
	context['user'] = user
	context['query'] = queryset

	return render(request, "user/post_detail.html", context)

def login_page(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		return redirect("loggedInUser")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("login")
	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "user/login.html", context)

@login_required(login_url='/user/login/')
def loggedInUser(request):
	user = CustomUser.objects.filter()[:1].get()
	context = {'user' : user}
	return render(request, 'user/dashboard.html', context)

def logout_view(request):
	logout(request)
	return redirect('login')