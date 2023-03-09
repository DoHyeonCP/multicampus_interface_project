from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        if request.user in question.voter.all():
            question.voter.remove(request.user)
            messages.success(request, '추천을 취소했습니다.')          

        else:
            question.voter.add(request.user)
            messages.success(request, '추천했습니다.')


    return redirect('pybo:detail', question_id=question.id)

