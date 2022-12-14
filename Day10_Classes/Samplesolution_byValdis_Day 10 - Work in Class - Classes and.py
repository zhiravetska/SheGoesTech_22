# # Day 10 - Work in Class - Classes and Objects
# 1. Song class
# define a class Song

# The class constructor needs to have three additional 3 parameters (self and 3 more!)

# title defaults to empty string

# author defaults to empty string

# lyrics by default empty tuple

# inside constructor method:

# set/store these three parameters inside objects variables of the same name (remember to use self!)

#  print on the screen "New Song made" - (try also printing here author and title!)

class Song:
    # notice how lyrics default is a tuple, not a list, lists as defaults are dangerous
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        # print(f"New Song made by {self.author} called {self.title}")
        self.__print_song_info()

    # so private function for internal use only
    # we lose some customizability but we gain some security
    # it could have been public but we don't want to expose it with no need
    def __print_song_info(self):
        print(f"Song by {self.author} called {self.title}")

    def sing(self, max_lines=-1):
        # print(f"Singing song by {self.author} called {self.title}")
        self.__print_song_info()
        if max_lines == -1:
            max_lines = len(self.lyrics)  # our default
        for line in self.lyrics[:max_lines]:  # so default will be all lines
            print(line)
        return self  # so by returning self we can chain methods like this:

    def yell(self, max_lines=-1):
        # print(f"Yelling song by {self.author} called {self.title}")
        self.__print_song_info()
        if max_lines == -1:
            max_lines = len(self.lyrics)  # our default
        for line in self.lyrics[:max_lines]:
            print(line.upper())
        return self

# Minimum:

# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.

# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.

# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)

# Bonus: create an additional parameter max_lines to yell and sing methods that prints only a certain number of lines for both sing and yell. Better do with some default value e.g. -1, at which all rows are then printed.

# Create multiple songs with lyrics

# Example:


blank_song = Song()
ziemelmeita = Song("Zieme??meita", "Jumprava", [
                   "G??ju mekl??t zieme??meitu", "Garu, t??lu ce??u veicu", "Gr??ti bija"])

# ziemelmeita.sing()
# ziemelmeita.yell()

# now i can chain
ziemelmeita.sing(1).yell(2).sing().yell(500)


# Outputs:

# Zieme??meita - Jumprava

# G??ju mekl??t zieme??meitu

# Zieme??meita - Jumprava

# G??JU MEKL??T ZIEME??MEITU

# GARU, T??LU CE??U VEICU


# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song

# # no new constructor method is necessary (you can if you want)

class Rap(Song):
    def break_it(self, max_lines=-1, drop="yeah"):
        print(f"Breaking down rap by {self.author} called {self.title}")
        if max_lines == -1:
            max_lines = len(self.lyrics)  # our default
        for line in self.lyrics[:max_lines]:
            words = line.split()
            new_line = f" {drop} ".join(
                words) + " " + drop  # add drop at the end
            # # using replace as long as lyrics do not have extra whitespaces
            # new_line = line.replace(" ", f" {drop} ") + " " + drop
            # # the replace approach is more prone to input errors
            print(new_line)
        return self
#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to sing, but adds a drop after each word .

# Example:


zrap = Rap("Zieme??meita", "Jumprava", [
           "G??ju mekl??t zieme??meitu", "Garu, t??lu ce??u veicu"])


zrap.yell().break_it(1, "yah")

# Zieme??meita - Jumprava

# G??ju YAH mekl??t YAH zieme??meitu YAH
