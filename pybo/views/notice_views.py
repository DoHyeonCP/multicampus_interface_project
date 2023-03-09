from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


@login_required
def notice_detail_view(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    session_cookie = request.session['user_id']
    cookie_name = F'notice_hits:{session_cookie}'
    context = {
        'notice': notice,
    }
    response = render(request, 'notice/notice_detail.html', context)

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(pk) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{pk}', expires=None)
            notice.hits += 1
            notice.save()
            return response
    else:
        response.set_cookie(cookie_name, pk, expires=None)
        notice.hits += 1
        notice.save()
        return response

    return render(request, 'notice/notice_detail.html', context)