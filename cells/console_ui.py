from cells.map import Map, SlideDir

STEP_DICT = {
    1: SlideDir.UP,
    2: SlideDir.DOWN,
    3: SlideDir.LEFT,
    4: SlideDir.RIGHT
}

if __name__ == "__main__":
    print("Input height: ", end="")
    height = int(input())

    print("Input width: ", end="")
    width = int(input())

    map = Map(height, width)
    map.generate_new_cell()

    while(True):
        print(map)
        print("1 - UP\n"
              "2 - DOWN\n"
              "3 - LEFT\n"
              "4 - RIGHT\n"
              "$> ", end="")
        map.step(STEP_DICT[int(input())])