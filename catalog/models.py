from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(null=True)          
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)
    home_image = models.ImageField(upload_to="Post_home",null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Images(models.Model):    
    post = models.ForeignKey(Post,models.CASCADE) 
    image = models.ImageField(upload_to="Post",null=True,blank=True)
    

    def __str__(self):
        return f"{self.post}"
    
    def save(self,*args, **kwargs):
        self.slug =slugify(self.image)
        super().save(*args, **kwargs)
    
    




    



    
    


