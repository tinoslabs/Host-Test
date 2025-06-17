
from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.conf import settings 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import ChatMessage
from django.utils import timezone

from .models import ClientReview, ContactModel, ProjectModel, TeamModel,  Certificates, Career_Model, Candidate, Team_Category, Team_Details, Client_Logo, Expertised_Technologies, Blog_Category, Blog_Details, Event, EventEnquiry
from .models import Service_Model

from .forms import ClientReviewForm, ContactModelForm, ProjectModelForm, TeamModelForm, CertificatesForm, CareerForm, CandidateForm, Team_Category_Form, Team_Details_Form, Expertised_Technologies, Client_Logo_Form, Expertised_Technology_Form, Blog_Category_Form,Blog_Category_Form,Blog_Details_Form,EventForm,EnquiryForm
from .forms import Service_Form

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, ("Invalid username or password. Please try again...."))
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

@login_required(login_url='user_login')
def admin_dashboard(request):
    return render(request,'admin_pages/admin_dashboard.html')

from django.contrib import messages

def index(request):
    clients_review = ClientReview.objects.all()
    team = Team_Category.objects.all()
    client_logo = Client_Logo.objects.all()
    technologies = Expertised_Technologies.objects.all()
    
    if request.method == 'POST':
        id1 = request.POST.get('id1')
        pdf_url = generate_certificate_url(id1)
        if pdf_url:
            return render(request, 'certificate.html', {'pdf_url': pdf_url})
        else:
            messages.error(request, ("Certificate not found for the provided ID!!!"))
            return redirect('index')
    else:
        team_heading = "Your Team Heading"  
        if Team_Category.objects.filter(team_heading=team_heading, status=0).exists():
            team_details = Team_Details.objects.filter(category__team_heading=team_heading)
            category_name = Team_Category.objects.filter(team_heading=team_heading).first()
            context = {'team_details': team_details, 'category_name': category_name, 'team': team, 'clients_review': clients_review}
            return render(request, "index.html", context)
        else:
            
            return render(request, 'index.html', {'clients_review': clients_review,'team':team,'client_logo':client_logo,'technologies':technologies})

# ADMIN SECTION START  

from django.http import JsonResponse
from .models import ChatMessage

@login_required(login_url='user_login')
def chatbot_message_view(request):
    chatbot = ChatMessage.objects.all().order_by('-id')
    return render(request,'admin_pages/chatbot_message_view.html',{'chatbot':chatbot})

@login_required(login_url='user_login')
def delete_message(request,id):
    chatbot = ChatMessage.objects.get(id=id)
    chatbot.delete()
    return redirect('chatbot_message_view')

@login_required(login_url='user_login')
def add_client_reviews(request):
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientReviewForm()

    return render(request, 'admin_pages/add_client_reviews.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_client_reviews(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientReviewForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_reviews.html', {'form': form, 'client_reviews': client_reviews})
 

@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')


@login_required(login_url='user_login')
def contact_list(request):
    contact = ContactModel.objects.all().order_by('-id')
    return render(request,'admin_pages/contact_list.html',{'contact':contact})


@login_required(login_url='user_login')
def delete_contact(request,id):
    contact = ContactModel.objects.get(id=id)
    contact.delete()
    return redirect('contact_list')

@login_required(login_url='user_login')
def enquiry_list(request):
    data = EventEnquiry.objects.all().order_by('-id')
    return render(request,'admin_pages/enquiry_list.html',{'data':data})


@login_required(login_url='user_login')
def delete_enquiry(request,id):
    data = EventEnquiry.objects.get(id=id)
    data.delete()
    return redirect('enquiry_list')


@login_required(login_url='user_login')
def add_project(request):
    if request.method == 'POST':
        form = ProjectModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_projects') 
    else:
        form = ProjectModelForm()

    return render(request, 'admin_pages/add_project.html', {'form': form})

@login_required(login_url='user_login')
def view_projects(request):
    projects = ProjectModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_projects.html', {'projects': projects})

@login_required(login_url='user_login')
def update_projects(request, id):
    projects = get_object_or_404(ProjectModel, id=id)
    if request.method == 'POST':
        form = ProjectModelForm(request.POST, request.FILES, instance=projects)
        if form.is_valid():
            if 'remove_image' in request.POST:
                projects.project_image.delete() 
                projects.project_image = None 
            form.save()
            return redirect('view_projects')
    else:
        form = ProjectModelForm(instance=projects)
    return render(request, 'admin_pages/update_projects.html', {'form': form, 'projects': projects})

