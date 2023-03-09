from django.shortcuts import render,redirect
from .models import Video
from .forms import VideoUploadForm
# Create your views here.

def video_list(request):
    """
    비디오 목록
    """
    video_list = Video.objects.all()
    context = {'video_list':video_list}

    return render(request, 'streaming/video_list.html', context)

def video_detail(request, video_id):
    """
    비디오 출력
    """
    video = Video.objects.get(id = video_id)
    context = {'video': video}
    return render(request, 'streaming/video_detail.html', context)

def video_upload(request):
    """
    비디오 추가
    """
    if request.method =='POST':
        title = request.POST['title']
        videofile = request.FILES['videofile']
        fileupload = Video(
            title = title,
            videofile = videofile, 
        )
        fileupload.save()
        return redirect('streaming:video_upload')
    else:
        fileuploadForm = VideoUploadForm
        context = {
            'fileuploadForm':fileuploadForm,
        }
        return render(request, 'streaming/video_upload.html',context)
    

