from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# blog안에 view를 임포트 해준다.
import blog.views
#이곳에 미디어 하겠습니다!
from django.conf import settings
from django.conf.urls.static import static
#이곳에 회원가입!
from account import views

urlpatterns = [
    # 주소창 끝에 /admin을 쳐서 접속할 수 있음. 
    path('admin/', admin.site.urls),
    #페이지 열자마자 바로 실행됨, blog폴더 안에 view.py안에 main이라는 함수를 적용시킨다. 이름은 main으로 할 것임.
    path('', blog.views.main, name='main'),
    #주소창 끝에 /write/create를 쳐서 접속할 수 있음, blog폴더 안에 view.py안에 create이라는 함수를 적용시킨다. 이름은 create으로 할 것임.
    path('write/create/', blog.views.create, name='create'),
    #주소창 끝에 /detail를 쳐서 접속할 수 있음, 특정 게시물을 가져오는 것이기 때문에 id를 지정해줌, blog폴더 안에 view.py안에 create이라는 함수를 적용시킨다. 이름은 detail으로 할 것임.
    path('detail/<str:id>/', blog.views.detail, name='detail'),
    #주소창 끝에 /edit를 쳐서 접속할 수 있음, 특정 게시물을 가져오는 것이기 때문에 id를 지정해줌,blog폴더 안에 view.py안에 edit이라는 함수를 적용시킨다. 이름은 edit으로 할 것임.
    path('edit/<str:id>/', blog.views.edit, name='edit'),
    #주소창 끝에 /delete를 쳐서 접속할 수 있음, 특정 게시물을 가져오는 것이기 때문에 id를 지정해줌,blog폴더 안에 view.py안에 delete이라는 함수를 적용시킨다. 이름은 delete으로 할 것임.
    path('delete/<str:id>/', blog.views.delete, name='delete'),
    #해시테그 url추가
    path('blog/hashtag/', blog.views.hashtagform, name='hashtag'),
    #검색기능
    path('blog/<int:hashtag_id>/search/', blog.views.search, name='search'),
    #로그인!!!
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
