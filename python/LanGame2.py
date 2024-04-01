# -*- coding: utf-8 -*-

class TennisGame2:
    SCORE_NAMES_EN = ["Love", "Fifteen", "Thirty", "Forty"]
    SCORE_NAMES_FR = ["Zéro", "Quinze", "Trente", "Quarante"]

    def __init__(self, player1Name, player2Name, language):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.score_player1 = 0
        self.score_player2 = 0
        self.language = language

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.score_player1 += 1
        elif playerName == self.player2Name:
            self.score_player2 += 1
        else:
            raise ValueError("Player name is not recognized")

    def score(self):
        if self.is_deuce():
            return "Deuce" if self.language == 'EN' else "Égalité"
        if self.is_advantage():
            player_advantage = self.advantage_player()
            return f"Advantage {player_advantage}" if self.language == 'EN' else f"Avantage {player_advantage}"
        if self.is_win():
            player_winner = self.winning_player()
            return f"Win for {player_winner}" if self.language == 'EN' else f"Victoire pour {player_winner}"
        return self.current_score()

    def is_deuce(self):
        return self.score_player1 >= 3 and self.score_player1 == self.score_player2

    def is_advantage(self):
        return abs(self.score_player1 - self.score_player2) == 1 and max(self.score_player1, self.score_player2) >= 4

    def is_win(self):
        return abs(self.score_player1 - self.score_player2) >= 2 and max(self.score_player1, self.score_player2) >= 4

    def advantage_player(self):
        return self.player1Name if self.score_player1 > self.score_player2 else self.player2Name

    def winning_player(self):
        return self.player1Name if self.score_player1 > self.score_player2 else self.player2Name

    def current_score(self):
        score_names = self.SCORE_NAMES_EN if self.language == 'EN' else self.SCORE_NAMES_FR
        score_p1 = score_names[min(self.score_player1, 3)]
        score_p2 = score_names[min(self.score_player2, 3)]
        if self.score_player1 == self.score_player2:
            return f"{score_p1}-All" if self.language == 'EN' else f"{score_p1}-A" if self.score_player1 < 3 else "Deuce" if self.language == 'EN' else "Égalité"
        return f"{score_p1}-{score_p2}"
