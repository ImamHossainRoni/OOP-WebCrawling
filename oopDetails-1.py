class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attact(self, other_guy):
        other_guy.health = other_guy.health - self.damage

roni = Fighter("Roni")
you = Fighter("Imam Hossain")
print(roni.name)
print(you.name)
you.attact(roni)
print(roni.health)