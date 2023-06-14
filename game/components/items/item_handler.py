from game.components.items.item_skin  import ItemSpeed

class ItemHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(ItemSpeed())
        

    def update(self):
        for enemy in self.enemies:
            enemy.update()
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)