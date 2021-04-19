from django.forms import ModelForm, BooleanField
from .models import Product


class ProductForm(ModelForm):
    #check_box = BooleanField(label = 'Алло, Галочка')
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'category', 'price']