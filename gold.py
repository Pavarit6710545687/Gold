class Gold:
    """
    Represents a gold piece, any kind.

    Attributes:
    name -- the name of the piece of gold
    gold_mass -- the mass of gold in grams, initialize as 0
    total_mass -- the total mass of the piece in grams, initialize as 0
    markup_add -- how much to ADD to the value when attempting to sell in THB
                  default value for markup_add is 0.
    """

    def __init__(self, name: str = "Gold", markup: int = 0):
        """
        Create a new piece of gold. Its name can be specified.
        If name is not given, then it is simply called "Gold".
        >>> Gold('a').name
        'a'
        >>> Gold().name
        'Gold'
        >>> Gold().gold_mass
        0
        >>> Gold().total_mass
        0
        >>> Gold().markup_add
        0
        """
        self.name = name
        self.gold_mass = 0
        self.total_mass = 0
        self.markup_add = markup

    def add(self, is_gold: bool, amount: int) -> None:
        """
        Add some mass to the piece. This will increase the
        total mass of the piece.
        If it's gold, increase the gold mass too.
        """
        self.total_mass += amount
        if is_gold:
            self.gold_mass += amount

    def remove(self, is_gold: bool, amount: int) -> int:
        """
        Remove some mass from the piece, and return the
        actual mass removed as int.
        """
        if is_gold:
            if self.gold_mass >= amount:
                self.gold_mass -= amount
                self.total_mass -= amount
                return amount
            else:
                actual_removed = self.gold_mass
                self.gold_mass = 0
                self.total_mass -= actual_removed
                return actual_removed
        else:
            if self.total_mass >= amount:
                self.total_mass -= amount
                return amount
            else:
                actual_removed = self.total_mass
                self.total_mass = 0
                return actual_removed

    def price(self, per_gram: int = 2000, include_markup: bool = True, force_purity: float = None) -> int:
        """
        Returns the appraised price of the gold artifact.
        """
        if force_purity is not None:
            price = (force_purity * self.total_mass * per_gram) + (self.markup_add if include_markup else 0)
        else:
            price = (self.gold_mass * per_gram) + (self.markup_add if include_markup else 0)
        
        return int(price)

    def purity(self) -> float:
        """
        Return the purity of the gold piece.
        """
        return round(self.gold_mass / self.total_mass, 4)

    def __repr__(self):
        """
        The STRING REPRESENTATION of the gold piece.
        """
        return f"Gold: {self.name}, {self.gold_mass} g / {self.total_mass} g"

    def __eq__(self, other):
        """
        Two gold objects are considered equal based on mass and markup.
        """
        if isinstance(other, Gold):
            return (self.gold_mass == other.gold_mass and
                    self.total_mass == other.total_mass and
                    self.markup_add == other.markup_add)
        return False
    
# Do not remove this block.
# Doctest will not run otherwise and you won't get score.
if __name__ == "__main__":
    import doctest
    doctest.testmod()