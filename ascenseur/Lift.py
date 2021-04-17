from ascenseur.LiftLogic import LiftLogic


class Lift:
    current_floor = 0
    called_buttons = []

    def __init__(self, logic: LiftLogic, starting_floor, asked_floor=None, called_button=None):
        if called_button is None:
            called_button = []

        self.min_floor = -2
        self.max_floor = 10
        self.logic = logic
        self.asked_floor_button = asked_floor
        self.called_buttons = called_button

        self.current_floor = starting_floor

    def execute_iteration(self):
        direction = self.logic.getDirection(self.current_floor, self.asked_floor_button, self.called_buttons)

        if (self.current_floor + direction >= self.min_floor) and (self.current_floor + direction <= self.max_floor):
            if not self.logic.shouldStop(self.current_floor, self.asked_floor_button, self.called_buttons):
                self.current_floor += direction
                print("Lift moved to {0}".format(self.current_floor))
            else:
                print("Lift arrived at floor in called_button_list")
                self.called_buttons.remove(self.current_floor)

                if self.asked_floor_button == self.current_floor:
                    self.asked_floor_button = None
                    print("Lift arrived at the asked floor")

    def execute_iteration_double_button(self):
        direction = self.logic.getDirection(self.current_floor, self.asked_floor_button, self.called_buttons)

        if (self.current_floor + direction >= self.min_floor) and (self.current_floor + direction <= self.max_floor):
            if not self.logic.shouldStop(self.current_floor, self.asked_floor_button, self.called_buttons):
                self.current_floor += direction
                print("Lift moved to {0}".format(self.current_floor))
            else:
                print("Lift arrived at floor in called_button_list")
                self.called_buttons.remove((self.current_floor, direction))
                # a modifier !

                if self.asked_floor_button[0] == self.current_floor:
                    self.asked_floor_button = None
                    print("Lift arrived at the asked floor")

    def run(self):
        while True:
            self.execute_iteration()
