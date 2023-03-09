
def detail(request, id):
    detail_data = get_object_or_404(Book, pk = id)
    comments = Comment.objects.filter(book_id=id, comment_id__isnull=True)

    re_comments = []
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    
    form = CommentForm()
    response =  render(request, 'detail.html' ,{'data' : detail_data, 'comments' : comments, 're_comments' : re_comments, 'form':form})

    #조회수 기능 (쿠키 이용)
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitblog', '_')

    if f'_{id}_' not in cookie_value:
        cookie_value += f'{id}_'
        response.set_cookie('hitblog', value=cookie_value, max_age=max_age, httponly=True)
        detail_data.hits += 1
        detail_data.save()

    return response