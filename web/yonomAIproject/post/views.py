from django.shortcuts import render, redirect
from .models import video_content
# Create your views here.
def home(request):
    # video = video_content.objects.all()
    # context = {
        # 'video' : video,
    # }
    return render(request, 'post/home.html')

def about(request):
    return render(request, 'post/about.html')

def made_by(request):
    return render(request, 'post/made_by.html')

def video_content(request):

    if 'image' in request.FILES:
        video = request.FILES['image']
    video = video_content(dummi_videos = video)
    video.save()

    return redirect('post:home')

def home_number(request):
    if request.POST['number'] == '2' or request.POST['number'] == '3' or request.POST['number'] == '4':
        number = request.POST['number']

        return render(request, f'post/home{number}.html')
    
    else:
        return render(request, 'post/error.html')

def error(request):

    return render(request, 'error.html')