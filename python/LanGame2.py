# -*- coding: utf-8 -*-

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.score_player1  = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == "player1":
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.score_player1  == self.score_player2 and self.score_player1  < 3):
            if (self.score_player1 ==0):
                result = "Love"
            if (self.score_player1 ==1):
                result = "Fifteen"
            if (self.score_player1 ==2):
                result = "Thirty"
            result += "-All"
        if (self.score_player1 ==self.score_player2 and self.score_player1 >2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.score_player1  > 0 and self.score_player2==0):
            if (self.score_player1 ==1):
                P1res = "Fifteen"
            if (self.score_player1 ==2):
                P1res = "Thirty"
            if (self.score_player1 ==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.score_player2 > 0 and self.score_player1 ==0):
            if (self.score_player2==1):
                P2res = "Fifteen"
            if (self.score_player2==2):
                P2res = "Thirty"
            if (self.score_player2==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if (self.score_player1 >self.score_player2 and self.score_player1  < 4):
            if (self.score_player1 ==2):
                P1res="Thirty"
            if (self.score_player1 ==3):
                P1res="Forty"
            if (self.score_player2==1):
                P2res="Fifteen"
            if (self.score_player2==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.score_player2>self.score_player1  and self.score_player2 < 4):
            if (self.score_player2==2):
                P2res="Thirty"
            if (self.score_player2==3):
                P2res="Forty"
            if (self.score_player1 ==1):
                P1res="Fifteen"
            if (self.score_player1 ==2):
                P1res="Thirty"
            result = P1res + "-" + P2res

        if (self.score_player1  > self.score_player2 and self.score_player2 >= 3):
            result = "Advantage player1"

        if (self.score_player2 > self.score_player1  and self.score_player1  >= 3):
            result = "Advantage player2"

        if (self.score_player1 >=4 and self.score_player2>=0 and (self.score_player1 -self.score_player2)>=2):
            result = "Win for player1"
        if (self.score_player2>=4 and self.score_player1 >=0 and (self.score_player2-self.score_player1 )>=2):
            result = "Win for player2"
        return result



    def P1Score(self):
        self.score_player1  +=1


    def P2Score(self):
        self.score_player2 +=1
