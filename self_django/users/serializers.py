
from .models import CustomUser
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer): #하나만 임포트해서 하는게 나을 것 같아서 바꿈. 
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

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'nickname', 'age',) #유저 정보 get api땜시 근데 이거 자체는 그냥 get api지 않나라는 궁금증이 있었는데 나는 jwt로 세션관리를 할거니까 jwt를 이용해서 api를 호출했을 때 문제가 없으면 세션이 잘 유지되고 있다. 