import unittest
from unittest.mock import MagicMock
from ascenseur.Lift import Lift


class MyTestCase(unittest.TestCase):
    def test_lift_up(self):
        mock = MagicMock()
        mock.getDirection.return_value = 1
        mock.shouldStop.return_value = False

        lift = Lift(logic=mock, starting_floor=3)
        lift.execute_iteration()

        self.assertEqual(4, lift.current_floor)
        mock.getDirection.assert_called_with(3, None, [])

    def test_lift_down(self):
        mock = MagicMock()
        mock.getDirection.return_value = -1
        mock.shouldStop.return_value = False

        lift = Lift(logic=mock, starting_floor=0)
        lift.execute_iteration()

        self.assertEqual(-1, lift.current_floor)
        mock.getDirection.assert_called_with(0, None, [])

    def test_lift_stop_at_asked_floor(self):
        mock = MagicMock()
        mock.getDirection.return_value = 1
        mock.shouldStop.return_value = True

        lift = Lift(logic=mock, starting_floor=1, asked_floor=1, called_button=[3, 1, 5])
        lift.execute_iteration()

        self.assertEqual(1, lift.current_floor)
        self.assertEqual(None, lift.asked_floor_button)
        self.assertListEqual([3, 5], lift.called_buttons)

        mock.getDirection.assert_called_with(1, 1, [3, 5])

    def test_lift_stop_at_called_floor_list(self):
        mock = MagicMock()
        mock.getDirection.return_value = 1
        mock.shouldStop.return_value = True

        lift = Lift(logic=mock, starting_floor=4, asked_floor=10, called_button=[7, 10, 4])
        lift.execute_iteration()

        self.assertEqual(4, lift.current_floor)
        self.assertEqual(10, lift.asked_floor_button)
        self.assertListEqual([7, 10], lift.called_buttons)

        mock.getDirection.assert_called_with(4, 10, [7, 10])

    # Test : double bouton d'appel

    def test_lift_up_double_button_up(self):
        mock = MagicMock()
        mock.getDirection.return_value = 1
        mock.shouldStop.return_value = False

        lift = Lift(logic=mock, starting_floor=4, asked_floor=(5, 1), called_button=[(5, 1), (0, -1)])
        lift.execute_iteration_double_button()

        # Test result
        self.assertEqual(5, lift.current_floor)
        mock.getDirection.assert_called_with(4, (5, 1), [(5, 1), (0, -1)])

    def test_lift_up_double_button_down(self):
        mock = MagicMock()
        mock.getDirection.return_value = 1
        mock.shouldStop.return_value = False

        lift = Lift(logic=mock, starting_floor=2, asked_floor=(5, -1), called_button=[(5, -1), (7, 1)])
        lift.execute_iteration_double_button()

        mock.getDirection.assert_called_with(2, (5, -1), [(5, -1), (7, 1)])
        mock.shouldStop.assert_called_with(2, (5, -1), [(5, -1), (7, 1)])

        # Test result
        self.assertEqual(3, lift.current_floor)
        self.assertEqual((5, -1), lift.asked_floor_button)

    # Test : l'ascenseur descend, passe par un étage appelé, mais ne s'arrête pas
    def test_lift_up_double_button_no_stop(self):
        mock = MagicMock()
        mock.getDirection.return_value = -1
        mock.shouldStop.return_value = False

        lift = Lift(logic=mock, starting_floor=6, asked_floor=(6, 1), called_button=[(6, 1), (-2, 1)])
        lift.execute_iteration_double_button()

        mock.getDirection.assert_called_with(6, (6, 1), [(6, 1), (-2, 1)])
        mock.shouldStop.assert_called_with(6, (6, 1), [(6, 1), (-2, 1)])

        self.assertEqual(5, lift.current_floor)
        self.assertEqual((6, 1), lift.asked_floor_button)
        self.assertListEqual([(6, 1), (-2, 1)], lift.called_buttons)

        # Test : l'ascenseur descend, passe par un étage appelé, mais ne s'arrête pas

    def test_lift_up_double_button_stop(self):
        mock = MagicMock()
        mock.getDirection.return_value = -1
        mock.shouldStop.return_value = True

        lift = Lift(logic=mock, starting_floor=-1, asked_floor=(-1, -1), called_button=[(6, 1), (-2, 1), (-1, -1)])
        lift.execute_iteration_double_button()

        self.assertEqual(-1, lift.current_floor)
        self.assertEqual(None, lift.asked_floor_button)
        self.assertListEqual([(6, 1), (-2, 1)], lift.called_buttons)

        mock.getDirection.assert_called_with(-1, (-1, -1), [(6, 1), (-2, 1)])
        mock.shouldStop.assert_called_with(-1, (-1, -1), [(6, 1), (-2, 1)])


if __name__ == '__main__':
    unittest.main()
