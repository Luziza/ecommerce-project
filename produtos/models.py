from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    
    # Novo campo para imagem
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # upload para a pasta 'products/'
    
    # Novo campo para link de imagem
    image_url = models.URLField(max_length=500, null=True, blank=True)  # Para link de imagem externa
    
    def __str__(self):
        return self.name


class Avaliacao(models.Model):
    produto = models.ForeignKey(Product, related_name='avaliacoes', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), 
                                        (4, '4 estrelas'), (5, '5 estrelas')])
    comentario = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('produto', 'usuario')  # Um usuário pode avaliar um produto apenas uma vez

    def __str__(self):
        return f'Avaliação de {self.usuario.username} para {self.produto.name} - {self.nota} estrelas'
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
    def get_total_price(self):
        return self.quantity * self.product.price