@login_required(login_url='user_login')
def delete_projects(request,id):
    projects = ProjectModel.objects.get(id=id)
    projects.delete()
    return redirect('view_projects')



@login_required(login_url='user_login')
def add_teams(request):
    if request.method == 'POST':
        form = TeamModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_teams') 
    else:
        form = TeamModelForm()

    return render(request, 'admin_pages/add_teams.html', {'form': form})

@login_required(login_url='user_login')
def view_teams(request):
    teams = TeamModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_teams.html', {'teams': teams})



@login_required(login_url='user_login')
def update_teams(request,id):
    teams = get_object_or_404(TeamModel, id=id)
    if request.method == 'POST':
        form = TeamModelForm(request.POST, request.FILES, instance=teams)
        if form.is_valid():
            form.save()
            return redirect('view_teams')
    else:
        form = TeamModelForm(instance=teams)
    return render(request, 'admin_pages/update_teams.html', {'form': form, 'teams': teams})


@login_required(login_url='user_login')
def delete_teams(request,id):
    teams = TeamModel.objects.get(id=id)
    teams.delete()
    return redirect('view_teams')

@login_required(login_url='user_login')
def add_certificates(request):
    if request.method == 'POST':
        form = CertificatesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_certificates') 
    else:
        form = CertificatesForm()

    return render(request, 'admin_pages/add_certificates.html', {'form': form})

@login_required(login_url='user_login')
def view_certificates(request):
    certificates = Certificates.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_certificates.html', {'certificates': certificates})


@login_required(login_url='user_login')
def update_certificates(request,id):
    certificates = get_object_or_404(Certificates, id=id)
    if request.method == 'POST':
        form = CertificatesForm(request.POST, request.FILES, instance=certificates)
        if form.is_valid():
            form.save()
            return redirect('view_certificates')
    else:
        form = TeamModelForm(instance=certificates)
    return render(request, 'admin_pages/update_certificates.html', {'form': form, 'certificates': certificates})


@login_required(login_url='user_login')
def delete_certificates(request,id):
    certificates = Certificates.objects.get(id=id)
    certificates.delete()
    return redirect('view_certificates')

@login_required(login_url='user_login')
def add_job_details(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_job_details') 
    else:
        form = CareerForm()

    return render(request, 'admin_pages/add_job_details.html', {'form': form})

@login_required(login_url='user_login')
def view_job_details(request):
    job_details = Career_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_job_details.html', {'job_details': job_details})

@login_required(login_url='user_login')
def update_job_details(request, id):
    job_details = get_object_or_404(Career_Model, id=id)
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES, instance=job_details)
        if form.is_valid():
            form.save()
            return redirect('view_job_details')
    else:
        form = CareerForm(instance=job_details)
    return render(request, 'admin_pages/update_job_details.html', {'form': form, 'job_details': job_details})


@login_required(login_url='user_login')
def delete_job_details(request,id):
    job_details = Career_Model.objects.get(id=id)
    job_details.delete()
    return redirect('view_job_details')



@login_required(login_url='user_login')
def view_candidate_details(request):
    certificates = Candidate.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_candidate_certificates.html', {'certificates': certificates})


