# -*- coding:utf-8 -*-
from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator
from blog.models import BlogPost, BlogComment, POST_TYPE
from blog.forms import CommentForm


def blog_archive_view(request):
	type = request.GET.get('type', '')
	if type:
		posts_list = BlogPost.objects.filter(type=type)
	else:
		posts_list = BlogPost.objects.all()

	pages = Paginator(posts_list, 5)
	page = int(request.GET.get('page', '1'))
	try:
		page_list = pages.page(page)
	except (EmptyPage, InvalidPage):
		page_list = pages.page(paginator.num_pages)

	t = loader.get_template("blog_archive.html")
	c = Context(
		{'posts': page_list}
	)
	return HttpResponse(t.render(c))


def blog_detail_view(request, id=''):
	try:
		post = BlogPost.objects.get(id=int(id))
	except BlogPost.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save_comment(post)

	form = CommentForm()
	comments = post.blogcomment_set.all()
	t = loader.get_template("blog_detail.html")
	c = RequestContext(request, {'post': post})
	c['comments'] = comments
	c['form'] = form
	return HttpResponse(t.render(c))

