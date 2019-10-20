from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import ImageForm, PostCreationForm
from .models import Post
from .models import Image
from plant.models import Plant

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context['plants'] = Plant.objects.all()
		return context

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		pk = self.kwargs['pk']
		currentPost = get_object_or_404(Post, id=pk)
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['images'] = Image.objects.filter(post=currentPost)
		return context

@login_required
def PostCreateView(request):

	ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

	if request.method == 'POST':
		postForm = PostCreationForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

		if postForm.is_valid() and formset.is_valid():
			post_form = postForm.save(commit=False)
			post_form.author = request.user
			post_form.save()

			for form in formset.cleaned_data:
				if form:
					image = form['image']
					photo = Image(post=post_form, image=image)
					photo.save()
			else:
				print(postForm.errors, formset.errors)
		messages.success(request, "Upload successful")
		return HttpResponseRedirect("/")
	else:
		postForm = PostCreationForm()
		formset = ImageFormSet(queryset=Image.objects.none())
	return render(request, 'blog/post_form.html', {'postForm': postForm, 'formset': formset})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name_suffix = '_update_form'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
