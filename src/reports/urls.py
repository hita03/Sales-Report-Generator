from django.urls import path
from .views import create_report,ReportDetailView, ReportListView,render_pdf_view,UploadTemplateView,csv_upload_view

app_name = 'reports'

urlpatterns = [
    path('all/',ReportListView.as_view(), name='main'),
    path('save/', create_report,name='create-report'),
    path('from_file/', UploadTemplateView.as_view(),name='from-file'),
    path('<pk>/pdf/',render_pdf_view,name='pdf'),
    path('<pk>/', ReportDetailView.as_view(), name='detail'),
    path('', csv_upload_view,name='upload'),
    
]
