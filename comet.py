import comet_event
import pygame
import random

class Comet(pygame.sprite.Sprite):# définir que cette classe est un élement graphique
    def __init__(self,comet_event):
        super().__init__()
        self.image=pygame.image.load("PygameAssets-main/comet1.png")
        # redémensioner
        self.rect=self.image.get_rect()# récuperer le rectange de l'image
        self.velocity=random.randint(1,3)
        self.rect.x=random.randint(0,1240)
        self.comet_event=comet_event
        self.attack_comet=20

    def remov(self):
        self.comet_event.all_comets.remove(self)
        if len(self.comet_event.all_comets)==0:
            self.comet_event.recet_percent()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y+=self.velocity
        # si la comet tombe sur sol elle sera supprimée
        if self.rect.y>= 500:
            self.remov()
            # vérifier la boule touche le joueur
        if self.comet_event.game.check_collition(self,self.comet_event.game.all_player):
            self.remov()
            self.comet_event.game.player.damage_player(self.attack_comet)



