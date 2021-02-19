from django.db import models

class Pizza(models.Model):
    """Simple representation of a pizza for the pizzeria app."""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representations of the model."""
        return self.name

class Topping(models.Model):
    """Toppings for the pizzas."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
