from django.contrib.auth.forms import UserCreationForm
from .models import User

class creationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
        
class creationUserFormFuncionario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff']