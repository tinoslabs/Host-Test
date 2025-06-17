from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('portfolio',views.portfolio,name='portfolio'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('terms_and_conditions', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('home',views.home,name='home'),
    path('data_analysis',views.data_analysis,name='data_analysis'),

    path('project',views.project,name='project'),
    path('project_view',views.project_view,name='project_view'),
    path('add_projects',views.add_projects,name='add_projects'),
    path('dashboard',views.dashboard,name='dashboard'),

    path('service',views.service,name='service'),
    path('Cybersecurity',views.Cybersecurity,name='Cybersecurity'),
    path('digital_marketing',views.digital_marketing,name='digital_marketing'),
    path('software_development',views.software_development,name='software_development'),
    path('web_development',views.web_development,name='web_development'),
    path('web_design',views.web_design,name='web_design'),
    path('ui_ux_design',views.ui_ux_design,name='ui_ux_design'),
    path('data_science',views.data_science,name='data_science'),


    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('add_client_reviews',views.add_client_reviews,name='add_client_reviews'),
    path('view_client_reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update_client_reviews/<int:id>/',views.update_client_reviews,name='update_client_reviews'),
    path('delete_client_review/<int:id>/',views.delete_client_review,name='delete_client_review'),

    path('contact',views.contact,name='contact'),
    path('contact_list',views.contact_list,name='contact_list'),
    path('delete_contact/<int:id>/',views.delete_contact,name='delete_contact'),
    
    path('enquiry_list', views.enquiry_list, name='enquiry_list'),
    path('delete_enquiry/<int:id>/', views.delete_enquiry, name='delete_enquiry'),

    path('add_project',views.add_project,name='add_project'),
    path('view_projects',views.view_projects,name='view_projects'),
    path('update_projects/<int:id>/',views.update_projects,name='update_projects'),
    path('delete_projects/<int:id>/',views.delete_projects,name='delete_projects'),

    path('team',views.team,name='team'),
    path('add_teams',views.add_teams,name='add_teams'),
    path('view_teams',views.view_teams,name='view_teams'),
    path('update_teams/<int:id>/',views.update_teams,name='update_teams'),
    path('delete_teams/<int:id>/',views.delete_teams,name='delete_teams'),

    path('add_certificates',views.add_certificates,name='add_certificates'),
    path('view_certificates',views.view_certificates,name='view_certificates'),
    path('update_certificates/<int:id>/',views.update_certificates,name='update_certificates'),
    path('delete_certificates/<int:id>/',views.delete_certificates,name='delete_certificates'),
    path('verification',views.verification,name='verification'),
    path('view_candidate_details',views.view_candidate_details,name='view_candidate_details'),
    path('delete_candidate_certificates/<int:id>',views.delete_candidate_certificates,name='delete_candidate_certificates'),
    
    path('career',views.career,name='career'),
    path('add_job_details',views.add_job_details,name='add_job_details'),
    path('view_job_details',views.view_job_details,name='view_job_details'),
    path('update_job_details/<int:id>',views.update_job_details,name='update_job_details'),
    path('delete_job_details/<int:id>',views.delete_job_details,name='delete_job_details'),
    path('apply_jobs',views.apply_jobs,name='apply_jobs'),
    path('job_details/<str:job_position>/',views.job_details,name='job_details'),

    path('add_team_category',views.add_team_category,name='add_team_category'),
    path('view_team_category',views.view_team_category,name='view_team_category'),
    path('update_team_category/<int:id>/',views.update_team_category,name='update_team_category'),
    path('delete_team_category/<int:id>/',views.delete_team_category, name='delete_team_category'),

    
   path('add_team_details', views.add_team_details, name='add_team_details'),
   path('admin_view_team_details',views.admin_view_team_details,name='admin_view_team_details'),
   path('delete_team_details/<int:id>',views.delete_team_details,name='delete_team_details'),
   path('update_team_details/<int:id>/',views.update_team_details,name='update_team_details'),

   path('test',views.test,name='test'),
   
   path('premium_services',views.premium_services,name='premium_services'),
   path('automation',views.automation,name='automation'),
   path('crm_development',views.crm_development,name='crm_development'),
   path('drone_development',views.drone_development,name='drone_development'),
   path('ecommerce_solutions',views.ecommerce_solutions,name='ecommerce_solutions'),
   path('erp_development',views.erp_development,name='erp_development'),
   path('flange_management',views.flange_management,name='flange_management'),
   path('robotics',views.robotics,name='robotics'),

   path('submit_query/',views.submit_query, name='submit_query'),
   path('chatbot_message_view',views.chatbot_message_view,name='chatbot_message_view'),
   path('delete_message/<int:id>/',views.delete_message,name='delete_message'),

   path('add_clients_logo',views.add_clients_logo,name='add_clients_logo'),
   path('view_clients_logo',views.view_clients_logo,name='view_clients_logo'),
   path('update_clients_logo/<int:id>/',views.update_clients_logo,name='update_clients_logo'),
   path('delete_clients_logo/<int:id>/',views.delete_clients_logo,name='delete_clients_logo'),
   
   path('add_technologies',views.add_technologies,name='add_technologies'),
   path('view_technologies',views.view_technologies,name='view_technologies'),
   path('update_technologies/<int:id>/',views.update_technologies,name='update_technologies'),
   path('delete_technologies/<int:id>/',views.delete_technologies,name='delete_technologies'),

   path('add_blog_category',views.add_blog_category,name='add_blog_category'),
   path('view_blog_category',views.view_blog_category,name='view_blog_category'),
   path('update_blog_category/<int:id>/',views.update_blog_category,name='update_blog_category'),
   path('delete_blog_category/<int:id>/',views.delete_blog_category,name='delete_blog_category'),
   path('blog',views.blog,name='blog'),
   
   path('add_blog_details',views.add_blog_details,name='add_blog_details'),
   path('view_blog_details',views.view_blog_details,name='view_blog_details'),
   path('update_blog_details/<int:id>/',views.update_blog_details,name='update_blog_details'),
   path('delete_blog_details/<int:id>/',views.delete_blog_details,name='delete_blog_details'),
   path('blog_details/<str:blog_heading>/',views.blog_details,name='blog_details'),
   path('index_two',views.index_two,name='index_two'),
     
    path('log',views.log,name='log'),

    path('Artificial_intelligence',views.Artificial_intelligence,name='Artificial_intelligence'),
    path('ios_application',views.ios_application,name='ios_application'),
    path('android_application',views.android_application,name='android_application'),
    path('cloud_services',views.cloud_services,name='cloud_services'),
    path('domain_services',views.domain_services,name='domain_services'),
    path('business_email',views.business_email,name='business_email'),
     
    path('add_servieces',views.add_servieces,name='add_servieces'),
    path('view_servieces',views.view_servieces,name='view_servieces'),
    path('update_servieces/<int:id>/',views.update_servieces,name='update_servieces'),
    path('delete_serviece/<int:id>',views.delete_serviece,name='delete_serviece'),

     
    path('add_servieces',views.add_servieces,name='add_servieces'),
    path('view_servieces',views.view_servieces,name='view_servieces'),
    path('update_servieces/<int:id>/',views.update_servieces,name='update_servieces'),
    path('delete_serviece/<int:id>',views.delete_serviece,name='delete_serviece'),
    path('event', views.event, name='event'),
    
    path('add_event', views.add_event, name='add_event'),
    path('view_event', views.view_event, name='view_event'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
   




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)