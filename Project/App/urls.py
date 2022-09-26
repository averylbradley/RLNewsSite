from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.PostList.as_view(), name="home"),
  path('post/<int:pk>', views.DetailView.as_view(), name="post_detail"),
  path("register", views.register_request, name="register"),
  path("login", views.login_request, name="login"),
  path("logout", views.logout_request, name= "logout"),
  path("add_post", views.AddPostView.as_view(), name="add_post"),
  path("post/<int:pk>/comment/", views.AddCommentView.as_view(), name="add_comment"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
