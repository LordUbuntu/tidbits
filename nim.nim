# Created by Jacobus Burger (2021)
# Info:
#   The game of nim, written in nim. This was a rewrite of an older
#   version I deleted back in 2019 and consequently is much better than
#   the old version. This rewrite was commissioned for my favourite class
#   (a class about programming languages).
#   This program was written once previously for fun but looked
#   quite different at the time.
import rdstdin, strutils, strformat

var 
  player: int
  robot: int
  total: int

total = 4 * parseInt(readLineFromStdin "How many rounds?: ")
echo (fmt"Starting total: {total}")
while total > 0:
  #  player turn
  player = parseInt(readLineFromStdin "How many tiles (1 to 3)?: ")
  
  # ensure player input remains valid
  if player > 3:
    player = 3
  elif player < 1:
    player = 1

  # bot turn
  robot = 4 - player

  # subtract from total and finish turn
  total = total - (player + robot)
  echo (fmt"You take: {player}, AI takes: {robot}, total left: {total}")
echo "AI Wins!" # end game (note: robot always wins)
