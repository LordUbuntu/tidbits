# Jacobus Burger (2023)
# Info:
#   A much simpler base64 encoder/decoder program (practically cheating).
#   Done to solve some neat base64 strings I saw in a video, done for fun.
# See:
#   https://www.youtube.com/watch?v=bOCHTHkBoAs
import base64


if __name__ == '__main__':
    print(base64.b64decode(input()).decode("ascii"))
