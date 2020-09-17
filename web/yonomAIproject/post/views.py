from django.shortcuts import render, redirect
from .models import video_content
# Create your views here.

def home(request):
    video = video_content.objects.all()
    video.delete()
    # context = {
        # 'video' : video,
    # }
    # video = video_content.objects.all()
    # video.delete()

    return render(request, 'post/home.html')

def about(request):
    return render(request, 'post/about.html')

def made_by(request):
    return render(request, 'post/made_by.html')

# def video_content(request):

#     if 'image' in request.FILES:
#         video = request.FILES['image']
#     video = video_content(dummi_videos = video)
#     video.save()

#     return redirect('post:home')
def insert_video(request):
    number = request.POST['number']

    for i in range(int(number)):
        i_p = i+1
        i_str = str(i_p)
        input_value = f'input_video_{i_str}'

        input_video = request.FILES[input_value]
        video = video_content(video = input_video)
        video.save()
    
    video = video_content.objects.all()

    context = {}
    for i in range(int(number)):
        i_p = i+1
        i_str = str(i_p)

        context[f'video{i_str}'] = video[i]

    print(context)
    return render(request, f'post/home{number}.html', context)

def home_number(request):
    if request.POST['number'] == '2' or request.POST['number'] == '3' or request.POST['number'] == '4':
        number = request.POST['number']
        video = video_content.objects.all()
        
        context = {
            'video' : video,
            'number' : number
        }


        return render(request, f'post/home{number}.html', context)
    
    else:
        return render(request, 'post/error.html')

def error(request):

    return render(request, 'error.html')