from django.shortcuts import render

posts = [
	{
		'author': 'Brett Stenerson',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 1st, 2018'
	},
	{
		'author': 'Brett Stenerson',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 1st, 2018'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
