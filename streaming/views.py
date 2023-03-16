from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoUploadForm
from django.utils import timezone
from django.contrib import messages
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

@login_required(login_url = 'common:login')
def video_upload(request):
    """
    비디오 추가
    """
    if request.method =='POST':
        fileuploadForm = VideoUploadForm(request.POST)
        if fileuploadForm.is_valid():
            video = fileuploadForm.save(commit=False)
            video.author = request.user
            video.create_date = timezone.now()
            fileuploadForm.save()
            return redirect('streaming:video_upload')
    else:
        fileuploadForm = VideoUploadForm()
        
    context = {
        'fileuploadForm':fileuploadForm,
    }
    return render(request, 'video_upload.html',context)


@login_required(login_url = "common:login")
def video_modify(request, video_id):
    """
    비디오 수정
    """
    video = get_object_or_404(Video, pk=video_id)
    if request.user != video.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('streaming:detail', video_id = video.id)
    
    if request.method == "POST":
        fileuploadForm = VideoUploadForm(request.POST, instance = video)
        if fileuploadForm.is_valid():
            video = fileuploadForm.save(commit = False)
            video.author = request.user
            video.modify_date = timezone.now()
            video.save()
            return redirect('steraming:detail', video_id = video.id)
    else:
        fileuploadForm = VideoUploadForm(instance = video)

    context = {'fileuploadForm': fileuploadForm}
    return render(request, 'streaming/video_upload.html', context )

@login_required(login_url = "common:login")
def video_delete(request, video_id):
    """
    비디오삭제
    """
    video = get_object_or_404(Video, pk = video_id)
    if request.user != video.author:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect('streaming:detail', video_id = video.id)
    video.delete()
    return redirect('streaming:list')