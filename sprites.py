import pygame
import os
import constantes


RUTA_SPRITES = "sprites"
NUEVO_TAMANO_CARRO = (100, 120)
NUEVO_TAMANO_TROCA = (90, 100)

auto_azul_original = pygame.image.load(os.path.join(RUTA_SPRITES, "carro_azul.png")).convert_alpha()
auto_azul = pygame.transform.scale(auto_azul_original, NUEVO_TAMANO_CARRO)
mask_auto = pygame.mask.from_surface(auto_azul)

troca_original = pygame.image.load(os.path.join(RUTA_SPRITES, "troca.png")).convert_alpha()
troca = pygame.transform.scale(troca_original, NUEVO_TAMANO_TROCA) 
mask_troca = pygame.mask.from_surface(troca)

carretera_original = pygame.image.load(os.path.join(RUTA_SPRITES, "carretera.jpg")).convert()
carretera = pygame.transform.scale(carretera_original, (constantes.ANCHO, constantes.ALTO))