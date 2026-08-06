def calcular_total(itens, desconto_percentual=0):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    # Defeito proposital:
    # o desconto percentual esta sendo subtraido como valor monetario.
    total = subtotal - (subtotal * (desconto_percentual / 100))
    

CUPON_DESCONTO = {
    "DEVOPS10" : 10,
}

def desconto_cupom(cupom):
    if cupom is None:
        return  0
    
    codigo = cupom.strip().upper()
    if codigo not in CUPON_DESCONTO:
        raise ValueError("Cupom nao disponivel")
    
    return CUPON_DESCONTO [codigo]
