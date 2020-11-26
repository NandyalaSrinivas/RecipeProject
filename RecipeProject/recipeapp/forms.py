from django import forms
from recipeapp.models import RecipeModel


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = "__all__"
