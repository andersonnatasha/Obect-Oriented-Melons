"""Classes for melon orders."""

class AbstractMelonOrder:
    """ An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty):
        """Initialize"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5

        if self.species == "christmas melon":
            base_price = 1.5 * base_price
        
        total = (1 + self.tax) * self.qty * base_price

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the Government"""

    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        """Determine if order has passed inspection"""

        self.passed_inspection = passed
        
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17 
    
    def __init__(self, species, qty, country_code): #overwriting parent, but still need to call the parent 
        """Overwrite parent function initalization to add country code"""

        super().__init__(species, qty) #how we are going to make species and quantity 
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Overwrite parenrt's get_total() to 
        account for fee on orders less than six"""
        
        total = super().get_total()
        if self.qty < 10:
            total = total + 3

        return total
