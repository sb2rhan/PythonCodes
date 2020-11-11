class Player(object):

    def __init__(self, name, heroes):
        self.name = name
        self.heroes = heroes

    def start_game(self, enemy_player):
        print(f'{self} starts to attack:')

        self.refresh_heroes()

        if len(self.heroes) == 0:
            return False

        for hero in self.heroes:
            for enemy_hero in enemy_player.heroes:
                status = hero.attack(enemy_hero)
                if status == False:
                    print(f'\t{enemy_hero} is dead ☠')
                    enemy_player.refresh_heroes()
                else:
                    print(f'\t{enemy_hero} is alive')

    def refresh_heroes(self):
        new_heroes = []
        for hero in self.heroes:
            if hero.hp > 0:
                new_heroes.append(hero)
        self.heroes = new_heroes

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Player: {self.name}, heroes alive: {self.heroes}'
