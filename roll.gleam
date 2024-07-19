// Jacobus Burger (2024-07-16)
// Roll of the dice in starlang ❤️⭐
import gleam/io
import gleam/int

pub fn main() {
  let num = int.random(1, 50)
  let outcome = case num {
    3 -> "I'm three!!!"
    7 -> "Lucky!"
    11 -> "Symmetric!"
    12 -> "...And a partridge in a pair tree!"
    13 -> "🐍 Very Lucky!"
    42 -> "⭐ you found it!"
    69 -> "☯️ Yin-Yang"
    96 -> "Symmetry!"
    _ -> "(Nothing Happens)"
  }
  io.println(outcome)
}
