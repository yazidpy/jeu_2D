import pygame
from projectile import  Projectile
# classe player
class Player(pygame.sprite.Sprite): # la classe de base de tout les élements visible

    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health=100 # la durée de vie de joueur
        self.max_health=100
        self.attack=20
        self.velocity=4 #vitesse de déplacement
        self.all_projectiles=pygame.sprite.Group() # ranger chaque projectile dans un group
        self.image=pygame.image.load("PygameAssets-main/player.png")
        self.rect =self.image.get_rect()
        self.rect.x=0
        self.rect.y=420



    def launch_projectile(self):
     #créer des instance de la classe projectile
      self.all_projectiles.add(Projectile(self))


    def move_right(self):
       # vérification si en collision avec un monstre
       if not self.game.check_collition(self,self.game.all_monstre):
         self.rect.x+=self.velocity


    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_player(self, surface):
        # définir une couleur pour la barre
        barre_color = (255, 210, 46)
        # definier la position de la barre ainsi sa largeur et épaisseur
        bar_position = [self.rect.x+45 , self.rect.y , self.health, 8]
        # dessiner notre bar rect (pour rectangle)
        pygame.draw.rect(surface, barre_color, bar_position)
        # définir une couleur pour l'arriere plan de la jauge
        back_bar_color = (60, 63, 60)
        back_bar_position = [self.rect.x+45, self.rect.y, self.max_health, 8]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, barre_color, bar_position)

    def damage_player(self,amount):
         if self.health-amount>amount:
            self.health-=amount
            # si le joueur n'a plus de point de vie
         else:
             # remettre le jeu à zéro ,
             self.game.game_over()


