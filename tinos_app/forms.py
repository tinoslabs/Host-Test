from django import forms
from .models import ClientReview,ContactModel,ProjectModel,TeamModel,Certificates,Career_Model,Candidate,Team_Category,Team_Details,Client_Logo,Expertised_Technologies,Blog_Category,Blog_Details,Service_Model,Event,EventEnquiry
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = TeamModel
        fields = '__all__'

class CertificatesForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = '__all__'

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career_Model
        fields = '__all__'

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class Team_Category_Form(forms.ModelForm):
    class Meta:
        model = Team_Category
        fields = '__all__'

class Team_Details_Form(forms.ModelForm):
    class Meta:
        model = Team_Details
        fields = '__all__'

class Client_Logo_Form(forms.ModelForm):
    class Meta:
        model = Client_Logo
        fields = '__all__'

class Expertised_Technology_Form(forms.ModelForm):
    class Meta:
        model = Expertised_Technologies
        fields = '__all__'

class Blog_Category_Form(forms.ModelForm):
    class Meta:
        model = Blog_Category
        fields = '__all__'

class Blog_Details_Form(forms.ModelForm):
    class Meta:
        model = Blog_Details
        fields = '__all__'


class Service_Form(forms.ModelForm):
    class Meta:
        model = Service_Model
        fields = '__all__'
        
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = EventEnquiry
        fields = '__all__'