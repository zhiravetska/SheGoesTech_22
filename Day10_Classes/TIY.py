class House:
    #     # #     # class method example meaning method we can use without any objects created
    #     # #     # a library could be created by grouping class methods
    @classmethod
    def add(cls, a, b):
        print(a, b, a + b, cls.all_house_prop)
        return a + b

    #     #
    all_house_prop = "Brick"  # class property generally meant to be shared among instances

    #
    #     # # # # # #     # do not share lists, dictionaries other mutable structures in class properties
    # method definition which is function associated with objects
    def print_house_prop(self):
        print(f"This house is built from {self.all_house_prop}")

    #
    #     #
    #     # # # #     # so __init__ has to be exact name for constructor to be called
    #     # # # #     # __init__ is so called double under - dunder method
    # constructor method called upon creation of object
    def __init__(self, color="green", nails=0):
        #         # we add everything that we want done when we first create object from our class blueprints
        # self.color = color  # self.color is a property of the object
        self.color = None  # of course we could have stuck with self.color = color
        # by calling built in method we can perform extra validation
        self.set_color(color)
        self.nails = nails
        print(
            f"Initialized class instance with {self.color=} {self.nails=} {self.all_house_prop=}")
