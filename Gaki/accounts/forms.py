from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):


    username = forms.RegexField(
        label=_("Login"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                        "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                'placeholder': 'Имя пользователя'
        })
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                        'placeholder': 'Пароль',
                                        'required': 'true',

        })
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                        'type': 'password',
                                        'placeholder': 'Подтверждение пароля',
                                        'required': 'true',
        }),
        help_text=_("Enter the same password as above, for verification.")
    )

    class Meta:
            model = User
            fields = ('username', 'password1', 'password2')