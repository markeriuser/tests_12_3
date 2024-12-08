import unittest
import tournamenttest
import runnertest

def skip_if_frozen(test_func):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self)
    return wrapper

# Обновление классов RunnerTest и TournamentTest
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_walk(self):
        # Ваш тест
        pass

    # Добавьте остальные тесты

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        # Ваш тест
        pass

# Создание тестового набора
def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(create_test_suite())
