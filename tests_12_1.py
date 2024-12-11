import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runer = Runner('<NAME>')
        for i in range(10):
            runer.walk()
        self.assertEqual(runer.distance, 50)

    def test_run(self):
        runer = Runner('<NAME>')
        for i in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    def test_challenger(self):
        runner1 = Runner('<NAME>')
        runner2 = Runner('<NAME>')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


my_test = RunnerTest()
my_test.test_run()
my_test.test_walk()
my_test.test_challenger()
