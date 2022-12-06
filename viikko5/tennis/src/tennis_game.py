class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def _get_even_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        elif self.m_score1 == 3:
            return "Forty-All"
        else:
            return "Deuce"

    def _find_who_has_lead(self):
        score_difference = self.m_score1 - self. m_score2
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_player_score(self, player_name):
        if player_name == self.player1_name:
            score = self.m_score1
        elif player_name == self.player2_name:
            score = self.m_score2

        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_even_score()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._find_who_has_lead()

        return self._get_player_score(self.player1_name) + "-" + self._get_player_score(self.player2_name)
