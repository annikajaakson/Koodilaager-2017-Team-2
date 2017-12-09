class Bullet:
    def __init__(self):
        self.bullet_speed = 500
        self.bullet_lifetime = 500
        self.rect = pygame.Rect([self.x, self.y, 1, 1])
        self.x = x
        self.y = y

    def bullet_kill(self, opilane):
        if opilane.x == self.x and opilane.y == self.y:
            self.bullet_lifetime = 0

    