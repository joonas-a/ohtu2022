class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def check_nationality(self, player, nationality):
        return player.nationality == nationality

    def top_scorers_by_nationality(self, nationality):
        arr = [p for p in self.reader.players if self.check_nationality(p, nationality)]

        return sorted(arr, key=lambda player : player.assists+player.goals, reverse=True)
