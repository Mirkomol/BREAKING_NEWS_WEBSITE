from django.core.mail import send_mail
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,)
from hitcount.views import HitCountDetailView
from .filters import *

from .forms import *

from .models import *



# Likeview
def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post-detail' , args=[str(pk)]))

def ItLikeView(request,pk):
    post = get_object_or_404(It_Post, id=request.POST.get('it_post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('it-post-detail' , args=[str(pk)]))


def BusinessLikeView(request,pk):
    post = get_object_or_404(Business_Post, id=request.POST.get('business_post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('business-post-detail' , args=[str(pk)]))


def SportLikeView(request,pk):
    post = get_object_or_404(Sport_Post, id=request.POST.get('sport_post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('sport-post-detail' , args=[str(pk)]))


def TravelLikeView(request, pk):
    post = get_object_or_404(Travel_Post, id=request.POST.get('travel_post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('travel-post-detail' , args=[str(pk)]))


# HOME

class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    extra_context = {'latest_posts': Latest_Post.objects.all(),
                     'recent_posts': Recent_Post.objects.all(),
                    }

    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SearchFilter(self.request.GET, queryset=self.get_queryset())
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    count_hit = True

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post-detail", kwargs={'pk':post.pk}))

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content',]
    template_name='post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', ]
    template_name = 'post_form.html'

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
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#It

class ItListView(ListView):
    model = It_Post
    template_name = 'magazine.html'
    context_object_name = 'it_post'
    extra_context = {'it_latest_post': It_Latest_Post.objects.all(),
                  'it_recent_post': It_Recent_Post.objects.all(),
                  'it_trending_post': It_Trending_Post.objects.all()}

    ordering = ['-date_posted']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ItSearchFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ItUserPostListView(ListView):
    model = It_Post
    template_name = 'it/it_user_posts.html'
    context_object_name = 'it_post'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return It_Post.objects.filter(author=user).order_by('-date_posted')


class ItPostDetailView(HitCountDetailView):
    model = It_Post
    template_name = 'it/it_post_detail.html'
    count_hit = True

    form = ItCommentForm

    def post(self, request, *args, **kwargs):
        form = ItCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("it-post-detail", kwargs={'pk': post.pk}))

    def get_context_data(self, **kwargs):
        post_comments_count = ItComment.objects.all().filter(post=self.object.id).count()
        post_comments = ItComment.objects.all().filter(post=self.object.id)

        stuff = get_object_or_404(It_Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context




class ItCreateView(LoginRequiredMixin, CreateView):
    model = It_Post
    fields = ['title', 'content', ]
    template_name='it/it_post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ItUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = It_Post
    fields = ['title', 'content', ]
    template_name = 'it/it_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ItDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = It_Post
    success_url = '/'
    template_name = 'it/it_post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




# Business

class BusinessPostListView(ListView):
    model = Business_Post
    template_name = 'business.html'
    context_object_name = 'business_post'
    extra_context = {'business_latest_post': Business_Latest_Post.objects.all(),
                  'business_recent_post': Business_Recent_Post.objects.all(),
                  'business_trending_post': Business_Trending_Post.objects.all()}

    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BusinessSearchFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BusinessUserPostListView(ListView):
    model = Business_Post
    template_name = 'business/business_user_posts.html'
    context_object_name = 'business_post'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Business_Post.objects.filter(author=user).order_by('-date_posted')


class BusinessPostDetailView(HitCountDetailView):
    model = Business_Post
    template_name = 'business/business_post_detail.html'
    count_hit = True

    form = BusinessCommentForm

    def post(self, request, *args, **kwargs):
        form = BusinessCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("business-post-detail", kwargs={'pk': post.pk}))

    def get_context_data(self, **kwargs):
        post_comments_count = BusinessComment.objects.all().filter(post=self.object.id).count()
        post_comments = BusinessComment.objects.all().filter(post=self.object.id)


        stuff = get_object_or_404(Business_Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context



class BusinessPostCreateView(LoginRequiredMixin, CreateView):
    model = Business_Post
    fields = ['title', 'content', ]
    template_name ='business/business_post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BusinessPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Business_Post
    fields = ['title', 'content', ]
    template_name = 'business/business_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BusinessPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business_Post
    success_url = '/'
    template_name = 'business/business_post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Sports

class SportPostListView(ListView):
    model = Sport_Post
    template_name = 'sports.html'
    context_object_name = 'sport_post'
    extra_context = {'sport_latest_post': Sport_Latest_Post.objects.all(),
                        'sport_recent_post': Sport_Recent_Post.objects.all(),
                        'sport_trending_post': Sport_Trending_Post.objects.all()}


    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SportSearchFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SportUserPostListView(ListView):
    model = Sport_Post
    template_name = 'sport/sport_user_posts.html'
    context_object_name = 'sport_post'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Sport_Post.objects.filter(author=user).order_by('-date_posted')


class SportPostDetailView(HitCountDetailView):
    model = Sport_Post
    template_name = 'sport/sport_post_detail.html'
    count_hit = True

    form = SportCommentForm

    def post(self, request, *args, **kwargs):
        form = SportCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("sport-post-detail", kwargs={'pk': post.pk}))

    def get_context_data(self, **kwargs):
        post_comments_count = SportComment.objects.all().filter(post=self.object.id).count()
        post_comments = SportComment.objects.all().filter(post=self.object.id)


        stuff = get_object_or_404(Sport_Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()


        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context

class SportPostCreateView(LoginRequiredMixin, CreateView):
    model = Sport_Post
    fields = ['title', 'content', ]
    template_name ='sport/sport_post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SportPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sport_Post
    fields = ['title', 'content', ]
    template_name = 'sport/sport_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SportPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sport_Post
    success_url = '/'
    template_name = 'sport/sport_post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# Travel

class TravelPostListView(ListView):
    model = Travel_Post
    template_name = 'travel.html'
    context_object_name = 'travel_post'
    extra_context = {'travel_latest_post': Travel_Latest_Post.objects.all(),
                        'travel_recent_post': Travel_Recent_Post.objects.all(),
                        'travel_trending_post': Travel_Trending_Post.objects.all()}


    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TravelSearchFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TravelUserPostListView(ListView):
    model = Travel_Post
    template_name = 'travel/travel_user_posts.html'
    context_object_name = 'travel_post'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Travel_Post.objects.filter(author=user).order_by('-date_posted')


class TravelPostDetailView(HitCountDetailView):
    model = Travel_Post
    template_name = 'travel/travel_post_detail.html'
    count_hit = True


    form = TravelCommentForm

    def post(self, request, *args, **kwargs):
        form = TravelCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("travel-post-detail", kwargs={'pk': post.pk}))

    def get_context_data(self, **kwargs):
        post_comments_count = TravelComment.objects.all().filter(post=self.object.id).count()
        post_comments = TravelComment.objects.all().filter(post=self.object.id)


        stuff = get_object_or_404(Travel_Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()


        context = super().get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context




class TravelPostCreateView(LoginRequiredMixin, CreateView):
    model = Travel_Post
    fields = ['title', 'content', ]
    template_name ='travel/travel_post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TravelPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Travel_Post
    fields = ['title', 'content', ]
    template_name = 'travel/travel_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TravelPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Travel_Post
    success_url = '/'
    template_name = 'travel/travel_post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




# Contact and About

def contact(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        firstname = request.POST['firstname']
        emailo = request.POST['emailo']

        # send an email
        send_mail(
            'firstname', # subject
            'comment' , # message
             'emailo',  # from email
            ['rakmircraffers@gmail.com'],  # To email
        )


        return render(request,'contactus.html', {'firstname':firstname})

    else:
        return render(request, 'contactus.html')


def aboutus(request):
    context = {'travel_recent_post':Travel_Recent_Post.objects.all(), }

    return render(request,'aboutus.html' , context)
