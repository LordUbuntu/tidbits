# Created by Jacobus Burger (2019)
# Info:
#   A demo text adventure game with practically no content that I created to
#   explore an idea I had. For some reason it doesn't work now but it used
#   to work.
# TODO: revisit and repair to functionality
import strutils


proc showCommands() =
  echo command_usage

proc lookAround() =
  var 
    item_list: string = "[ "
  echo "Name: ", currentRoom.name
  echo "Desc: ", currentRoom.desc
  echo "Items: "
  for it in currentRoom.item:
    item_list = item_list, "", it, ", "
  echo item_list


when isMainModule:
  var
    input: seq[string]
    gameIsRunning: bool = true
  while gameIsRunning:
    input = readLine(stdin).string.split(' ')
    case input[0]:
      of "help", "h":
        showCommands()
      of "look", "l":
        lookAround()
      of "get", "g":
        continue # implement proc
      of "use", "u":
        continue # implement proc
      of "inv", "i":
        continue # implement proc
      of "act", "a":
        continue # implement proc
      of "move", "m":
        #go(input[1])
        continue
      of "quit", "q":
        gameIsRunning = false
      else:
        echo "unrecognized command"
  echo "GAME DONE"





# TODO can't figure out how to link rooms, chicken and egg problem

type
  dir = enum
    North,
    South,
    East,
    West

type
  Item = object
    name: string
    desc: string

type
  Room = object
    name: string # the title
    desc: string # info on the room
    item: seq[Item] # items in the room

# relevant constant strings
const
  command_usage = """
  help: show valid command usage
  look: look around the room 
  get: take the specified item
  use: use the specified item 
  inv: show current player inventory
  act: do an action on an object
  move: move in a direction or to a location
  quit: quit this game """

# Items
const
  key: Item = Item(name: "Key", desc: "A key for some door")
  crowbar: Item = Item(name: "Crowbar", desc: "A standard crowbar")

# Rooms
const
  Start: Room = Room(name: "Start", desc: "start room", item: @[key, crowbar])
  End: Room = Room(name: "End", desc: "end room", item: @[])

# Temp
var
  currentRoom: Room = Start