@login_required(login_url='user_login')
def delete_candidate_certificates(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    candidate.delete()
    return redirect('view_candidate_details')

@login_required(login_url='user_login')
def add_team_category(request):
    if request.method == 'POST':
        form = Team_Category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_team_details') 
    else:
        form = Team_Category_Form()

    return render(request, 'admin_pages/add_team_category.html', {'form': form})

@login_required(login_url='user_login')
def view_team_category(request):
    team_category = Team_Category.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_team_category.html', {'team_category': team_category})


@login_required(login_url='user_login')
def update_team_category(request, id):
    team_category = get_object_or_404(Team_Category, id=id)
    if request.method == 'POST':
        form = Team_Category_Form(request.POST, request.FILES, instance=team_category)
        if form.is_valid():
            form.save()
            return redirect('view_team_category')
    else:
        form = Team_Category_Form(instance=team_category)
    return render(request, 'admin_pages/update_team_category.html', {'form': form, 'team_category': team_category})


@login_required(login_url='user_login')
def delete_team_category(request,id):
    team_category = Team_Category.objects.get(id=id)
    team_category.delete()
    return redirect('view_team_category')


@login_required(login_url='user_login')
def add_team_details(request):
    if request.method == 'POST':
        team_details = Team_Details_Form(request.POST, request.FILES)
        if team_details.is_valid():
            team_details.save()
            return redirect('admin_view_team_details')  
    else:
        team_details = Team_Details_Form()

    categories = Team_Category.objects.all() 
    return render(request, 'admin_pages/add_team_details.html', {'team_details': team_details,'categories':categories})

@login_required(login_url='user_login')
def admin_view_team_details(request):
    team = Team_Details.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_team_details.html',{'team':team})

@login_required(login_url='user_login')
def update_team_details(request, id):
    team_details = get_object_or_404(Team_Details, id=id)
    if request.method == 'POST':
        form = Team_Details_Form(request.POST, request.FILES, instance=team_details)
        if form.is_valid():
            form.save()
            return redirect('admin_view_team_details')
    else:
        form = Team_Details_Form(instance=team_details)
        categories = Team_Category.objects.all()
    return render(request, 'admin_pages/update_team_details.html', {'form': form, 'team_details': team_details,'categories':categories})


@login_required(login_url='user_login')
def delete_team_details(request,id):
    team_details = Team_Details.objects.get(id=id)
    team_details.delete()
    return redirect('admin_view_team_details')

@login_required(login_url='user_login')
def add_technologies(request):
    if request.method == 'POST':
        form = Expertised_Technology_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_technologies') 
    else:
        form = Expertised_Technology_Form()

    return render(request, 'admin_pages/add_technologies.html', {'form': form})


@login_required(login_url='user_login')
def view_technologies(request):
    technologies = Expertised_Technologies.objects.all().order_by('-id')
    return render(request,'admin_pages/view_technologies.html',{'technologies':technologies})

@login_required(login_url='user_login')
def update_technologies(request,id):
    logos = get_object_or_404(Expertised_Technologies, id=id)
    if request.method == 'POST':
        form = Expertised_Technology_Form(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_technologies')
    else:
        form = Expertised_Technology_Form(instance=logos)
    return render(request, 'admin_pages/update_technologies.html', {'form': form, 'logos': logos})


@login_required(login_url='user_login')
def delete_technologies(request,id):
    logos = Expertised_Technologies.objects.get(id=id)
    logos.delete()
    return redirect('view_technologies')


@login_required(login_url='user_login')
def add_clients_logo(request):
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo') 
    else:
        form = Client_Logo_Form()

    return render(request, 'admin_pages/add_clients_logo.html', {'form': form})

@login_required(login_url='user_login')
def view_clients_logo(request):
    logo = Client_Logo.objects.all().order_by('-id')
    return render(request,'admin_pages/view_clients_logo.html',{'logo':logo})

@login_required(login_url='user_login')
def update_clients_logo(request,id):
    logos = get_object_or_404(Client_Logo, id=id)
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo')
    else:
        form = Client_Logo_Form(instance=logos)
    return render(request, 'admin_pages/update_clients_logo.html', {'form': form, 'logos': logos})

@login_required(login_url='user_login')
def delete_clients_logo(request,id):
    logos = Client_Logo.objects.get(id=id)
    logos.delete()
    return redirect('view_clients_logo')

@login_required(login_url='user_login')
def add_blog_category(request):
    if request.method == 'POST':
        form = Blog_Category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_blog_details') 
    else:
        form = Blog_Category_Form()

    return render(request, 'admin_pages/add_blog_category.html', {'form': form})

@login_required(login_url='user_login')
def view_blog_category(request):
    blog_category = Blog_Category.objects.all().order_by('-id')
    return render(request,'admin_pages/view_blog_category.html',{'blog_category':blog_category})

@login_required(login_url='user_login')
def update_blog_category(request,id):
    blog_category = get_object_or_404(Blog_Category, id=id)
    if request.method == 'POST':
        form = Blog_Category_Form(request.POST, request.FILES, instance=blog_category)
        if form.is_valid():
            form.save()
            return redirect('view_blog_category')
    else:
        form = Blog_Category_Form(instance=blog_category)
    return render(request, 'admin_pages/update_blog_category.html', {'form': form, 'blog_category': blog_category})

@login_required(login_url='user_login')
def delete_blog_category(request,id):
    blog_category = Blog_Category.objects.get(id=id)
    blog_category.delete()
    return redirect('view_blog_category')


@login_required(login_url='user_login')
def add_blog_details(request):
    categories = Blog_Category.objects.all() 
    if request.method == 'POST':
        blog_details = Blog_Details_Form(request.POST, request.FILES)
        if blog_details.is_valid():
            blog_details.save()
            return redirect('view_blog_details')  
    else:
        blog_details = Blog_Details_Form()

    
    return render(request, 'admin_pages/add_blog_details.html', {'blog_details': blog_details,'categories':categories})



@login_required(login_url='user_login')
def view_blog_details(request):
    blog_details = Blog_Details.objects.all().order_by('-id')
    return render(request,'admin_pages/view_blog_details.html',{'blog_details':blog_details})

@login_required(login_url='user_login')
def update_blog_details(request, id):
    blog_details = get_object_or_404(Blog_Details, id=id)
    if request.method == 'POST':
        form = Blog_Details_Form(request.POST, request.FILES, instance=blog_details)
        if form.is_valid():
            form.save()
            return redirect('view_blog_details')
    else:
        form = Blog_Details_Form(instance=blog_details)
        categories = Blog_Category.objects.all()
    return render(request, 'admin_pages/update_blog_details.html', {'form': form, 'blog_details': blog_details,'categories':categories})

@login_required(login_url='user_login')
def delete_blog_details(request,id):
    blog_details = Blog_Details.objects.get(id=id)
    blog_details.delete()
    return redirect('view_blog_details')


@login_required(login_url='user_login')
def add_servieces(request):
    if request.method == 'POST':
        form = Service_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_servieces') 
    else:
        form = Service_Form()

    return render(request, 'admin_pages/add_servieces.html', {'form': form})


@login_required(login_url='user_login')
def view_servieces(request):
    servieces = Service_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_servieces.html', {'servieces': servieces})


@login_required(login_url='user_login')
def update_servieces(request, id):
    servieces = get_object_or_404(Service_Model, id=id)
    if request.method == 'POST':
        form = Service_Form(request.POST, request.FILES, instance=servieces)
        if form.is_valid():
            form.save()
            return redirect('view_servieces')
    else:
        form = Service_Form(instance=servieces)

    # Define your service options
    service_options = [
        ("Cyber Security", "Cyber Security"),
        ("Software Development", "Software Development"),
        ("Artificial Intelligence", "Artificial Intelligence"),
        ("Drone Development", "Drone Development"),
        ("Erp Development", "Erp Development"),
        ("Flange Management", "Flange Management"),
        ("Robotics", "Robotics"),
        ("Automation", "Automation"),
        ("CRM Development", "CRM Development"),
        ("Web Development", "Web Development"),
        ("Android Application", "Android Application"),
        ("Ios Application", "Ios Application"),
        ("Ui/Ux", "Ui/Ux"),
    ]

    # Pass the current service name to the template
    current_service_name = servieces.service_name  # Assuming 'service_name' is the field name

    return render(request, 'admin_pages/update_servieces.html', {'form': form, 'servieces': servieces, 'service_options': service_options, 'current_service_name': current_service_name})

@login_required(login_url='user_login')
def delete_serviece(request,id):
    servieces = Service_Model.objects.get(id=id)
    servieces.delete()
    return redirect('view_servieces')
# ADMIN SECTION END 

def verification(request):
    if request.method == 'POST':
        id1 = request.POST.get('id1')
        pdf_url = generate_certificate_url(id1)
        if pdf_url:
            return render(request, 'certificate.html', {'pdf_url': pdf_url})
        else:
            # return render(request, 'error.html', {'message': 'Certificate not found.'})
            error_message = 'Certificate not found for the provided ID.'
            return render(request, 'verification.html', {'error_message': error_message})
    else:
        return render(request, 'verification.html')


def submit_query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and phone_number and email and message:
            # Save the data to the ChatMessage model
            ChatMessage.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                message=message
            )
            return JsonResponse({'message': 'Data saved successfully'}, status=200)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)


