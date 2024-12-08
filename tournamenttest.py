import unittest

# Исходный класс Runner
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# Класс Tournament
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = str(participant)  # Изменение здесь
                    place += 1
                    self.participants.remove(participant)

        return finishers


# Класс тестов TournamentTest
class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
