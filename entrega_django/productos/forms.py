from django import forms
from .models import Pedido
class ProductoForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    fecha_vencimiento=forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}))
    
class ProveedorForm(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.IntegerField()

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["fecha", "productos"] 