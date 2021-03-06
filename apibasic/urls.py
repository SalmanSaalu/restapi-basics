
from django.urls import path,include
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
urlpatterns = [
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('articleclass/',ArticleAPIView.as_view()),
    path('ArticleDetails/<int:id>/',ArticleDetails.as_view()),
    path('generic/article/<int:id>/',GenericAPIView.as_view())


]
