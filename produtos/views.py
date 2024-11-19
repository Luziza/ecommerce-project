from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem, Avaliacao
from .forms import AvaliacaoForm

def index(request):
    return render(request, 'index.html')



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, produto_id):
    produto = get_object_or_404(Product, id=produto_id)
    avaliacoes = Avaliacao.objects.filter(produto=produto)
    return render(request, 'store/product_detail.html', {'produto': produto, 'avaliacoes': avaliacoes})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_items')

def cart_items(request):
    cart_items = CartItem.objects.all()  # Pega todos os itens do carrinho
    total = sum(item.get_total_price() for item in cart_items)  # Calcula o total
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_items')
    

def home(request):
    return render(request, 'base.html')

def cart(request):
    return render(request, 'cart.html')


def avaliar_produto(request, produto_id):
    produto = get_object_or_404(Product, id=produto_id)

    # Verifica se o usuário já fez uma avaliação
    if Avaliacao.objects.filter(produto=produto, usuario=request.user).exists():
        return render(request, 'store/erro_avalicao.html', {'mensagem': 'Você já avaliou este produto.'})

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            # Salva a avaliação com produto e usuário
            avaliacao = form.save(commit=False)
            avaliacao.produto = produto  # Atribui o produto
            avaliacao.usuario = request.user  # Atribui o usuário logado
            avaliacao.save()
            return redirect('product_detail', produto_id=produto.id)
    else:
        form = AvaliacaoForm()

    return render(request, 'store/avaliar_produto.html', {'produto': produto, 'form': form})# Exibição de avaliações de um produto
# def produto_detalhe(request, produto_id):
#     produto = get_object_or_404(Product, id=produto_id)
#     avaliacoes = Avaliacao.objects.filter(produto=produto)
#     return render(request, 'store/produto_detalhe.html', {'produto': produto, 'avaliacoes': avaliacoes})

# Exibição de avaliar produto
def avaliar_produto(request, produto_id):
    produto = get_object_or_404(Product, id=produto_id)
    avaliacoes = Avaliacao.objects.filter(produto=produto)
    return render(request, 'store/avaliar_produto.html', {'produto': produto, 'avaliacoes': avaliacoes})

