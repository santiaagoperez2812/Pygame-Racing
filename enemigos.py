import pygame
import random
import constantes
import sprites

class Enemigo:
    def __init__(self, direccion="abajo"):
        self.imagen_original = sprites.troca
        self.direccion = direccion
        if self.direccion == "abajo":
            self.velocidad = random.randint(3, 7)
            self.imagen = self.imagen_original 

        else:
            self.velocidad = random.randint(-7, -3)
            self.imagen = pygame.transform.flip(self.imagen_original, False, True)

        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, constantes.ANCHO - self.rect.width)
        
 
        if self.direccion == "abajo":
            self.rect.y = random.randint(-600, -100)
        else:
            self.rect.y = random.randint(constantes.ALTO, constantes.ALTO + 500)

        self.mask = pygame.mask.from_surface(self.imagen)

    def actualizar(self):
        self.rect.y += self.velocidad
        
      
        if self.direccion == "abajo" and self.rect.top > constantes.ALTO:
            self.rect.y = random.randint(-300, -100)
            self.rect.x = random.randint(0, constantes.ANCHO - self.rect.width)
            
      
        elif self.direccion == "arriba" and self.rect.bottom < 0:
            self.rect.y = random.randint(constantes.ALTO, constantes.ALTO + 300)
            self.rect.x = random.randint(0, constantes.ANCHO - self.rect.width)

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)