def home(request):
    clients_review = ClientReview.objects.all()
    if request.method == 'POST':
        id1 = request.POST.get('id1')
        pdf_url = generate_certificate_url(id1)
        if pdf_url:
            return render(request, 'certificate.html', {'pdf_url': pdf_url})
        else:
            return render(request, 'error.html', {'message': 'Certificate not found.'})
    else:
        return render(request,'index-3.html', {'clients_review': clients_review})


def generate_certificate_url(id):
    try:
        certificate = Certificates.objects.get(id1=id)
        return f'{settings.MEDIA_URL}{certificate.pdf_file}'
    except Certificates.DoesNotExist:
        return None


def project(request):
    review = ClientReview.objects.all()
    project = ProjectModel.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ContactModelForm()
    return render(request,'project.html',{'form':form,'project':project,'review':review})



def dashboard(request):
    return render(request,'admin_pages/dashboard.html')

def Cybersecurity(request):
    youtube_video = Service_Model.objects.all()
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    return render(request,'cybersecurity/cybersecurity.html',{'project':project,'review':review,'youtube_video':youtube_video})
    
def web_development(request):
    youtube_video = Service_Model.objects.filter(service_name='Web Development')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ContactModelForm()
    return render(request,'web_development.html',{'project':project,'review':review,'form':form,'youtube_video':youtube_video})


