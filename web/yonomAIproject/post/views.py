from django.shortcuts import render, redirect
from .models import video_content, mat
from scipy.io import loadmat
import matplotlib.pyplot as plt
import io
import urllib, base64
import cv2
import numpy as np
import os
import urllib, base64

################## 반복 실행 시키기 ####################
# import time 
# import threading 

# def thread_run():
#     print("test")

# rel = 0
# count = 5
# while count:
#     threading.Timer(5+rel, thread_run).start()
#     rel = rel + 5
#     count = count - 1

#######################################################

# import chart_studio.plotly as py
# import plotly.graph_objects as go 
# from plotly.offline import plot
# import plotly.graph_objs as go
# import chart_studio.plotly as py 
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
    video_delete = video_content.objects.all()
    video_delete.delete()

    input_video = request.FILES['input_video_1']
    str_input_video = str(input_video)
    str_input_video = str_input_video.split('.')[0]
    video = video_content(video = input_video, title=str_input_video)
    video.save()

    # print(video)
    script_mat = '_C'
    mat_name = str_input_video.split('.')[0] + script_mat

    mat_check = mat.objects.all()

    for i in mat_check:
        if str(mat_name) == str(i):
            load_mat = mat.objects.get(title=mat_name)
            mat_info = loadmat(load_mat.mat)
            mat_score = mat_info['predictions']
        else:
            pass
    

    
    # print(mat_score)
    video = video_content.objects.all()
    url = "../media/post/"
    video_path = url + str(input_video)
    print(video_path)

    context = {}
    context['video'] = video[0]



    return render(request, 'post/inserted.html', context)


def home_number(request):
    if 'non_member_login' in request.POST.keys():

        return render(request, 'post/home2.html')
    
    else:
        return render(request, 'post/error.html')

def error(request):

    return render(request, 'post/error.html')

def about2(request):
    return render(request, 'post/about2.html')

def about3(request):
    return render(request, 'post/about3.html')


def home_video(request):
    video = video_content.objects.all()
    video.delete()


    return render(request, 'post/home2.html')


def result(request):
    video = video_content.objects.all()

    isnormal = "normal"
    script = '_C'
    mat_name = video[0].title + script
    print(str(mat_name))
    str_mat_name = str(mat_name)

    getmat = mat.objects.get(title = str_mat_name)
    load_mat = loadmat(getmat.mat)
    mat_score = load_mat['predictions']
    format_score = []
    format_score_str = {}
    count = 1
    for i in mat_score:
        
        formatting = format(i[0], '.4f')
        float_formatting = float(formatting)
        count_to_dic = str(count) + "/32"
        if float_formatting > 0.4:
            format_score_str[count] = count_to_dic+ " " + formatting + " abnormal"
        else:
            pass

        format_score.append(float_formatting)
        count = count + 1

    # 12개

    if len(format_score_str.values()) > 3:
        isnormal = "abnormal"
    else:
        pass

###### plt ########
##### matplot #####
    # plt.plot(range(10))
    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format='png')
    # buf.seek(0)
    # string = base64.b64encode(buf.read())
    # url = urllib.parse.quote(string)

    # context['data'] = url
    # data2 = np.linspace(1, len(data1), 32)
    # data3 = pd.DataFrame(data1, data2)

    # plt.plot(data3)
    # plt.savefig()

    plt.figure(figsize=(5.1,2.2))
    plt.plot(np.linspace(1, 32, 32), format_score, c='r', label="abnormal_score")
    plt.plot(np.linspace(1, 32, 32), [0.4 for x in range(32)], 'b--')
    plt.yticks(np.linspace(0, 1, 11))
    plt.xticks(np.linspace(0, 32, 9))
    plt.legend()

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

#####################

    context = { 'video' : video[0],
                'isnormal' : isnormal,
                'format_score_str' : format_score_str.values(),
                'data' : uri
    }
    return render(request, 'post/result.html', context)