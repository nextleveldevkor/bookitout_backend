from django.urls import path
from customer import views
from rest_framework import routers, urlpatterns

router = routers.DefaultRouter()
router.register('', views.BooksViewSet)
router.register(r'search', views.BooksSearchViewSet)

# urlpatterns = [
#   path('products/', views.BooksView.as_view()),
# ]

urlpatterns = router.urls