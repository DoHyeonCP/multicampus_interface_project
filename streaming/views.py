from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video, Subscription
from .forms import VideoUploadForm
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.sessions.backends.db import SessionStore
from django.views.decorators.http import require_POST
# Create your views here.

def video_list(request):
    """
    비디오 목록
    """
    video_list = Video.objects.order_by('-create_date')
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
            video.videofile = request.FILES["videofile"]
            fileuploadForm.save()
            return redirect('list')
    else:
        fileuploadForm = VideoUploadForm()
        
    context = {
        'fileuploadForm':fileuploadForm,
    }
    return render(request, 'streaming/video_upload.html', context)


@login_required(login_url = "common:login")
def video_modify(request, video_id):
    """
    비디오 수정
    """
    video = get_object_or_404(Video, pk=video_id)
    if request.user != video.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('detail', video_id = video.id)
    
    if request.method == "POST":
        fileuploadForm = VideoUploadForm(request.POST, instance = video)
        if fileuploadForm.is_valid():
            video = fileuploadForm.save(commit = False)
            
            if 'videofile' in request.FILES:
                video.videofile = request.Files['videofile']
                
            video.author = request.user
            video.modify_date = timezone.now()
            video.save()
            return redirect('detail', video_id = video.id)
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
        return redirect('detail', video_id = video.id)
    video.delete()
    return redirect('list')

@login_required(login_url = 'common:login')
def subscribe(request, video_id):
    item = Video.objects.get(pk=video_id)
    if Subscription.objects.filter(user = request.user, subscribed_to=item).exists():
        #이미 구독중이라면
        return redirect('detail', pk=video_id)
    Subscription.objects.create(user=request.user, subscribed_to=item)
    return redirect('detail', video_id=item.id)


@require_POST
def increment_view_count(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    session = SessionStore(request.session.session_key)
    session_video_key = f'video_{video_id}_view'

    if not session.get(session_video_key):
        video.view_count += 1
        video.save()
        session[session_video_key] = True

    return JsonResponse({'view_count':video.view_count})


@login_required(login_url='common:login')
def post_l(request, video_id):    
    video = get_object_or_404(Video, pk=video_id)
    if video.likes.contains(request.user) == False:

        if request.user == video.author:
            messages.error(request, '본인의 영상입니다.')
        else:
            video.likes.add(request.user)
    else:
        video.likes.remove(request.user)

    return redirect('detail', video_id=video.id)

