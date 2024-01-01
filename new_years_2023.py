# Jacobus Burger (2023)
# Happy New Years (2023->2024)!
from time import sleep
from os import name, system
from random import choice

def clear(): system("cls" if name == "nt" else "clear")
DELAY = 0.5
message = "Happy New Years!"
frames = [
    """







    """,
    """





         
        *
    """,
    """





        *
        ?
    """,
    """




        *
        ?
        |
    """,
    """



        *
        ?
        |
         
    """,
    """


       ***
       *#*
        *


    """,
    """
      * @ *
       \ /
      *-#-*
        |
        *

    """,
    """
      @   @
       @ @
      @ @ @
         
        @

    """,
    """
           
     @     @
       @ @ 
      @   @
        @
        @
    """,
    """
           
     .     @
       @ @ 
      @   .
        @
        .
    """,
    """
           
           .
       . @ 
      @    
        .
         
    """,
    """
           
            
         . 
      .    
         
         
    """,
    """







    """,
]


if __name__ == "__main__":
    for frame in frames:
        clear()
        print(message)
        print(frame)
        sleep(DELAY)
    input()
