import pygame
from player import  Player
from  monstre import Monstre
from comet_event import CometFallEvent

# création d'une classe qui va représenter notre jeu
class Game():

     def __init__(self):
       #charger notre joueur
       #définir si notre joueur à commencé ou non
       self.is_playing=False
       self.all_player=pygame.sprite.Group()
       self.player=Player(self)
       self.all_player.add(self.player)
       self.comet_event=CometFallEvent(self) # générer l'évenement
       self.all_monstre = pygame.sprite.Group()
       self.pressed={} # dictionnaire pour enregistrer les touches



     def start(self):
         self.is_playing=True
         self.spawn_monster()
         self.spawn_monster()


     def update(self,surface):

         # appliquer l'image de joueur
         surface.blit(self.player.image, self.player.rect)

         # recuperer les projectiles
         for projectile in self.player.all_projectiles:
             projectile.move_projectile()

         # recuperer les monstres
         for monstre in self.all_monstre:
             monstre.forward()
             monstre.update_health(surface)

         #actualiser la barre de vie
         self.player.update_health_player(surface)

         # actualiser la barre d'évenement de jeu
         self.comet_event.update_bar(surface)

         # appliquer l'ensemble des images de groupe de projectiles
         self.player.all_projectiles.draw(surface)
         # appliquer l'ensemble des images de groupe de monstres
         self.all_monstre.draw(surface)


         # verifier si le joueur souhaite aller à gauche ou droite
         if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width <= surface.get_width():
             self.player.move_right()

         elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
             self.player.move_left()

         elif self.pressed.get(pygame.K_a):
             self.player.launch_projectile()

         #dessiner mes images de comets
         self.comet_event.all_comets.draw(surface)
         # récuperer mes comtes
         for comet in self.comet_event.all_comets:
             comet.fall()


     def spawn_monster(self):
         monstre=Monstre(self)
         self.all_monstre.add(monstre)


     def check_collition(self,sprite,group): # comparison entre une entité et un groupe
         # le 3eme élement est ce que on tue l'objet courant
         # le 4eme ,type de collition
         return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)


     def game_over(self):
         self.all_monstre=pygame.sprite.Group()
         self.comet_event.all_comets=pygame.sprite.Group()
         self.comet_event.recet_percent()
         self.player.health=self.player.max_health
         self.is_playing = False




