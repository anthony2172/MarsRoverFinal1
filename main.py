class Rover:

    # class attributes - they hold the same value for all instances of the class
    __plateau_limit_x_pos = 0
    __plateau_limit_y_pos = 0

    def __init__(self, initial_data):
        print()
        self.__x_pos = int(initial_data[0])
        self.__y_pos = int(initial_data[1])
        self.__heading = initial_data[2]

    def current_location(self):
        return "{} {} {}".format(self.__x_pos,self.__y_pos,self.__heading)

    def current_plateau_limits(self):
        return "Limits: x={} , y={}".format(Rover.__plateau_limit_x_pos, Rover.__plateau_limit_y_pos)

    def move(self):
        if self.__heading == "N":
            self.__y_pos += 1
        elif self.__heading == "S":
            self.__y_pos -= 1
        elif self.__heading == "E":
            self.__x_pos += 1
        elif self.__heading == "W":
            self.__x_pos -= 1
        return

    def rotate(self, rotation):
        if rotation == "L":
            if self.__heading == "N":
                self.__heading = "W"
            elif self.__heading == "W":
                self.__heading = "S"
            elif self.__heading == "S":
                self.__heading = "E"
            elif self.__heading == "E":
                self.__heading = "N"
        elif rotation == "R":
            if self.__heading == "N":
                self.__heading = "E"
            elif self.__heading == "E":
                self.__heading = "S"
            elif self.__heading == "S":
                self.__heading = "W"
            elif self.__heading == "W":
                self.__heading = "N"

        return

    def set_plateau_limits(plateau_limits):
        __plateau_limit_x_pos = int(plateau_limits[0])
        __plateau_limit_y_pos = int(plateau_limits[1])
        return

def main():

    rover_list = []
    # read plateau co-ordinates (e.g. '5 5')
    Rover.set_plateau_limits(input('Enter plateau co-ordinate limits: ').split())

    while 1:
        #get rover start co-ordinates and heading (e.g. '1 3 N')
        rover_start_data = input('\nEnter start position and heading of a rover to move [enter nothing to exit]: ').split()
        if not rover_start_data:
            # no input is exit condition - no more data to process
            break

        #instantiate rover class passing start co-ordinates & heading
        rover = Rover(rover_start_data)
        rover_list.append(rover)

        #get rover movement data (e.g. 'LMRRMMLLMR')
        rover_instruction_data = [char for char in input('Enter rover movement instruction string: ')]

        # process rover movement instructions
        for char in rover_instruction_data:
            if char == 'M':
                rover.move()
            else:
                rover.rotate(char)

        print("Rover movements completed")

    print("Exiting data entry...")

    #display results
    print('\nOutput:')
    for r in rover_list:
        print(r.current_location())

    return

if __name__ == "__main__":
    main()