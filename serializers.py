from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class LogOutSerializer(serializers.Serializer)
  refresh = serializers.CharField()
  default_error_messages = {
    'bad_token' : ('Token is expired or invalid')
  }
  
  def validate(self, attrs):
    self.token = attrs['refresh']
    return attrs
    
  def save(self, **kwargs):
    try:
      RefreshToken(self.token).blacklist()
    except TokenError:
      self.fail('bad_token')
    
    
