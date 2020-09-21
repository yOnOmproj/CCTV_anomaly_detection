from django.shortcuts import render, redirect
from .models import video_content, mat
from scipy.io import loadmat
import matplotlib.pyplot as plt
import io
import urllib, base64
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
    input_video = request.FILES['input_video_1']
    video = video_content(video = input_video)
    video.save()

    str_input_video = str(input_video)
    script_mat = '_C'
    mat_name = str_input_video.split('.')[0] + script_mat

    load_mat = mat.objects.get(title=mat_name)
    data1 = loadmat(load_mat.mat)
    print(data1['predictions'])
    video = video_content.objects.all()


    context = {}
    context['video'] = video[0]

    ###### plotly ######
    # fig = go.Figure()
    # scatter = go.Scatter(x=[0,1,2,3], y=[0,1,2,3], mode='lines', name='test', opacity=0.8, marker_color='green')
    # fig.add_trace(scatter)
    # plt_div = plot(fig, output_type='div')
    # x_data = [0,1,2,3]
    # y_data = [x**2 for x in x_data]
    # plot_div = plot([Scatter(x=x_data, y=y_data,
    #                     mode='lines', name='test',
    #                     opacity=0.8, marker_color='green')],
    #            output_type='div')

    # context['plot_div'] = plot_div

    # data = [go.bar(x=[0,1,2,3], y=[0,1,2,3])]
    # plot_url = py.plot(data, filename='basic-bar')

    # context['plot_url'] = plot_url
    # print(context)
    # trace0 = go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17])
    # trace1 = go.Scatter(x=[1, 2, 3, 4], y=[16, 5, 11, 9])
    
    # data = [trace0, trace1]
    # plotly = py.plot(data, filename ='basic-line')

    # context['plotly'] = plotly
    # print(context)

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



    return render(request, 'post/home2.html', context)
    # number = request.POST['number']

    # for i in range(int(number)):
    #     i_p = i+1
    #     i_str = str(i_p)
    #     input_value = f'input_video_{i_str}'

    #     input_video = request.FILES[input_value]
    #     video = video_content(video = input_video)
    #     video.save()
    
    # video = video_content.objects.all()

    # context = {}
    # for i in range(int(number)):
    #     i_p = i+1
    #     i_str = str(i_p)

    #     context[f'video{i_str}'] = video[i]

    # print(context)
    # return render(request, f'post/home{number}.html', context)

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