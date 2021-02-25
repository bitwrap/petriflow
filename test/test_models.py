import unittest
from petriflow import Models
from examples import Counter, Pointer
from petriflow.error import InvalidOutput, InvalidInput, GuardFail


class ModelTestCase(unittest.TestCase):

    def test_ref_by_schema(self):
        self.assertTrue(self, 'counter_v1' in Models)
        self.assertTrue(self, 'pointer_v1' in Models)

    def test_counter_model(self):
        state, _ = Counter.transform([0, 0], 'inc0', 1)
        state, _ = Counter.transform(state, 'inc1', 3)
        self.assertEqual(state, [1, 3])

    def test_pointer_model(self):
        state, _ = Pointer.transform(Pointer.initial_vector(), 'create', 1)

        with self.assertRaises(InvalidInput):
            Pointer.transform(state, 'fake_action', 1)

        with self.assertRaises(InvalidOutput):
            Pointer.transform(state, 'create', 1)

        self.assertEqual(state, [1, 0, 0])
        state, _ = Pointer.transform(state, 'update', 1)
        self.assertEqual(state, [2, 0, 0])
        state, _ = Pointer.transform(state, 'disable', 1)
        self.assertEqual(state, [3, 1, 0])

        with self.assertRaises(GuardFail):
            Pointer.transform(state, 'update', 1)

        with self.assertRaises(InvalidOutput):
            Pointer.transform(state, 'disable', 1)

        state, _ = Pointer.transform(state, 'enable', 1)
        self.assertEqual(state, [4, 0, 0])
