import pygame
# la classe qui va gérer la projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.velocity=5
        self.player=player
        self.image=pygame.image.load("PygameAssets-main/projectile.png")
        self.rect= self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect.x=player.rect.x+120
        self.rect.y=player.rect.y+80
        self.origine=self.image
        self.angle=0
    def rotate(self):
        # tourner le projectile
        self.angle+=6
        self.image=pygame.transform.rotozoom(self.origine,self.angle,1)

    def remove_projectile(self):
        self.player.all_projectiles.remove(self)

    def move_projectile(self):
        self.rect.x+=self.velocity
        self.rotate()

        # si le projectile entre en collision avec un monstre il se supprime
        # il faut connaitre les monstres qui ont fait des collision avec projectile
        for monstre in  self.player.game.check_collition(self,self.player.game.all_monstre):
            self.remove_projectile()
            # infliger des dégats
            monstre.damage(self.player.attack)

        if self.rect.x>1240:
        #supprimer le projectile sortie
          self.remove_projectile()

