class Player:

    def tournaments(self, game_id):
        return Tournament.query.filter(game_id=game_id, user_id=self.id).all()


class Tournament:
    ...


player = Player(id=1)
print(player.tournaments(1))
