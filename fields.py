class Field:
    """You'll work in fields of Z_n"""

    def __init__(self, field):
        """Initialize with field number"""
        self.field = field

    def build_list(self):
        """Build the list of field"""
        field = list(range(self.field))
        return field

    def change_field(self, new_field):
        """You can to change the field"""
        self.field = new_field

    def show_field(self):
        """You'll see the field with the work"""
        print(self.field)

    def additive_inverse(self):
        """Provides the additive inverse of the numbers in the field"""
        inverse_addition = {}
        for i in self.build_list():
            for n in self.build_list():
                if (i + n) % self.field == 0:
                    inverse_addition[i] = n

        return inverse_addition

    def multiplicative_inverse(self):
        """Provides the multiplicative inverse of the numbers in the field"""
        inverse_multiplicative = {}
        for i in self.build_list():
            for n in self.build_list():
                if (i * n) % self.field == 1:
                    inverse_multiplicative[i] = n

        return inverse_multiplicative

    def operations(self, *numbers):
        """Realize operations with numbers in the field"""
        operation = sum(numbers) % self.field
        print(operation)

