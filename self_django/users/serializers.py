from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class UserRegisterSerializer(ModelSerializer): 
    class Meta: 
        model = CustomUser
        fields = ('username', 'email', 'password', 'nickname', 'age',) 

    def create(self, validate_data):
        user = CustomUser(
            username = validate_data['username'],
            email = validate_data['email'],
            nickname = validate_data.get('nickname'),#models.py에서 닉네임과 나이는 공란으로 받아도 된다고 설정했으니까
            age = validate_data.get('age'),
        )
        user.set_password(validate_data['password']) # 비밀번호는 그냥 받으면 위험하구로.
        user.save()
        return user
