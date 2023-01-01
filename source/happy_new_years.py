from datetime import datetime



if __name__ == '__main__':
    times = int(input())
    for _ in range(times):
        print("Happy New Years {}!".format(datetime.now().year))
