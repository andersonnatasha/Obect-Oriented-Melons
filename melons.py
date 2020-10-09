"""Classes for melon orders."""

class AbstractMelonOrder:
    """ An abstract base class that other Melon Orders inherit from"""

    def __init__(self, p_species, p_qty):
        """Initialize"""

        self.species = p_species
        self.qty = p_qty
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
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17 
    
    def __init__(self, parameter_species, parameter_qty, country_code): #overwriting parent, but still need to call the parent 
        super().__init__(parameter_species, parameter_qty) #how we are going to make species and quantity 
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        if self.qty < 10:
            total = super().get_total()
            total = total + 3 

        return total
