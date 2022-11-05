import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_konstruktori_toimii_oikein(self):
        self.assertAlmostEqual(len(self.statistics._players), 5)

    def test_haku_toimii_oikein(self):
        tulos = self.statistics.search("Sem")
        self.assertAlmostEqual(tulos, self.statistics._players[0])


    def test_huono_haku_ei_tuloksia(self):
        tulokset = self.statistics.search("WWWWWWWW")
        self.assertAlmostEqual(tulokset, None)

    def test_joukkue_haku_toimii(self):
        haku = self.statistics.team("EDM")
        self.assertAlmostEqual(len(haku), 3)

    def test_pisteiden_lasku_toimii(self):
        suurin = self.statistics.top(1)
        self.assertAlmostEqual(suurin[0].name, "Gretzky")

    def test_maalien_lasku_top_haku_toimii(self):
        tulos = self.statistics.top(1, SortBy.GOALS)
        self.assertAlmostEqual(tulos[0].name, "Lemieux")

    def test_syottojen_lasku_top_haku_toimii(self):
        tulos = self.statistics.top(1, SortBy.ASSISTS)
        self.assertAlmostEqual(tulos[0].name, "Gretzky")
    