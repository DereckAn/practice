import pygame
import neat
import time 
import os       # Creo que esto es para acceder a los archivos de la pc 
import random   # to random place the tubes 
pygame.font.init() # esto es para escribir en la pantalla 

WIN_WIDTH = 600
WIN_HEIGHT = 800

gen = 0

# Esta es una lista para cargar las imagenes de una carpeta. Es una lista porque son varias imagenes para simular que el pajaro esta volando. 
BIRD_IMGS = [ pygame.transform.scale2x( pygame.image.load(  os.path.join("imgs", "bird1.png")) ), pygame.transform.scale2x( pygame.image.load(  os.path.join("imgs", "bird2.png")) ),  pygame.transform.scale2x( pygame.image.load(  os.path.join("imgs", "bird3.png")) ) ]

# This code is to load the pipes images. As you can see, the pipes do not need animation that is why it is just one single image. 
PIPIE_IMGS = pygame.transform.scale2x( pygame.image.load(  os.path.join("imgs", "pipe.png") ) )

# To load the base or el suelo. Tierra 
BASE_IMG = pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs", "base.png")))

# To load the background. Se refiera al cielo
BG_IMG = pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs", "bg.png")))

# To see the score top right corner of the screen
STAT_FONT = pygame.font.SysFont("comicsans", 50)



# To start we create the bird class because we are going to create several birds for our A.I
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25  # Esto es para ver cuando rotaremos la imagen del pajara para dar la apariencia de que esta yedno hacia arriba o hacia abajo. 
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5 # esto es para ver cuantas veces se cambia el pajara por frame
    
    
    
    def __init__(self,x,y): # Este es el constructor. x y representan la posicion inicial del pajaro 
        self.x = x
        self.y = y
        self.tilt = 0 # Esto es para ver la inclinacion del pajaro. 0 para que el pajaro este perfectamente horizontal. 
        self.tick_count = 0
        self.vel = 0 # velocidad del pajaro. 0 porque no se esta moviendo 
        self.height =  self.y
        self.img_count = 0
        self.img = self.IMGS[0]
        
        
        
    def jump(self):
        self.vel = -10.5 # esto espara que el pajaro vaya hacia abajo 
        self.tick_count = 0 # Esto es para saber nuestro ultimo salto. Es para saber cuando cambiar direccion o para cambiar velocidades 
        self.height = self.y # where the bird jump from. Para saber de donde salto el pajaro. De donde nos empezamos a mover 
    
    
    
    def move(self):
        self.tick_count += 1 # Esto representara el tiempo. Cuantos segundos nos estaremos moviendo 
        
        d = self.vel * self.tick_count + 1.5 * self.tick_count**2   # Dependiendo de la velocidad calculara cuanto nos moveremos hacia arriba o hacia abajo 
        
        if d>=16:
            d = 16
        if d < 0:
            d -= 2
            
        self.y = self.y + d # esto es para calcular moverse despacio hacia arriba o despacio hacia abajo 
        
        if d < 0 or self.y < self.height + 50 : # Esto es para inclinar al pajaro. Para que no se incline al instante al caer 
            if self.tilt < self.MAX_ROTATION: # Esto es para que cuando saltemos se incline para arriba con un angulo de 25 grados
                self.titl = self.MAX_ROTATION
        else:
            if self.tilt > -90: # Esto es para si el pajara esta cayendo ,uy rapido, va a inclinar la imagen para que sea totalmente vertical. 
                self.tilt -= self.ROTATION_VELOCITY
        
        
        
    def draw(self, win):
        self.img_count += 1
        
        #Esto es para saber que imagen mostrar dependiendol contador de imagenes 
        if self.img_count < self. ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4+1:
            self.img = self.IMGS[0]
            self.img_count = 0
            
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
            
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center) # no sabe bein lo que hace. Solo se que rota la imagen en base al centro. 
        win.blit(rotated_image, new_rect.topleft)
        
        
        
    def get_mask(self):  # Este metodo es para crear una matris de la imagen y asi poder crear un caja de colicion mas certera 
        return pygame.mask.from_surface(self.img)
        
'''--------------------------------------------------------------------------------------------------------------------------------------------------------'''       
 
