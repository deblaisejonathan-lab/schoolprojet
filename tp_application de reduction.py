def apply_discount(price,discount):
    if not isinstance(price, (int, float)):
        return f'the price should be a number'
    if not isinstance(discount,(int,float)):
        return f'the discount should be a number'
    if price <= 0:
        return f'the price should be greater than 0'
    if discount<0 or discount >100:
        return f'the discount should be betwenn 0and 100'
    else:
         resultat = price- (price * discount / 100)
    return resultat
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(74.5, 20.0))



