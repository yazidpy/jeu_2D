# la classe des monstres (les ennemis)
import pygame
import random
from comet_event import  CometFallEvent

class Monstre(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.velocity=random.randint(1,3) # vitesse
        self.health=100 # point de vie de monstre
        self.max_health=100
        self.attack=0.3
        self.image=pygame.image.load("PygameAssets-main/mummy.png")
        self.rect=self.image.get_rect() # position de la photo (x,y)
        self.rect.x=1050+random.randint(0,300)
        self.rect.y=460
    # une méthode qui va permettre de subir des dégats
    def damage(self,amount):
     # infliger les dégats
      self.health-=amount
        # véerifier si son nombre de point de vie est inf à 0
      if self.health<=0:
         #réapparaitre comme un nouveau monstre
          self.rect.x=1050+random.randint(0,300)
          self.health=100
          self.velocity=random.randint(1,3)
          #si la barre de l'évenement est chargé alors on reapparaitre pas un monstre

          if self.game.comet_event.is_full_loaded():
            self.game.all_monstre.remove(self)


    def update_health(self,surface):
        # définir une couleur pour la barre
        barre_color=(255,0,0)
        # definier la position de la barre ainsi sa largeur et épaisseur
        bar_position=[self.rect.x+40,self.rect.y-20,self.health,8]
        # dessiner notre bar rect(pour rectangle)
        pygame.draw.rect(surface,barre_color,bar_position)
        # définir une couleur pour l'arriere plan de la jauge
        back_bar_color=(60,63,60)
        back_bar_position=[self.rect.x+40,self.rect.y-20,self.max_health,8]
        pygame.draw.rect(surface,back_bar_color,back_bar_position)
        pygame.draw.rect(surface,barre_color,bar_position)

    def forward(self): # déplacement
        if not self.game.check_collition(self,self.game.all_player):
         self.rect.x-=self.velocity
         # si le monstre est en collision
        else:
            self.game.player.damage_player(self.attack)