class Pipe:
    GAP =  200 # El espacio entre los tubos
    VEL = 5
    
    def __init__(self, x):
        self.x = x
        self.height = 0
        
        self.top = 0 # variables para saber el limite de donde estaran los tubos de arriba
        self.bottom = 0  # variables para saber el limite de donde estaran los tubos de abajo
        self.PIPE_TOP = pygame.transform.flip(PIPIE_IMGS, False, True)
        self.PIPE_BOTTOM = PIPIE_IMGS
        
        self.passed = False # Esto es for collition purposes y para la inteligencia artificial despues 
        self.set_height()  # Este metodo es para saber donde estan los tubos y que tan altos son, y donde estael gap (espacio dond psara el pajaro)
        
    
    def set_height(self): #Este es para que los tubos tenga un a cierta altura. 
        self.height = random.randrange(50,450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP
        
    def move(self): # Esto es para quelos tubos se muevan 
        self.x -= self.VEL
    
    def draw(self, win):  # este es para dibujar los tubos uno arriba del otro 
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        
    def collide(self, bird): # Hacer las coliciones
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        b_point = bird_mask.overlap(bottom_mask, bottom_offset) # esto es para saber si collicionan. Si las mascaras se sobreponen. # Si no colicionan regresan un NONE
        t_point = bird_mask.overlap(top_mask, top_offset)
        
        if t_point or b_point: # Esto es para checar si existen las collisiones. 
            return True
        return False
    
    
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
            
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
    
    
        
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''        
def draw_window(win, birds, pipes, base, score, gen):
    win.blit(BG_IMG, (0,0))
    
    for pipe in pipes:  # Esto es para crear y mostrar los tubos
        pipe.draw(win)
        
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    
    text = STAT_FONT.render("Gen: " + str(gen), 1, (255,255,255))
    win.blit(text, (10, 10))
    
    base.draw(win) #  Esto es para crear y mostrar la base o el piso 
    
    for bird in birds:
        bird.draw(win)
        
    pygame.display.update()
    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''    
def main(genomes, config):
    global gen
    gen += 1
    # bird = Bird(230,350)
    birds = []
    nets = []
    ge = []
    
    for genome_id, g in genomes:   # ponemos el _, g  porque genomes es una tupla y tiene el indice junto con el denoma pero nosotros solo queremos el genoma 
        g.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(g,config) # este es el metodo que hace el genoma. CREO
        nets.append(net)
        birds.append(Bird(230,350))
        ge.append(g)
        
        
    base = Base(730)
    pipes = [Pipe(700)]
    score = 0
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()  # esto tiene el proposito de alentar un poco el proceso 
    
    run = True
    while run and len(birds) > 0:
        clock.tick(30)  # 30 tick por segundo 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Esto significa que cuando apretemos la "x" de la ventana vamos a salir del juego 
                run = False
                pygame.quit()
                quit()
                break
    
                
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
            else:
                run = False
                break
                
        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1  # Cada que el pajaro sobreviva por 30 en un segundo ganara 0.1 fitness puntos   //  Esto motiva alpajaro a estar vivo 
            
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            
            if output[0] > 0.5:
                bird.jump()
                
        base.move() 
        add_pipe = False
        rem = []
        
        for pipe in pipes:
            pipe.move()
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1 # Cada vez que un pajaro choque removera un de su fitness score. 
                    # birds.remove(bird) # Esto solo removera el objeto pajaro
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)
                    
            
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True    
                    
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
                
            
        if add_pipe: # Esta parte es para cuando el pajaro pase exitosamente en medio de los tubos. 
            score += 1                        
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))
        
        for r in rem:
            pipes.remove(r)
           
        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0: # Esta parte es para ver si el pajaro todo el piso  # Ahora con el forloop checamos si muchos pajaros chocan con el piso y para que muera con el cielo 
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
                
        
              
        base.move() 
        draw_window(win, birds, pipes, base, score, gen) 
                   

       
    

def run(confif_path):
    # import pickle
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, confif_path)
    
    p = neat.Population(config) # Para crear la population
    
    p.add_reporter(neat.StdOutReporter(True)) # Dice que esto nos da unas estadisticas. 
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    winner = p.run(main,10) # Aqui llamaremos a la funcion main 0 veces y pasara todos los genes 
    


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)       # Nos dara la direccion del archivo en el que estamos actualmente. 
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
    
    
        
          
 

