
from django.shortcuts import render, redirect, get_object_or_404
# models.py에서 Blog모델을 쓸 것이기 때문에 가져온다!
from .models import Blog, Hashtag
#forms.py에서 PostForm를 가져온다.
from .forms import PostForm, CommentForm, HashtagForm #CommentForm 추가함, 해시태그폼도!
# 장고에서 제공하는 시간기능을 사용하기 위함!
from django.utils import timezone

# Create your views here.

# def로 함수선언~ main이란 이름의 함수는 요청받았을 때 
# models.py에 있는 Blog클래스로 만든 객체들을 posts라는 변수에 저장한다.
# 반환한다(return), 불러옴으로써(render) 요청받았을 때 (request), blog파일에 main.html이란 html파일을 띄운다!
# 그리고 posts라는 변수를 main.html로 넘길 때 posts라는 이름으로 넘기겠다!!
#메인페이지
def main(request):
    posts = Blog.objects
    #여기에 해시태그 검색 넣음
    hashtags = Hashtag.objects
    return render(request, 'blog/main.html', {'posts':posts, 'hashtags':hashtags})
    
# def로 함수선언~ write이란 이름의 함수는 요청받았을 때 
# 반환한다(return), 불러옴으로써(render) 요청받았을 때 (request), blog파일에 write.html이란 html파일을 띄운다!
#글쓰기페이지
def write(request):
    return render(request, 'blog/write.html')

#글쓰기 함수
# def로 함수선언~ create이란 이름의 함수는 요청받았을 때 
def create(request, blog=None):
    #view에서 다시 한번 method를 확인 한뒤
    if request.method == 'POST':
        # form의 입력값 유효성 검증을 시작
        #request.files (미디어) 추가
        form = PostForm(request.POST, request.FILES, instance=blog )
        #우리가 post형식으로 요청받은 form이 forms.py에서 작성받기로 한 정보를 다 받았는 지 유효성검사!
        if form.is_valid ():
           blog = form.save(commit=False)
           blog.pub_date = timezone.datetime.now()
           blog.save()
           form.save_m2m()

           return redirect('main')

    #그렇지 않는다면 폼을 다시 입력받음      
    else:
        form = PostForm
        return render(request, 'blog/write.html', {'form':form})

#수정페이지
def edit(request, id):
    #blog모델에서 id값을 Blog라는 변수에 담아 가져오려 하는데, id값을 제대로 가져오지 못하면 404에러를 일으킬 것.
    blog = get_object_or_404(Blog, id = id)
    #view에서 다시 한번 method를 확인 한뒤
    if request.method == "POST":
        #orm의 입력값 유효성 검증을 시작, 이때 instance는 수정할 글이 어떤 글인지 글의 id를 함수에게 설명
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
           form.save(commit=False)
           form.save()
           # 여기에 해시태그 했음#
           form.save_m2m()
           #form이 잘 입력되었다면 main으로 이동!
           return redirect('main')

    #그렇지 않는다면 폼을 다시 입력받음 
    else:
        form = PostForm(instance=blog)
        return render(request, 'blog/edit.html', {'form':form})
   

#삭제 함수
def delete(request, id):
    blog = get_object_or_404(Blog, id = id)
    #특정 id값을 가진 데이터를 삭제해주는 함수.
    blog.delete()
    
    #삭제를 한 다음에 다시 main페이지를 띄운다.
    return redirect('main')

#디테일
def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment  = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            form.save_m2m()
            return redirect('detail',id)
        
    else:
        form=CommentForm()
        return render(request, "blog/detail.html", {'post':blog, 'form':form})

#해시태그함수(제발 오타 노)
def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'blog/hashtag.html', {'form':form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            #인덱스가 아니라 메인인가!?
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'blog/search.html', {'hashtag':hashtag})

