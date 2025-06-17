from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


class Team_Category(models.Model):
    team_heading = models.CharField(max_length=100)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.team_heading

class Team_Details(models.Model):
    category = models.ForeignKey(Team_Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=1000, null=True, blank=True)
    team_image = models.ImageField(upload_to='images/',null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    def __str__(self):
        return self.name
    


class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    review_video = models.FileField(upload_to='review_videos/', null=True, blank=True)
    def __str__(self):
        return f"{self.client_name} - {self.designation}"


class ContactModel(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ProjectModel(models.Model):
    project_name = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.CharField(max_length=200, null=True, blank=True)
    project_image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    def __str__(self):
        return self.project_name

class TeamModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)
    def __str__(self):
        return self.name if self.name else "Team Member"


class Certificates(models.Model):
    id1 = models.CharField(max_length=100)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')  
    def __str__(self):
        return f"{self.id1}"


class Career_Model(models.Model):    
    job_position = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    salary = models.IntegerField()
    job_details = RichTextField(max_length=20000)
    posted_date = models.DateField()
    end_date = models.DateField()
    post_end_date = models.DateTimeField()
    
    def is_active(self):
        return self.post_end_date >= timezone.now()



class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    job_position = models.ForeignKey(Career_Model, on_delete=models.CASCADE, related_name='candidates', null=True)
    
    def _str_(self):
        return self.name

class ChatMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Client_Logo(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name


class Expertised_Technologies(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
    


class Blog_Category(models.Model):
    category_name = models.CharField(max_length=100)
    blog_heading = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    main_image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.category_name

    
class Blog_Details(models.Model):
    category = models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    blog_description = RichTextField(max_length=60000)
    blog_image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.blog_description
    
class Service_Model(models.Model):
    service_name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.service_name
    
class Event(models.Model):
    
    description = models.TextField(null=True, blank=True)
    event_video = models.FileField(upload_to='event_videos/', null=True, blank=True)
    
    
    
class EventEnquiry(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'