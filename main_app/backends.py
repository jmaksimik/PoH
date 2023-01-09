from django.contrib.auth.backends import ModelBackend, UserModel 
from django.db.models import Q 

class EmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
    
    def get_user(self, user_id):
        user = UserModel.objects.get(pk=user_id)
        return user if self.user_can_authenticate(user) else None
        