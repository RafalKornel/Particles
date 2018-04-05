class Particle:    
    def __init__(self, _pos):
        self.pos = _pos                                    # POSITION
        self.lastPos = PVector(self.pos.x, self.pos.y)     # PREVIOUS FRAME POSITION, NECCESARY TO DRAW CONTINUOUS LINE
        self.vel = PVector(random(-2, 2), random(-2, 2))   # VELOCITY
        self.acc = PVector()                               # ACCELERATION
        self.r = random(1, 10)                             # RADIUS, USED IN STROKEWEIGHT
        self.g = 5                                         # GRAVITATIONAL CONSTANT PLACEHOLDER
        self.mass = 1                                      # MASS                    
        #self.col = color(random(255), 255, 255) # <- HSB  # COLOR
        self.col = color(random(255), random(255), random(255), random(255)) # <- RGB                
        
    def update(self):                                      # UPDATES POSITION, VELOCITY AND CHCECKS COLLISION WITH BORDERS                          
        self.pos += self.vel   
        self.vel += self.acc
        self.acc.mult(0)
        self.collision()
        self.col += 1
                
    
    def show(self):                                        # DRAWS PARTICLE
        colorMode(RGB)
        stroke(self.col)
        strokeWeight(self.r)                               # MORE STROKEWEIGHT WITH CLEAR FUNCTION MAKES PARTICLES LOOK BLURRY
        
        line(self.lastPos.x, self.lastPos.y, self.pos.x, self.pos.y) 
        
        self.lastPos.x = self.pos.x                        # ASSIGN CURRENT POSITION TO LAST POSITION 
        self.lastPos.y = self.pos.y                        # IN ORDER TO DRAW LINE BETWEEN TWO NEIGHBOUR POINTS
        
        
        #fill(self.col)                                    # THIS CHUNK DRAWS PARTICLE AS A ELLIPSE (CIRCLE)
        #ellipse(self.pos.x, self.pos.y, self.r, self.r)
        
    
    
    def collision(self):                                   # COLLISION WITH BORDER DETECTION
        if self.pos.x >= width or self.pos.x <= 0:
            if self.pos.x <= 0:
                self.pos.x = 1
            else:
                self.pos.x = width - 1
            self.vel.x *= -0.8
            self.acc.x = 0# *= 0.51
        if self.pos.y >= height or self.pos.y <= 0:
            if self.pos.y <= 0:
                self.pos.y = 1
            else:
                self.pos.y = height - 1
            self.vel.y *= -0.8
            self.acc.y = 0#*= 0.51
    
    def attract(self, target):                            # FORCE ATTRACTING PARTICLES TO 'HOLES'
        dis = target.pos - self.pos  
        rSq = dis.magSq()
        if rSq != 0:                                      # PREVENTING FROM DIVIDING BY ZERO       
            force =  self.g * self.mass * target.mass / rSq    # F = G(m1 * m2) / r^2
            force = constrain(force, -2, 10)               # KEEPS FORCES IN RESONABLE COMPARTMENT
            self.acc += dis * force
                                                                
                                                   
            # if dis.mag() <= 2:                          # PUSHES PARTICLE AWAY IF MOVED TOO CLOSE
            #     self.vel *= -0.8
            #     self.acc = dis * force * -1
            # else:
            #     self.acc = dis * force             
                                                  
        #_col = map(dis.mag(), 0, width/2, 255, 0)        # MAPS PARTICLE COLOR TO DISTANCE 
        #self.col = color(_col, 255, 255)     
        
            
class Hole:                                               # HOLE OBJECT IS BASICALLY POINT WHICH INTERACTS WITH PARTICLE WITH GRAVITATIONAL FORCE        
    def __init__(self, _pos, _mass = 3, _radius = 3):
        self.pos = _pos                                   # POSITION OF 'HOLE'
        self.mass = _mass                                 # MASS
        self.r = _radius                                  # RADIUS, USED FOR DRAWING
    
    def show(self):
        stroke(0)
        fill(0)
        ellipse(self.pos.x, self.pos.y, self.r, self.r)
