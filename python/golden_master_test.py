import os
import unittest
# je dé commente la ligne en dessous quand je veux faire un record de ce que la classe originelle
# et je commente lanGame2, une fois que c'est fait je recommente et je lance le replay pour comparer les résultats
#from tennis2 import TennisGame2
from lanGame2 import TennisGame2
class GoldenMasterTest(unittest.TestCase):

    DIR = "/Users/kenzamerzouk/PycharmProjects/Tennis-Refactoring-Kata/golden-master";
    subFR= "/Users/kenzamerzouk/PycharmProjects/Tennis-Refactoring-Kata/golden-master/FR";
    subEN= "/Users/kenzamerzouk/PycharmProjects/Tennis-Refactoring-Kata/golden-master/EN";
    #concernant ls stockage de mes résultats de tests, je sépare bien dans des sous dossiers FR et EN

    @staticmethod
    def play_game(p1Points, p2Points, p1Name, p2Name, langue):
        game = TennisGame2(p1Name, p2Name, langue)
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        return game.score()

    def make_file_name(self, score_player_1, score_player_2, langue):
        return f"{self.DIR}/{langue}/{score_player_1}_{score_player_2}.txt"

    def _test_record(self):
        for langue in ['FR', 'EN']:
            #rajouter un mkdir qui génerera un dossier s'il existe pas
            # Créer le sous-dossier correspondant à la langue si nécessaire
            sub_dir = self.subFR if langue == 'FR' else self.subEN
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir)

            for score_player_1 in range(16):
                for score_player_2 in range(16):
                    with self.subTest(f"{score_player_1}, {score_player_2} - {langue}"):
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", langue)
                        file = open(self.make_file_name(score_player_1, score_player_2,langue), "w")
                        file.write(sortie)
                        file.close()

    def test_replay(self):
        for langue in ['FR', 'EN']:
            # Créer le sous-dossier correspondant à la langue si nécessaire
            sub_dir = self.subFR if langue == 'FR' else self.subEN
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir)

            for score_player_1 in range(16):
                for score_player_2 in range(16):
                    with self.subTest(f"{score_player_1}, {score_player_2} - {langue}"):
                        file = open(self.make_file_name(score_player_1, score_player_2,langue), "r")
                        attendu = file.read()
                        file.close()
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", langue)
                        self.assertEqual(attendu, sortie)