def web_design(request):
    youtube_video = Service_Model.objects.filter(service_name='Web Design')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ContactModelForm()
    return render(request,'web_design.html',{'project':project,'review':review,'form':form,'youtube_video':youtube_video})

def ui_ux_design(request):
    youtube_video = Service_Model.objects.filter(service_name='Ui/Ux Design')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ContactModelForm()
    return render(request,'ui_ux_design.html',{'project':project,'review':review,'form':form,'youtube_video':youtube_video})

def data_science(request):
    youtube_video = Service_Model.objects.filter(service_name='Data Science')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ContactModelForm()
    return render(request,'data_science.html',{'project':project,'review':review,'data_science':data_science,'youtube_video':youtube_video})


def digital_marketing(request):
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('digital_marketing')
    else:
        form = ContactModelForm()
    return render(request, 'digital-marketing/digital-marketing.html', {'form': form,'project':project,'review':review})


def software_development(request):
    youtube_video = Service_Model.objects.filter(service_name='Software Development')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('software_development')
    else:
        form = ContactModelForm()
    return render(request,'software-development/software-development.html',{'project':project,'review':review,'youtube_video':youtube_video,'form':form})

def Artificial_intelligence(request):
    youtube_video = Service_Model.objects.filter(service_name='Artificial Intelligence')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'artificial_intelligence.html',{'project':project,'review':review,'youtube_video':youtube_video,'form':form})

def ios_application(request):
    youtube_video = Service_Model.objects.filter(service_name='Ios Application')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'ios_application.html',{'project':project,'review':review,'youtube_video':youtube_video,'form':form})

def android_application(request):
    youtube_video = Service_Model.objects.filter(service_name='Android Application')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'android_application.html',{'project':project,'review':review,'youtube_video':youtube_video,'form':form})

def Artificial_intelligence(request):
    youtube_video = Service_Model.objects.filter(service_name='Artificial Intelligence')
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'artificial_intelligence.html',{'project':project,'review':review,'youtube_video':youtube_video,'form':form})

def cloud_services(request):
    # youtube_video = Cloud_Services.objects.all()
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'cloud_services.html',{'project':project,'review':review,'form':form})

def domain_services(request):
    # youtube_video = Domain_Services.objects.all()
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'domain_services.html',{'project':project,'review':review,'form':form})

def business_email(request):
    # youtube_video = Business_Email.objects.all()
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artificial_intelligence')
    else:
        form = ContactModelForm()
    return render(request,'business_email.html',{'project':project,'review':review,'form':form})

