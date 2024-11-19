from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nota'].widget = forms.Select(choices=[(1, '1 estrela'), (2, '2 estrelas'), 
                                                            (3, '3 estrelas'), (4, '4 estrelas'), 
                                                            (5, '5 estrelas')])
        self.fields['comentario'].widget = forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escreva um comentário'})

    # Validação extra: Um usuário não pode avaliar o mesmo produto mais de uma vez
    def clean(self):
        cleaned_data = super().clean()
        produto = self.instance.produto  # Atribui o produto da instância atual
        usuario = self.instance.usuario  # Atribui o usuário da instância atual

        # Verifica se já existe uma avaliação do mesmo usuário para o mesmo produto
        if Avaliacao.objects.filter(produto=produto, usuario=usuario).exists():
            raise forms.ValidationError("Você já avaliou este produto.")
        return cleaned_data
