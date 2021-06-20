from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Tag(models.Model):
    name = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg',upload_to='pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    tags = models.ManyToManyField(Tag)


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Latest_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Recent_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


## It News Model


class It_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg',upload_to='it_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='it_posts')

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('it-post-detail', kwargs={'pk': self.pk})



class It_Latest_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='it_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class It_Trending_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='it_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class It_Recent_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='it_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



# Business Model

class Business_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg',upload_to='business_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='business_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('business-post-detail', kwargs={'pk': self.pk})



class Business_Latest_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg', upload_to='business_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Business_Trending_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg' ,upload_to='business_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class Business_Recent_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='business_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





# Sport Model

class Sport_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg', upload_to='sport_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='sport_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('sport-post-detail', kwargs={'pk': self.pk})




class Sport_Latest_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='sport_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Sport_Trending_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='sport_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class Sport_Recent_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='sport_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





# Travel Model

class Travel_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(default='default.jpg' ,upload_to='travel_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='travel_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('travel-post-detail', kwargs={'pk': self.pk})




class Travel_Latest_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='travel_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Travel_Trending_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='travel_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class Travel_Recent_Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='travel_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Comments


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username



class ItComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('It_Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username



class BusinessComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Business_Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username



class SportComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Sport_Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username



class TravelComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Travel_Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username