def contact(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to a success page or confirmation message
    else:
        form = ContactModelForm()
    return render(request,'contact.html',{'form': form})

def data_analysis(request):
    youtube_video = Service_Model.objects.all()
    project = ProjectModel.objects.all()
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_analysis')
    else:
        form = ContactModelForm()
    return render(request,'data_analysis.html',{'form': form,'project':project,'review':review,'youtube_video':youtube_video})


def career(request):
    review = ClientReview.objects.all()
    jobs = Career_Model.objects.filter(post_end_date__gte=timezone.now())
    return render(request,'career.html',{'jobs':jobs,'review':review})

def job_details(request,job_position):
    job_details = get_object_or_404(Career_Model, job_position=job_position)
    return render(request,'job-details.html',{'job_details':job_details})

def apply_jobs(request):
    job_positions = Career_Model.objects.all()
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('apply_jobs')
           
    else:
        form = CandidateForm()

    return render(request, 'job_apply.html', {'form': form,'job_positions':job_positions})


def test(request):
    return render(request,'test.html')

# PREMIUM SERVICE SECTION

def premium_services(request):
    return render(request,'premium-services.html')

def automation(request):
    youtube_video = Service_Model.objects.filter(service_name='Automation')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('automation')
    else:
        form = ContactModelForm()
    return render(request,'automation.html',{'form':form,'review':review,'youtube_video':youtube_video})


def crm_development(request):
    youtube_video = Service_Model.objects.filter(service_name='CRM Development')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_analysis')
    else:
        form = ContactModelForm()
    return render(request,'crm-development.html',{'form':form,'review':review,'youtube_video':youtube_video})


def drone_development(request):
    youtube_video = Service_Model.objects.filter(service_name='Drone Development')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drone_development')
    else:
        form = ContactModelForm()
    return render(request,'drone_development.html',{'form':form,'review':review,'youtube_video':youtube_video})

def ecommerce_solutions(request):
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce_solutions')
    else:
        form = ContactModelForm()
    return render(request,'ecommerce_solutions.html',{'form':form,'review':review})

def erp_development(request):
    youtube_video = Service_Model.objects.filter(service_name='Erp Development')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('erp_development')
    else:
        form = ContactModelForm()
    return render(request,'erp_development.html',{'form':form,'review':review,'youtube_video':youtube_video})

def flange_management(request):
    youtube_video = Service_Model.objects.filter(service_name='Flange Management')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flange_management')
    else:
        form = ContactModelForm()
    return render(request,'flange_management.html',{'form':form,'review':review,'youtube_video':youtube_video})

def robotics(request):
    youtube_video = Service_Model.objects.filter(service_name='Robotics')
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('robotics')
    else:
        form = ContactModelForm()
    return render(request,'robotics.html',{'form':form,'review':review,'youtube_video':youtube_video})

# end premium service

def blog(request):  
    review = ClientReview.objects.all()
    blog_category = Blog_Category.objects.filter(status=0)
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce_solutions')
    else:
        form = ContactModelForm()
    return render(request,'blog.html',{'blog_category':blog_category,'review':review,'form':form})



def blog_details(request, blog_heading):
    blog = Blog_Category.objects.all()
    category = get_object_or_404(Blog_Category, blog_heading=blog_heading, status=False)
    if category:
        blog_details = Blog_Details.objects.filter(category=category, status=False)
        context = {'blog_details': blog_details, 'category_name': category,'blog':blog}
        return render(request, "blog_details.html", context)
    else:
        messages.warning(request, "No such category found")
        return render(request, 'blog_details.html')
    

def index_two(request):
    return render(request,'index-2.html')

def service(request):
    review = ClientReview.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ContactModelForm()
    return render(request,'services.html',{'service':service,'review':review,'form':form})

def team(request):
    team = TeamModel.objects.all()
    return render(request,'team.html',{'team':team})

def portfolio(request):
    return render(request,'portfolio.html')

def testimonial(request):
    review = ClientReview.objects.all()
    return render(request,'testimonial.html',{'review':review})

def terms_and_conditions(request):
    return render(request,'terms_and_conditions.html')


def privacy_policy(request):
    return render(request,'privacy_policy.html')

def project_view(request):
    return render(request,'admin_pages/project_view.html')

def add_projects(request):
    return render(request,'admin_pages/add_projects.html')

def log(request):
    return render(request,'authenticate/log.html')


# def event(request):
#     if request.method == 'POST':
#         form = ContactModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')
#     else:
#         form = ContactModelForm()
#     event = Event.objects.all()
#     return render(request,'event.html',{'event':event,'form':form})

def event(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')  # Redirect to a success page or confirmation message
    else:
        form = EnquiryForm()
    event = Event.objects.all()
    return render(request, 'event.html', {'form': form,'event':event})




@login_required(login_url='user_login')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_event') 
    else:
        form = EventForm()

    return render(request, 'admin_pages/add_event.html', {'form': form})


@login_required(login_url='user_login')
def view_event(request):
    event = Event.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_event.html', {'event': event})


@login_required(login_url='user_login')
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('view_event')
    else:
        form = EventForm(instance=event)
    return render(request, 'admin_pages/update_event.html', {'form': form, 'event': event})

    
@login_required(login_url='user_login')
def delete_event(request,id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('view_event')


def event_enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or confirmation message
    else:
        form = EnquiryForm()
    return render(request,'event.html')
