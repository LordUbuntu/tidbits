// Jacobus Burger (2024-07-16)
// Roll of the dice with the cute starlang
import gleam/io
import gleam/int

pub fn main() {
  let num = int.random(1, 50)
  let outcome = case num {
    3 -> "I'm three!!!"
    7 -> "Lucky!"
    13 -> "Very Lucky!"
    12 -> "...And a partridge in a pair tree!"
    42 -> "⭐ you found it!"
    _ -> "(Nothing Happens)"
  }
  io.println(outcome)
}
