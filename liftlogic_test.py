import unittest
from ascenseur.LiftLogic import LiftLogic


class MyTestCase(unittest.TestCase):
    # Ex 2 :
    def test_get_floor_prioritize_null_called_floor(self):
        lift = LiftLogic()
        self.assertEqual(None, lift.getFloor(1, None, None))

    def test_get_floor_prioritize_empty_list(self):
        lift = LiftLogic()
        self.assertEqual(None, lift.getFloor(1, None, []))

    def test_get_floor_prioritize_called_floor(self):
        lift = LiftLogic()
        self.assertEqual(1, lift.getFloor(1, 1, [2]))

    def test_get_floor_prioritize_closest_floor_above(self):
        lift = LiftLogic()
        self.assertEqual(2, lift.getFloor(0, None, [-3, 2]))

    def test_get_floor_prioritize_closest_floor_below(self):
        lift = LiftLogic()
        self.assertEqual(1, lift.getFloor(3, None, [1, 7]))

    def test_getFloor_prioritize_closest_floor_equal_distance_first_in_list_below(self):
        lift = LiftLogic()
        self.assertEqual(1, lift.getFloor(1, None, [1, 3]))

    def test_getFloor_prioritize_closest_floor_equal_distance_first_in_list_above(self):
        lift = LiftLogic()
        self.assertEqual(1, lift.getFloor(1, None, [3, 1]))

    def test_getDirection_shoud_stay(self):
        lift = LiftLogic()
        self.assertEqual(0, lift.getDirection(1, 1, []))

    def test_getDirection_should_go_up(self):
        lift = LiftLogic()
        self.assertEqual(1, lift.getDirection(1, 5, []))

    def test_should_stop_for_asked_floor(self):
        lift = LiftLogic()
        self.assertEqual(True, lift.shouldStop(1, 1, []))

    def test_should_stop_for_called_floors(self):
        lift = LiftLogic()
        self.assertEqual(True, lift.shouldStop(1, None, [3, 1]))

    def test_should_stop_for_both(self):
        lift = LiftLogic()
        self.assertEqual(True, lift.shouldStop(2, 2, [3, 2]))

    def test_should_not_stop(self):
        lift = LiftLogic()
        self.assertEqual(False, lift.shouldStop(3, 2, [1, 2]))

if __name__ == '__main__':
    unittest.main()
