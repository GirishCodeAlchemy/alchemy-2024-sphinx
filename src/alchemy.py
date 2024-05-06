class StarterSuit:

    """
    This class defines one of the starter Iron Man suits built by Tony Stark
    at the beginning of the Iron Man movie series.

    Actual suits can be created by calling the specific classes defining the
    Iron Man suit types. You can see more details about them at :ref:`starter`.
    """

    def __init__(self):
        self.name = None
        self.evolution = None
        self.ability = None
        self.suit_type = None

    def who_is_that_suit(self):
        """
        Shows the Iron Man suit name and its upgrades.

        Usage:

        .. doctest::

           >>> import ironman
           >>> suit = ironman.MarkI()
           >>> suit.who_is_that_suit()
           This is Mark I Iron Man suit.
           It will upgrade into Mark II, Mark III, Hulkbuster, and Infinity War Suit.
           >>>
        """
        print(f"This is {self.name} Iron Man suit.")
        print(f"It will upgrade into {', '.join(self.evolution)}.")


class MarkI(StarterSuit):
    """
    Mark I is the first Iron Man suit built by Tony Stark.

    It is the original Iron Man suit featured in the first Iron Man movie.

    Along with :class:`MarkII` and :class:`MarkIII`, Mark I is one of
    three starter suits available at the beginning of Iron Man movie.
    """

    def __init__(self):
        self.name = "Mark I"
        self.suit_type = {"armor"}
        self.ability = "Armor"
        self.evolution = [
            "Mark II",
            "Mark III",
            "Hulkbuster",
            "Infinity War Suit",
        ]


class MarkII(StarterSuit):
    """
    Mark II is an upgraded version of the Iron Man suit.

    It features improved capabilities and enhancements compared to the
    original Mark I suit.

    Along with :class:`MarkI` and :class:`MarkIII`, Mark II is one of
    three starter suits available in the Iron Man movie.
    """

    def __init__(self):
        self.name = "Mark II"
        self.suit_type = {"armor"}
        self.ability = "Flight"
        self.evolution = [
            "Mark III",
            "Hulkbuster",
            "Infinity War Suit",
        ]


class MarkIII(StarterSuit):
    """
    Mark III is a highly advanced Iron Man suit.

    It features state-of-the-art technology and weaponry, making it one of
    the most powerful suits in Tony Stark's arsenal.

    Along with :class:`MarkI` and :class:`MarkII`, Mark III is one of
    three starter suits available in the Iron Man movie.
    """

    def __init__(self):
        self.name = "Mark III"
        self.suit_type = {"armor"}
        self.ability = "Repulsor Beams"
        self.evolution = [
            "Hulkbuster",
            "Infinity War Suit",
        ]
