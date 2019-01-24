from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post,PostImage,Comment
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
class PostLV(ListView):
    model = Post
    # 어떤 데이터를 꺼내쓸래??
    context_object_name = 'post_list'

def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    property = Post.objects.get(pk=post_pk)
    image_list = property.images.all()
    comment_form = CommentForm()

    context = {
        'post' : post,
        'image_list' : image_list,
        'comment_form' : comment_form,
    }

    return render(request, 'blog/post_detail.html', context)

@login_required
def comment_create(request, post_pk):
    # GET 파라미터로 전달된 작업 완료 후 이동할 URL값
    next_path = request.GET.get('next')
    print(next_path)
    # 요청 메서드가 POST방식 일 때만 처리
    if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=post_pk)
        # request.POST데이터를 이용한 Bounded Form생성
        comment_form = CommentForm(request.POST)
        # 올바른 데이터가 Form인스턴스에 바인딩 되어있는지 유효성 검사
        if comment_form.is_valid():
            # 유효성 검사에 통과하면 ModelForm의 save()호출로 인스턴스 생성
            # DB에 저장하지 않고 인스턴스만 생성하기 위해 commit=False옵션 지정
            comment = comment_form.save(commit=False)
            # CommentForm에 지정되지 않았으나 필수요소인 author와 post속성을 지정
            comment.post = post
            comment.author = request.user
            # DB에 저장
            comment.save()

            # 성공 메시지를 다음 request의 결과로 전달하도록 지정
            messages.success(request, '댓글이 등록되었습니다')
        else:
            # 유효성 검사에 실패한 경우
            # 에러 목록을 순회하며 에러메시지를 작성, messages의 error레벨로 추가
            error_msg = '댓글 등록에 실패했습니다\n{}'.format(
                '\n'.join(
                    [f'- {error}'
                     for key, value in comment_form.errors.items()
                     for error in value]))
            messages.error(request, error_msg)

        # next paramater에 값이 담겨 온 경우, 해당 경로로 이동
        if next_path:
            return redirect(next_path)
        # next paramater가 빈 경우 post_list뷰로 이동
        return redirect('post:post_list')
