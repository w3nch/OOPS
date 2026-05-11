## Challenge: Online Shopping Cart (OOP)

### Description:
Create a class-based system to manage an online shopping cart. The system should handle products, adding/removing items, checkout, and discounts. Use composition, abstraction, and polymorphism.

### Requirements:
1. Classes and Attributes:
  - Product:
    - name (str)
    - price (float)
    - stock (int)
  - Cart:
    - items (dictionary mapping Product to quantity)
  - Coupon:
    - code (str)
    - discount_percentage (float)
2. Methods:
  - Cart.add_product(product, quantity):
    - Add the product to cart if enough stock is available.
  - Cart.remove_product(product):
    - Remove the product from the cart.
  - Cart.checkout(coupon=None):
    - Calculate total price, apply coupon if provided, reduce product stock, return total amount.

**Extra Challenges:**
- Implement different product types with specific discounts.
- Validate coupon codes and expiration dates.
- Allow multiple coupons and combine discounts correctly.
