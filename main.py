# Pizza interface
class Pizza:
    def get_description(self):
        pass

    def get_cost(self):
        pass


# Concrete Pizza implementation
class BasicPizza(Pizza):
    def get_description(self):
        return "Basic Pizza"

    def get_cost(self):
        return 10.0


# Topping decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


# Concrete Topping decorators
class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return super().get_description() + ", Cheese"

    def get_cost(self):
        return super().get_cost() + 2.0


class Pepperoni(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return super().get_description() + ", Pepperoni"

    def get_cost(self):
        return super().get_cost() + 3.0


# Create different pizza variations using decorators
if __name__ == "__main__":
    # Create a basic pizza
    basic_pizza = BasicPizza()
    print("Description:", basic_pizza.get_description())
    print("Cost: $", basic_pizza.get_cost())

    # Add cheese to the basic pizza
    cheese_pizza = Cheese(basic_pizza)
    print("Description:", cheese_pizza.get_description())
    print("Cost: $", cheese_pizza.get_cost())

    # Add pepperoni and cheese to the basic pizza
    pepperoni_cheese_pizza = Pepperoni(Cheese(basic_pizza))
    print("Description:", pepperoni_cheese_pizza.get_description())
    print("Cost: $", pepperoni_cheese_pizza.get_cost())

    # Add more toppings or combinations as needed