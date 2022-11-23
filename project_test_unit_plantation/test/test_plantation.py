from unittest import TestCase, main

from project_test_unit_plantation.plantation import Plantation


class TestPlantation(TestCase):
    SIZE = 10

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_setter_raises_when_plantation_size_is_less_than_zero(self):
        plantation = Plantation(self.SIZE)
        with self.assertRaises(ValueError) as context:
            plantation.size = -1

        self.assertEqual("Size must be positive number!", str(context.exception))
        self.assertIsNotNone(context.exception)
        self.assertEqual(self.SIZE, plantation.size)

    def test_hire_worker_when_worker_already_added(self):
        name = 'Gosho'
        self.plantation.hire_worker(name)

        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker(name)

        self.assertEqual("Worker already hired!", str(context.exception))
        self.assertEqual([name], self.plantation.workers)

    def test_hire_worker_when_worker_not_already_added(self):
        name = 'Gosho'
        result = self.plantation.hire_worker(name)

        self.assertEqual([name], self.plantation.workers)
        self.assertEqual(f"{name} successfully hired.", result)

    def test_len(self):
        self.plantation.plants['Gosho'] = ['plant']

        self.assertEqual(1, len(self.plantation))

    def test_len_is_adding_correctly(self):
        plantation = Plantation(10)
        plantation.hire_worker('Gosho')
        plantation.hire_worker('Tosho')
        plantation.plants['Gosho'] = ['plant']
        plantation.plants['Tosho'] = ['plant1']

        self.assertEqual(2, len(plantation))

    def test_empty_len(self):
        self.plantation.workers = ['Smrad']

        self.assertEqual(0, len(self.plantation))

    def test_planting_when_worker_is_not_hired_expect_to_raise(self):
        worker = 'Gosho'
        plant = 'Plant'

        with self.assertRaises(ValueError) as context:
            self.plantation.planting(worker, plant)

        self.assertEqual(f"Worker with name {worker} is not hired!", str(context.exception))

    def test_planting_when_plantation_is_full(self):
        size = 1
        plantation = Plantation(size)
        plantation.workers = ['Gosho']
        plantation.planting('Gosho', 'plant1')
        with self.assertRaises(ValueError) as context:
            plantation.planting('Gosho', 'plant')

        self.assertEqual("The plantation is full!", str(context.exception))
        self.assertEqual(plantation.plants['Gosho'], ['plant1'])

    def test_planting_when_worker_is_already_hired_and_has_planted(self):
        size = 100
        worker = 'Gosho'
        plant1 = 'plant1'
        plant2 = 'plant2'
        plantation = Plantation(size)
        plantation.hire_worker(worker)

        plantation.planting(worker, plant1)

        self.assertEqual(f"{worker} planted {plant2}.", plantation.planting(worker, plant2))
        self.assertDictEqual({worker: ['plant1', 'plant2']}, plantation.plants)

    def test_planting_worker_plants_first_plant(self):
        size = 100
        worker = 'Gosho'
        plant1 = 'plant1'
        plantation = Plantation(size)
        plantation.hire_worker(worker)

        self.assertEqual(f"{worker} planted it's first {plant1}.", plantation.planting(worker, plant1))
        self.assertEqual(plantation.plants[worker], [plant1])

    def test_str_when_no_workers(self):
        size = 100
        plantation = Plantation(size)

        self.assertEqual(f'''Plantation size: {plantation.size}\n''', str(plantation))

    def test_str_when_workers_and_no_plants(self):
        size = 100
        worker = 'Gosho'
        plantation = Plantation(size)
        plantation.hire_worker(worker)
        self.assertEqual(f'''Plantation size: {plantation.size}\nGosho''', str(plantation))

    def test_str_when_workers_and_plants(self):
        size = 100
        worker = 'Gosho'
        plant1 = 'plant1'
        plantation = Plantation(size)
        plantation.hire_worker(worker)
        plantation.planting(worker, plant1)
        self.assertEqual(f'''Plantation size: {plantation.size}\nGosho\nGosho planted: plant1''', str(plantation))

    def test_repr_when_no_workers(self):
        size = 100
        plantation = Plantation(size)

        self.assertEqual(f'''Size: {plantation.size}\nWorkers: ''', repr(plantation))

    def test_repr_when_there_are_workers(self):
        size = 100
        worker = 'Gosho'
        worker1 = 'Pesho'
        plant1 = 'plant1'
        plantation = Plantation(size)
        plantation.hire_worker(worker)
        plantation.hire_worker(worker1)
        plantation.planting(worker, plant1)
        self.assertEqual(f'''Size: {plantation.size}\nWorkers: Gosho, Pesho''', repr(plantation))


if __name__ == '__main__':
    main()
