class LiftLogic:
    def getFloor(self, current_floor, asked_floor, called_floors):
        if asked_floor is not None:
            return asked_floor
        elif called_floors is not None and len(called_floors) > 0:
            delta = None
            result = None

            for floor in called_floors:
                current_delta = abs(current_floor - floor)
                if delta is None or delta > current_delta:
                    delta = current_delta
                    result = floor

            return result
        return None

    def getDirection(self, current_floor, asked_floor, called_floors):
        floor_to_move = self.getFloor(current_floor, asked_floor, called_floors)
        if floor_to_move is None or current_floor == floor_to_move:
            return 0
        elif floor_to_move > current_floor:
            return 1
        else:
            return -1

    def shouldStop(self, current_floor, asked_floor, called_floors):
        return (asked_floor is not None and current_floor == asked_floor) or current_floor in called_floors
