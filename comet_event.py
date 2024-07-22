import pygame
from comet import Comet
class CometFallEvent:
    def __init__(self,game):
        super().__init__()
        self.percent=0
        self.progress=33
        # définir un groupe de sprite pour stocker nos comets
        self.all_comets=pygame.sprite.Group()
        self.game=game
        self.fall_mode=False # attemp de fall

    def add_percent(self):
        self.percent+=self.progress/100
    def is_full_loaded(self):# si la barre est totalement chargée
         return  self.percent>=100

    def recet_percent(self):
        self.percent=0

    def meteor_fall(self):
        # boucle pour apparaitre bcp de comets
        for i in range(1,10):
          self.all_comets.add(Comet(self))


    def attemp_fall(self):#la pluit de comet
        if self.is_full_loaded() and len(self.game.all_monstre)==0: # que il n'y plus de monstre
            self.recet_percent()
            self.meteor_fall()
            self.fall_mode=True # activier l'évenement


    def update_bar(self,surface):
        self.add_percent()
        #appell de la méthode pour déclencher de la pluit
        self.attemp_fall()
        pygame.draw.rect(surface, (0,0,0), [
            0 ,
            surface.get_height()-15 ,
            surface.get_width(),
            10])
        pygame.draw.rect(surface,(255,0,0),[
            0,
            surface.get_height()-15,
            (surface.get_width()/100)*self.percent,
            10])


