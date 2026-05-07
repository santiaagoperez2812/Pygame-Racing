import pygame
import sys
import random
import constantes
import sprites
import math



class Enemigo:
    def __init__(self, direccion="abajo", otros_enemigos=[]):
        self.direccion = direccion
        self.imagen_original = sprites.troca
        
        if self.direccion == "abajo":
            self.velocidad = random.randint(4, 7)
            self.imagen = pygame.transform.rotate(self.imagen_original, 180)
        else:
            self.velocidad = random.randint(-7, -4)
            self.imagen = self.imagen_original

        self.rect = self.imagen.get_rect() 
        self.mask = pygame.mask.from_surface(self.imagen)
        self.aparecer_sin_colision(otros_enemigos)

    def aparecer_sin_colision(self, otros_enemigos):
        intentos = 0
        while intentos < 50:
            self.rect.x = random.randint(50, constantes.ANCHO - self.rect.width - 50)
            if self.direccion == "abajo":
                self.rect.y = random.randint(-1200, -200)
            else:
                self.rect.y = random.randint(constantes.ALTO + 200, constantes.ALTO + 1200)

            colision = any(otro != self and self.rect.inflate(40, 80).colliderect(otro.rect) 
                          for otro in otros_enemigos)
            if not colision:
                break
            intentos += 1

    def actualizar(self, otros_enemigos):
        self.rect.y += self.velocidad
        fuera = (self.direccion == "abajo" and self.rect.top > constantes.ALTO) or \
                (self.direccion == "arriba" and self.rect.bottom < 0)
        if fuera:
            self.aparecer_sin_colision(otros_enemigos)

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

# ---------------------------------------------------------
# FUNCIONES DE INTERFAZ
# ---------------------------------------------------------

def dibujar_fondo_animado():
    """Función auxiliar para reutilizar el fondo en Menú y Game Over."""
    global fondo_y
    fondo_y = (fondo_y + 2) % constantes.ALTO 
    constantes.ventana.blit(sprites.carretera, (0, fondo_y))
    constantes.ventana.blit(sprites.carretera, (0, fondo_y - constantes.ALTO))
    
    # Capa oscura (Overlay)
    overlay = pygame.Surface((constantes.ANCHO, constantes.ALTO))
    overlay.set_alpha(160) 
    overlay.fill((0, 0, 0)) 
    constantes.ventana.blit(overlay, (0, 0))

def mostrar_menu():
    dibujar_fondo_animado()
    fuente_titulo = pygame.font.SysFont("Arial", 65, bold=True)
    fuente_instrucciones = pygame.font.SysFont("Arial", 30)

    texto_titulo = fuente_titulo.render("NO TE CHOQUES", True, constantes.ROJO)
    rect_titulo = texto_titulo.get_rect(center=(constantes.ANCHO // 2, 180))
    constantes.ventana.blit(texto_titulo, rect_titulo)

    if (pygame.time.get_ticks() // 500) % 2 == 0: 
        texto_inicio = fuente_instrucciones.render("Presiona ESPACIO para Jugar", True, constantes.BLANCO)
        constantes.ventana.blit(texto_inicio, texto_inicio.get_rect(center=(constantes.ANCHO // 2, 350)))

    texto_salir = fuente_instrucciones.render("Presiona Q para Salir", True, (180, 180, 180))
    constantes.ventana.blit(texto_salir, texto_salir.get_rect(center=(constantes.ANCHO // 2, 420)))
    pygame.display.flip()

def mostrar_game_over(puntos_finales):
    """Pantalla de Game Over con fondo animado y opción de salir."""
    dibujar_fondo_animado()
    
    fuente_go = pygame.font.SysFont("Arial", 60, bold=True)
    fuente_res = pygame.font.SysFont("Arial", 30)

    linea1 = fuente_go.render("CHOCASTE", True, constantes.ROJO)
    linea2 = fuente_res.render(f"Puntaje: {puntos_finales}", True, constantes.BLANCO)
    linea3 = fuente_res.render("ESPACIO - Reintentar", True, constantes.BLANCO)
    linea4 = fuente_res.render("Q - Salir", True, (180, 180, 180))

    constantes.ventana.blit(linea1, linea1.get_rect(center=(constantes.ANCHO//2, 180)))
    constantes.ventana.blit(linea2, linea2.get_rect(center=(constantes.ANCHO//2, 280)))
    constantes.ventana.blit(linea3, linea3.get_rect(center=(constantes.ANCHO//2, 360)))
    constantes.ventana.blit(linea4, linea4.get_rect(center=(constantes.ANCHO//2, 420)))
    
    pygame.display.flip()

def crear_enemigos():
    lista = []
    for d in ["abajo", "abajo", "arriba", "arriba"]:
        nuevo = Enemigo(direccion=d, otros_enemigos=lista)
        lista.append(nuevo)
    return lista

# ---------------------------------------------------------
# INICIALIZACIÓN
# ---------------------------------------------------------
pygame.init()
pygame.display.set_caption("Carritos Chistosos")

try:
    carro_player = sprites.auto_azul 
    player_rect = carro_player.get_rect(center=(constantes.ANCHO // 2, constantes.ALTO - 100))
    mask_player = pygame.mask.from_surface(carro_player)
    velocidad_jugador = 6
    enemigos = crear_enemigos()
except Exception as e:
    print(f"Error al cargar recursos: {e}")
    pygame.quit()
    sys.exit()

reloj = pygame.time.Clock()
fondo_y = 0
velocidad_fondo = 5
estado = "MENU"
puntaje = 0
fuente_puntaje = pygame.font.SysFont("Arial", 30, bold=True)

# ---------------------------------------------------------
# GAME LOOP
# ---------------------------------------------------------
ejecutando = True
while ejecutando:
    
    if estado == "MENU":
        mostrar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    estado = "JUGANDO"
                if evento.key == pygame.K_q:
                    ejecutando = False

    elif estado == "GAMEOVER":
        mostrar_game_over(puntaje)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    puntaje = 0
                    player_rect.center = (constantes.ANCHO // 2, constantes.ALTO - 100)
                    enemigos = crear_enemigos()
                    estado = "JUGANDO"
                if evento.key == pygame.K_q:
                    ejecutando = False

    elif estado == "JUGANDO":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        puntaje += 1
        fondo_y = (fondo_y + velocidad_fondo) % constantes.ALTO

        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and player_rect.left > 0:
            player_rect.x -= velocidad_jugador
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and player_rect.right < constantes.ANCHO:
            player_rect.x += velocidad_jugador
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and player_rect.top > 0:
            player_rect.y -= velocidad_jugador
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and player_rect.bottom < constantes.ALTO:
            player_rect.y += velocidad_jugador

        constantes.ventana.blit(sprites.carretera, (0, fondo_y))
        constantes.ventana.blit(sprites.carretera, (0, fondo_y - constantes.ALTO))
        
        for e in enemigos:
            e.actualizar(enemigos)
            e.dibujar(constantes.ventana)
            offset_x = e.rect.x - player_rect.x
            offset_y = e.rect.y - player_rect.y

            if mask_player.overlap(e.mask, (offset_x, offset_y)):
                estado = "GAMEOVER"
                break

        constantes.ventana.blit(carro_player, player_rect)
        texto_puntos = fuente_puntaje.render(f"Puntos: {puntaje}", True, constantes.BLANCO)
        constantes.ventana.blit(texto_puntos, (20, 20))
        
        pygame.display.flip()

    reloj.tick(60)

pygame.quit()
sys.exit()