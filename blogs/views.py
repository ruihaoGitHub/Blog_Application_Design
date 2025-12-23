from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import BlogPost
from .forms import BlogPostForm


def index(request):
	"""The home page for Blog."""
	query = request.GET.get('q')
	sort_by = request.GET.get('sort', '-date_added')
	author_filter = request.GET.get('author')

	post_list = BlogPost.objects.all()

	if author_filter:
		post_list = post_list.filter(owner__username=author_filter)

	if query:
		post_list = post_list.filter(models.Q(title__icontains=query) | models.Q(text__icontains=query))
	
	# Validate sort option
	if sort_by not in ['date_added', '-date_added', 'title', '-title']:
		sort_by = '-date_added'
	
	post_list = post_list.order_by(sort_by)

	paginator = Paginator(post_list, 5)  # 每页 5 篇
	page_number = request.GET.get('page')
	posts = paginator.get_page(page_number)
	
	context = {
		'posts': posts,
		'current_sort': sort_by,
		'current_author': author_filter,
		'query': query
	}
	return render(request, 'blogs/index.html', context)


def post_detail(request, post_id):
    """Show a single post in detail."""
    post = get_object_or_404(BlogPost, id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post_detail.html', context)


def signup(request):
	"""Allow users to register for an account."""
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			messages.success(request, 'Account created and logged in as {}'.format(new_user.username))
			return redirect('blogs:index')

	context = {'form': form}
	return render(request, 'registration/signup.html', context)


@login_required
def delete_post(request, post_id):
	"""Delete a post after confirming ownership."""
	post = get_object_or_404(BlogPost, id=post_id)
	if post.owner != request.user:
		raise Http404

	if request.method == 'POST':
		post.delete()
		messages.success(request, 'Post deleted.')
		return redirect('blogs:index')

	context = {'post': post}
	return render(request, 'blogs/confirm_delete.html', context)


@login_required
def new_post(request):
	"""Add a new post."""
	if request.method != 'POST':
		form = BlogPostForm()
	else:
		form = BlogPostForm(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			messages.success(request, 'Post created successfully.')
			return redirect('blogs:index')

	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
	"""Edit an existing post."""
	post = get_object_or_404(BlogPost, id=post_id)
	if post.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = BlogPostForm(instance=post)
	else:
		form = BlogPostForm(instance=post, data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Post updated successfully.')
			return redirect('blogs:index')

	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)
