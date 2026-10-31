class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def take_damage(self, damage):
        self.hp = self.hp - damage
        print(f'Игрок {self.name} получил {damage} урона. Осталось {self.hp} HP.')

    def heal(self, amount):
        self.hp = self.hp + amount
        print(f'Игрок {self.name} излечился на {amount} HP. Теперь его здоровье {self.hp} HP')

p1 = Player('Егор', 100)
p2 = Player('Enemy', 80)

p1.take_damage(20)
p1.heal(15)
p2.take_damage(50)