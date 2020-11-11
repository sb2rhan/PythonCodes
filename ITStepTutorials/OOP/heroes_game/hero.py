class Hero(object):

    def __init__(self, name: str, hp: int, dmg: int):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    
    def attack(self, target):
        print(f'\t{self} 🗡 —> {target} and damaged {self.dmg}')
        return target.get_dmg(self.dmg)

    def get_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            return False  # if dead
        return True       # if alive

    def __repr__(self):
        return f'Hero - {self.name}, HP: {self.hp}, Damage: {self.dmg}'

    def __str__(self):
        return f'{self.name}: hp - {self.hp}'
