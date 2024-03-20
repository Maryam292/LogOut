from .views import LogOutAPIView

urlpatterns = [
  path('logout/', LogOutAPIView.as_view(), name = "logout")
]
