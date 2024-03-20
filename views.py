from .serializers import LogOutSerializer
from rest_framework import generics, views, permissions

class LogOutAPIView(generics.GenericAPIView):
  serializer_class = LogOutSerializer
  permission_classes = (permissions.IsAuthenticated, )
  def post(self, request):
    serializer = self.serializer_class(data = request.data)
    serializer.is_valid(raise_exception = True)
    derializer.save()
    return Responce(status = status.HTTP_204_NO_CONTENT)
    
  
  
