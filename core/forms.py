from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class Registro(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name","last_name","email","username","password1","password2")




    def clean_nombre(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match("^[A-Za-z]*$", first_name):
            raise ValidationError("El nombre solo debe contener letras.")
        return first_name
    

    def clean_apellido(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match("^[A-Za-z]*$", last_name):
            raise ValidationError("El apellido solo debe contener letras.")
        return last_name
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.(com|cl)$", email):
            raise ValidationError("El correo electrónico debe contener '@' y terminar con '.com' o '.cl'.")
        return email



    def clean_usuario(self):
        username = self.cleaned_data.get('username')
        if not re.match("^[A-Za-z]*$", username):
            raise ValidationError("El nombre de usuario solo debe contener letras.")
        if not re.search(r"[A-Z]", username):
            raise ValidationError("El usuario debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", username):
            raise ValidationError("El usuario debe contener al menos una letra mayúscula.")
        return username

    def clean_contra1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
        if not re.search(r"[A-Z]", password1):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", password1):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"[0-9]", password1):
            raise ValidationError("La contraseña debe contener al menos un número.")
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data