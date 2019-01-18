from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields['username'].widget.attrs.update({
                'placeholder': 'username'
            }),
            self.fields['password'].widget.attrs.update({
                'placeholder': 'password'
            })

class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        )
    )
    # 비밀번호 확인을 위한 필드
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password2',
            }
        )
    )

    # username필드의 검증에 username이 이미 사용중인지 여부 검사
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다')
        return username

    # password1와 password2의 값이 일치하는지 유효성 검사
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다')
        return password2

    # 자신이 가진 username과 password를 사용해서 유저 생성 후 반환하는 메서드
    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )
