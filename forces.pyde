# CREATED IN PROCCESSING.PY, PYTHON VERSION OF PROCESSING -> http://py.processing.org/
# INSPIRED BY DANIEL STIFFMAN'S YOUTUBE CHANNEL -> CODING TRAIN
# CHANNEL -> https://www.youtube.com/thecodingtrain
# VIDEO / TUTORIAL ABOUT ATTRACTION AND REPULSION FORCES -> https://www.youtube.com/watch?v=OAcXnzRNiCY


from particle import Particle
from particle import Hole

particles = []               # MAIN PARTICLES ARRAY
holes = []                   # MAIN 'HOLES' ARRAY -> HOLE OBJECT IS BASICALLY 
                             # POINT WHICH INTERACTS WITH PARTICLE WITH GRAVITATIONAL FORCE

holesCount = 2               # SPECIFIES THE NUMBER OF 'HOLES'
particlesCount = 100

def setup():
    global count    
    global hole
    global particles

    frameRate(60)
    size(1300, 700)           # SIZE OF THE WINDOW

    
    for j in range (holesCount):                                          # GENERATES HOLES RANDOMLY
        holes.append(Hole(PVector(random(width), random(height))))
    
    for i in range(particlesCount):                                       # GENERATES PARTICLES RANDOMLY
        particles.append(Particle(PVector(random(width), random(height))))


def draw():
    
    clear()                  # CLEARING WINDOW EVERY FRAME
    background(51)           # COMMENT BOTH LINES TO MAKE TRAILS EFFECT
    
    for par in particles:    # MAIN LOOP, APPLIES FORCES TO THE PARTICLE, THEN DRAWS IT
        for hole in holes:
            par.attract(hole)        
        par.update()
        par.show()   
        
    for hole in holes:       # DRAWS ALL OF THE HOLES
        hole.show()
    
                             # THIS PART CREATES PARTICLES WHEN MOUSE BUTTON IS PRESSED 
    # if mousePressed == True:
    #     if frameCount % 2 == 0:
    #         global count
    #         count += 1
    #         if mouseX != 0 and mouseY != 0:
    #             particles.append(Particle(PVector(mouseX, mouseY)))
    
                              
                             # ALLOWS USER TO MOVE ONE OF THE 'HOLES'                                           
    # holes[0].pos.x = mouseX 
    # holes[0].pos.y = mouseY            
                
                
    
        

    

    
