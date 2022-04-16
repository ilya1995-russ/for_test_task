from django.urls import path, include
from test_task import views
from django.contrib.auth import views as aut
from django.urls import path
from api.views import ArticleView

# app_name = "articles"

urlpatterns = [
    path('registration/', views.RegisterForm.as_view(), name='registration'),
    path('login/', aut.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', aut.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
    path('', views.ArticleView.as_view(), name='index'),
    path('artic/<int:pk>', views.DetailArticleView.as_view(), name='detail_article'),
    path('create_article', views.CreateArticleView.as_view(), name='create_article'),
    path('update_article/<int:pk>',
         views.UpdatelArticleView.as_view(), name='update_article'),
    path('delete_article/<int:pk>',
         views.DeleteArticleView.as_view(), name='delete_article'),
    path('api/articles/', ArticleView.as_view()),
    path('api/articles/<int:pk>', ArticleView.as_view()),

]
