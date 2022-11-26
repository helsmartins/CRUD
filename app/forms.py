from django.forms import ModelForm
from app.models import Oculos, Clientes

# Create the form class.
class OculosForm(ModelForm):
    class Meta:
        model = Oculos
        fields = ['marca', 'modelo', 'genero', 'cor']

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'logradouro', 'telefone', 'cpf']