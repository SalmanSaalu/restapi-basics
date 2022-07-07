
from django.urls import path,include
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails

urlpatterns = [
    # path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('articleclass/',ArticleAPIView.as_view()),
    path('ArticleDetails/<int:id>/',ArticleDetails.as_view())

]
