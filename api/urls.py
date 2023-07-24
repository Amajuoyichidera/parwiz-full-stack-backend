from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewset
from rest_framework.routers import DefaultRouter

# article_list, article_details, ArticleList, ArticleDetails

router = DefaultRouter()
router.register('articles', ArticleViewset, basename='articles')

urlpatterns = [
    path('', include(router.urls))
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
]
