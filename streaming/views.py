from django.shortcuts import render,redirect
from .models import Video
# Create your views here.

def video_list(request):
    """
    비디오 목록
    """
    video_list = Video.objects.all()
    context = {'video_list':video_list}

    return render(request, 'streaming/video_list.html', context)

def video_new(request):
    """
    비디오 추가
    """
    if request.method =='POST':
        title = request.POST['title']
        video_key = request.POST['video_key']
        Video.objects.create(titie=title, video_key=video_key )
        return redirect('video:list')
    elif request.method == 'GET':
        return render(request, 'streaming/video_new.html')
    
def video_detail(request, video_id):
    """
    비디오 출력
    """
    video = Video.objects.get(id = video_id)
    context = {'video': video}
    return render(request, 'streaming/video_detail.html', context)
