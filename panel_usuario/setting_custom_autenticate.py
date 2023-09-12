from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CodigoFuncionarioBackend(ModelBackend):
    def authenticate(self, request, codigo_funcionario=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(codigo_funcionario=codigo_funcionario)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
        return None
