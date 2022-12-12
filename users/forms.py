from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):

    email = forms.EmailField(required=True)


    class Meta:
        # vamos a indicar que este formulario pertenece a un modelo
        model = User
        # podemos definir que campos seran los que mostremos usando el atributo fields
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    # Vamos a sobre escribir el metodo save 

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)

        # aumentar el email

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user