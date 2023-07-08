# made by mohamed salem aladel

import math
from random import randint, random
import pygame
from pygame import mixer


pygame.init()
mixer.init()

#Load audio file
bg= mixer.music.load('song1.mp3')
#zombie_sounds=[pygame.mixer.Sound("assets\sounds\zombie1.mp3"),pygame.mixer.Sound("assets\sounds\zombie2.mp3")]
shooting_sound=pygame.mixer.Sound("assets\sounds\shoot.wav")
zombie_dead_sound=pygame.mixer.Sound("assets\sounds\deadz.mp3")
# levelup_sound=pygame.mixer.Sound("assets\sounds\up.wav")
lost_sound=pygame.mixer.Sound("assets\sounds\lost.wav")
# dead_sound=pygame.mixer.Sound("assets\sounds\dead.mp3")

#Set preferred volume
mixer.music.set_volume(0.7)
mixer.Sound.set_volume(shooting_sound,0.1)
mixer.Sound.set_volume(zombie_dead_sound,0.3)
mixer.Sound.set_volume(lost_sound,0.3)

# VARIABELS
SCREEN_WID=1280
SCREEN_HIGHT=640
WHITE=(254,254,254)
RED=(254,0,0)
GREEN=(0,254,0)
font_small=pygame.font.SysFont('Lucida Sans',20)
font_big=pygame.font.SysFont('Lucida Sans',24)
screen= pygame.display.set_mode((SCREEN_WID,SCREEN_HIGHT))
pygame.display.set_caption('survival')
spons=[(-100,300),(-200,400),(-300,700),(1700,300),(1600,400),(1600,700),(200,1000),(600,900),(1000,870)]

is_start_screen=True
is_game_over=False
is_playing=False

#set frame rate
clock=pygame.time.Clock()
clockevent=pygame.time.Clock()

fps=60
temp_img=pygame.image.load('assets/screens/start_screen.png')
start_img=pygame.transform.scale(temp_img,(SCREEN_WID,SCREEN_HIGHT))
over_img=pygame.image.load('assets/screens/over_screen.png')
levelup_img=pygame.image.load('level up.png').convert_alpha()
temp_img=pygame.image.load('assets/objects/fireball.png').convert_alpha()
fireball_img=pygame.transform.scale(temp_img,(15,15))
lvl1_bg= pygame.image.load('BG1.png').convert_alpha()
lvl2_bg= pygame.image.load('game_background_4_2.png').convert_alpha()
lvl3_bg= pygame.image.load('BG3.png').convert_alpha()
def playmusic():
    print("music started playing....")
    #Play the music
    mixer.music.play(loops=5)
def sounds_handling():
    zombie_dead_sound.play
    pass


#animations
hero_run = [pygame.image.load("assets/hero/Run-Sheet/texture_0_0.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_1.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_2.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_3.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_4.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_5.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_6.png"),
pygame.image.load("assets/hero/Run-Sheet/texture_0_7.png")]

hero_idle = [pygame.image.load("assets/hero/Idle-Sheet/texture_0_0.png"),
pygame.image.load("assets/hero/Idle-Sheet/texture_0_1.png"),
pygame.image.load("assets/hero/Idle-Sheet/texture_0_2.png"),
pygame.image.load("assets/hero/Idle-Sheet/texture_0_3.png"),
pygame.image.load("assets/hero/Idle-Sheet/texture_0_4.png"),
pygame.image.load("assets/hero/Idle-Sheet/texture_0_5.png"),
pygame.image.load("assets/hero/Idle-Sheet/texture_0_6.png")
]

hero_fireball = [pygame.image.load("assets/hero/Fireball/texture_0_0.png"),
pygame.image.load("assets/hero/Fireball/texture_0_1.png"),
pygame.image.load("assets/hero/Fireball/texture_0_2.png"),
pygame.image.load("assets/hero/Fireball/texture_0_3.png"),
pygame.image.load("assets/hero/Fireball/texture_0_4.png"),
pygame.image.load("assets/hero/Fireball/texture_0_5.png"),
pygame.image.load("assets/hero/Fireball/texture_0_6.png"),
pygame.image.load("assets/hero/Fireball/texture_0_7.png")
]

hero_death = [pygame.image.load("assets/hero/Death-Sheet/texture_0_0.png"),
pygame.image.load("assets/hero/Death-Sheet/texture_0_1.png"),
pygame.image.load("assets/hero/Death-Sheet/texture_0_2.png"),
pygame.image.load("assets/hero/Death-Sheet/texture_0_3.png"),
pygame.image.load("assets/hero/Death-Sheet/texture_0_4.png"),
pygame.image.load("assets/hero/Death-Sheet/texture_0_5.png")]

zombie_man_run = [pygame.image.load("assets/enemys/zombie_man/Run/texture_0_0.png"),
pygame.image.load("assets/enemys/zombie_man/Run/texture_0_1.png"),
pygame.image.load("assets/enemys/zombie_man/Run/texture_0_2.png"),
pygame.image.load("assets/enemys/zombie_man/Run/texture_0_3.png"),
pygame.image.load("assets/enemys/zombie_man/Run/texture_0_4.png"),
pygame.image.load("assets/enemys/zombie_man/Run/texture_0_5.png"),
pygame.image.load("assets/enemys/zombie_man/Run/texture_0_6.png")]
zombie_man_attack = [pygame.image.load("assets/enemys/zombie_man/Attack_1/texture_0_0.png"),
pygame.image.load("assets/enemys/zombie_man/Attack_1/texture_0_1.png"),
pygame.image.load("assets/enemys/zombie_man/Attack_1/texture_0_2.png"),
pygame.image.load("assets/enemys/zombie_man/Attack_1/texture_0_3.png"),
pygame.image.load("assets/enemys/zombie_man/Attack_1/texture_0_4.png")]
zombie_man_dead = [
pygame.image.load("assets/enemys/zombie_man/Dead/texture_0_0.png"),
pygame.image.load("assets/enemys/zombie_man/Dead/texture_0_1.png"),
pygame.image.load("assets/enemys/zombie_man/Dead/texture_0_2.png"),
pygame.image.load("assets/enemys/zombie_man/Dead/texture_0_3.png"),
pygame.image.load("assets/enemys/zombie_man/Dead/texture_0_4.png")
]
zombie_women_run = [pygame.image.load("assets/enemys/zombie_women/Run/texture_0_0.png"),
pygame.image.load("assets/enemys/zombie_women/Run/texture_0_1.png"),
pygame.image.load("assets/enemys/zombie_women/Run/texture_0_2.png"),
pygame.image.load("assets/enemys/zombie_women/Run/texture_0_3.png"),
pygame.image.load("assets/enemys/zombie_women/Run/texture_0_4.png"),
pygame.image.load("assets/enemys/zombie_women/Run/texture_0_5.png"),
pygame.image.load("assets/enemys/zombie_women/Run/texture_0_6.png")]
zombie_women_attack = [pygame.image.load("assets/enemys/zombie_women/Attack_1/texture_0_0.png"),
pygame.image.load("assets/enemys/zombie_women/Attack_1/texture_0_1.png"),
pygame.image.load("assets/enemys/zombie_women/Attack_1/texture_0_2.png"),
pygame.image.load("assets/enemys/zombie_women/Attack_1/texture_0_3.png")]

enemy_types=[[zombie_man_attack,zombie_man_run,zombie_dead_sound],[zombie_women_attack,zombie_women_run,zombie_man_dead]]

levels=[{
    "lvl" : 1,
    "max" : 4,
    "end_points":100,
    "image":lvl1_bg
},
{
    "lvl" : 2,
    "max" : 7,
    "end_points":200,
    "image":lvl2_bg
},
{
    "lvl" : 1,
    "max" : 10,
    "end_points":300,
    "image":lvl3_bg
}

]


#code
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y


def getdir(x):
    (mx,my)=pygame.mouse.get_pos()
    if x>mx:
        return True
    else:
        return False    
    

class Player():
    def __init__(self,x,y) :
        self.image=hero_idle
        self.health=100
        self.width=15
        self.height=55
        self.speed=7
        self.x=x
        self.y=y
        self.rect=pygame.Rect(0 , 0 ,self.width,self.height)
        self.rect.center=(x,y)
        self.stamina=1700
        self.pre_stamina=self.stamina
        self.flipped=False
        self.gun=gun(50,3,10,3,RED)
        self.limt=15
        self.frmlimt=3
        self.frame=0
        self.is_attacking=False
        self.iswalking=False
        self.isJump = False
        self.jumpCount = 10

    def move(self):

        key=pygame.key.get_pressed()
        mouse= pygame.mouse.get_pressed()
        if mouse[0]:
            self.limt-=1
            if self.limt==0:
                self.shoot()
                self.limt=20
           

            


        if self.rect.x>=19 and (key[pygame.K_a] or key[pygame.K_LEFT]):
            self.iswalking=True
            
            self.flipped=True
            if self.rect.x+bg_img.x<SCREEN_WID*0.33 and self.rect.x>SCREEN_WID*0.33:
                bg_img.x+=self.speed
            else:
                self.rect.x-=self.speed
            
        if self.rect.x<=1140 and (key[pygame.K_d] or key[pygame.K_RIGHT]):
            self.iswalking=True
            
            self.flipped=False
            if self.rect.x+bg_img.x>SCREEN_WID*0.33:
                bg_img.x-=self.speed
            else:
                self.rect.x+=self.speed


        if  (key[pygame.K_s] or key[pygame.K_DOWN])and self.rect.y<SCREEN_HIGHT -100:
            self.iswalking=True
            self.rect.y+=self.speed

        if  (key[pygame.K_w] or key[pygame.K_UP]) and self.rect.y>220:
            self.iswalking=True
            self.rect.y-=self.speed    

            
    def update_status(self):
        if self.stamina<1700:
            self.stamina+=2
       
        pygame.draw.line(screen,WHITE,(60,60),(self.stamina *0.5,60),3)
       
    def getlocation(self) :
        return Point(self.rect.x,self.rect.y)
        
    def gravity(self):
        if(self.rect.y<(SCREEN_HIGHT -125)):
            self.y+=10
            self.rect.y+=10

    
    def jump(self):
       if self.isJump==False:
            self.isJump=True
            while self.jumpCount<=0:
                self.rect.y+=-self.jumpCount
                self.jumpCount+=1
                if self.jumpCount==0:
                    self.jumpCount=-10
                    self.isJump=False


    def display(self):
      #  self.update_status()
        self.move()
        
     #   self.gravity()
        self.draw()
        self.gun.shoot_system()

    def heart(self,damage):
        self.health-=damage
        # print("damage"+ str(self.health))

    def shoot (self):
        self.is_attacking=True
        self.iswalking=False
        [mouse_x,mouse_y]=pygame.mouse.get_pos()
        shooting_sound.play()
        self.gun.add_bullet(self.rect.x,self.rect.y,mouse_x,mouse_y)
        # print("clicked")


    def draw(self):
        
        if self.iswalking:
            self.image=hero_run
        elif self.health<=0:
            self.image=hero_death

        elif self.is_attacking:
            self.image=hero_fireball
            
        else :
            self.image=hero_idle    



        if self.frame>len(self.image)-1:
            self.frame=0
            self.is_attacking=False
            self.iswalking=False
        if getdir(self.rect.x):
            screen.blit(pygame.transform.flip( self.image[self.frame],True,False),(self.rect.x-70 ,self.rect.y-70))
        else:   
            screen.blit(self.image[self.frame],(self.rect.x -40,self.rect.y-70))

        if self.frmlimt>3:
            self.frame+=1
            self.frmlimt=0
            self.iswalking=False
            
        self.frmlimt+=1       
        #pygame.draw.rect(screen,WHITE,self.rect,2)

class Background_c:
    def __init__(self,x,y,img):
        self.img= img
        self.x=x
        self.y=y
        
    def setbg(self,image):
        self.img=image
    
    def display(self):
        screen.blit(self.img,(self.x,self.y))
        


class enemy():
    def __init__(self,x,y,speed,damege,health,run_animation,attack_animation,dead_animation):
        self.run_animation=run_animation
        self.dead_animation=dead_animation
        self.attack_animation=attack_animation
        self.health=health
        self.speedLimt=speed
        self.speed=speed
        self.damege=damege
        self.width=24
        self.height=54
        self.rect=pygame.Rect(0 , 0 ,self.width,self.height)
        self.image=run_animation
        self.rect.center=(x,y)
        self.color=RED
        self.frame=0
        self.frmlimt=8
        self.attacking=False
        self.iswalking=True
        self.flipped=False
        self.attack_space=20
        self.iscolidedx_l=False
        self.iscolidedx_r=False


    def movement(self):
        self.speed=randint(0,self.speedLimt)
        pl_char.getlocation()

        if pl_char.getlocation().x>self.rect.x+self.attack_space:
            self.iscolidedx_r=False
       

            if self.iscolidedx_r==False:
                self.rect.x+=self.speed
                self.flipped=False
        elif pl_char.getlocation().x<self.rect.x+self.attack_space:
            self.iscolidedx_l=False

            self.rect.x-=self.speed
            self.flipped=True
        if pl_char.getlocation().y>self.rect.y:
            self.rect.y+=self.speed
        elif pl_char.getlocation().y<self.rect.y: 
            self.rect.y-=self.speed

        

    def display(self):
        self.draw()
        self.movement()
            
    def draw(self):
        pygame.draw.line(screen,RED,(self.rect.x,self.rect.y),(self.rect.x +self.health *0.5,self.rect.y),3)
        if self.iswalking:
            self.image=self.run_animation

        elif self.attacking :
            self.image=self.attack_animation
        
        elif self.health<=0:
            self.image=self.dead_animation


        if self.frame>len(self.image)-1:
            self.frame=0
            if self.rect.colliderect(pl_char.rect.x,pl_char.rect.y,pl_char.width,pl_char.height) and self.attacking==True:
                pl_char.heart(self.damege)
            self.attacking=False
            self.iswalking=True
        if self.flipped:
            screen.blit(pygame.transform.flip( self.image[self.frame],True,False),(self.rect.x -30,self.rect.y-30))
        else:    
            screen.blit(self.image[self.frame],(self.rect.x -30,self.rect.y-45))

        if self.frmlimt>3:
            self.frame+=1
            self.frmlimt=0
            self.iswalking=False
        self.frmlimt+=1        
        # pygame.draw.rect(screen,self.color,self.rect,2)




class gun():

    def __init__(self,damage,count,speed,rate,color) :
        self.damage=damage
        self.count=count
        self.speed=speed
        self.rate=rate
        self.color=color
        self.hits=0
        self.bullets=[]
        self.targate=Point(0,0)
        self.distance=0
    
    def add_bullet(self,x,y,tx,ty):
        b=Bullet(x,y+20,tx,ty)
        self.bullets.append(b)
        
        
        


    def shoot_system(self):
        img=font_small.render( "your score is:"+str(self.hits),True,WHITE)
        screen.blit(img,(60,30))
        for bullet in self.bullets:
            bullet.shoot()
          
            if bullet.rect.x>1600 or bullet.rect.x<0:
                self.bullets.remove(bullet)
            
            
            
            for enemy in enemys:
                if bullet.rect.colliderect(enemy.rect.x,enemy.rect.y,enemy.width,enemy.height):
                    enemy.health-=self.damage
                    try:
                        self.bullets.remove(bullet)
                    except:
                        pass    
                    if enemy.health <1:
                        zombie_dead_sound.play()
                        enemys.remove(enemy)

                    self.hits+=1
            #    self.target.color=(randint(0,254),randint(0,254),randint(0,254))

                


                if enemy.rect.x < 0:
                    enemys.remove(enemy)
                    

def normalize_vector(vector):
        if vector == [0, 0]:
            return [0, 0]    
        pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
        return (vector[0] / pythagoras, vector[1] / pythagoras)

class mine():
    def __init__(self,x,y,tx,ty) :
        self.width=5
        self.height=5
        radios=20
        self.speed=8
        self.rect=pygame.Rect(0 , 0 ,self.width,self.height)
        self.rect.center=(x,y)



    def draw(self):
     #   screen.blit(self.obj,(self.rect.x -40,self.rect.y-8))
        pygame.draw.circle(screen,RED,(self.rect.x,self.rect.y),3,3)
    

class Bullet():
    
    def __init__(self,x,y,tx,ty) :
        self.width=5
        self.height=10
        self.speed=10
        self.rect=pygame.Rect(0 , 0 ,self.width,self.height)
        self.rect.center=(x,y)
        direction = (tx - x, ty - y)
        self.movementVector = normalize_vector(direction)

    
    
    def draw(self):
        screen.blit(fireball_img,(self.rect.x ,self.rect.y-10))
        # pygame.draw.circle(screen,RED,(self.rect.x,self.rect.y),3,3)

    def move(self):
      #  print('angel'+str(self.angle))
        self.rect.x += self.movementVector[0] * self.speed * 1
        self.rect.y += self.movementVector[1] * self.speed * 1
        self.draw()


    def shoot(self):
        
        self.move()

def angle_of_line(x1, y1, x2, y2):
    return math.degrees(math.atan2(-(y2-y1), x2-x1))

def create_enemys(num):
    for i in range(num):
        spon=randint(0,len(spons)-1)
        type=randint(0,len(enemy_types)-1)
        temp= enemy(spons[spon][0] ,spons[spon][1],5,10,100,enemy_types[type][1],enemy_types[type][0],enemy_types[type][2])
        enemys.append(temp)

def display_enemys():
    for enemy in enemys:
        
        enemy.display()

def colidhandler():
    for enemy in enemys:
        if enemy.rect.colliderect(pl_char.rect.x,pl_char.rect.y,pl_char.width,pl_char.height):
            enemy.attacking=True

def ui():
    pygame.draw.line(screen,GREEN,(50,20),(50 +pl_char.health*4,20),5)
    img=font_small.render( "Level:"+str(level),True,WHITE)
    screen.blit(img,(60,60))
    


def dropmine():
    pass

#variables
enemys=[]
mines=[]
level=1
temp=0
max_enemys=levels[level-1]["max"]
tonum=levels[level-1]["end_points"]
timer=0
newlevel=False
transtion=False
islost_sound=False
bg_img=Background_c(0,0,levels[level-1]["image"])
pl_char=Player(SCREEN_WID*0.5,SCREEN_HIGHT*0.5)
run=True
create_enemys(5)

keys=pygame.key.get_pressed()

def level_up_screen():
    screen.blit(levelup_img,(300,250))

playmusic()

def main():
        if mixer.get_busy()==True:
            mixer.unpause()
        bg_img.display()
        pl_char.display()
        colidhandler()
        display_enemys()
        ui()

while run:
    clock.tick(fps)
    keys=pygame.key.get_pressed()

    if is_start_screen:
        screen.blit(start_img,(0,0))
    elif is_game_over:
        screen.blit(over_img,(300,150))
        if islost_sound!=True:
            lost_sound.play()
            islost_sound=True
        
    elif transtion:
         level_up_screen()
  
    elif is_playing and transtion!=True:
        main()
    #draw
#    pygame.draw.line(screen,WHITE,(60,60),(220,60),1)
#    pygame.draw.circle(screen,WHITE,(60,60),60,3)
#    pygame.draw.ellipse(screen,WHITE,(200,100,100,50),2)
#    pygame.draw.rect(screen,WHITE,(10,100,50,50))
    
    if pl_char.health<=0:
        is_game_over=True
        is_playing=False
    if keys[pygame.K_RETURN] and is_start_screen:
        is_playing=True
        is_start_screen=False
        is_game_over=False
    elif keys[pygame.K_RETURN] and is_game_over:
        is_playing=True
        is_game_over=False
        pl_char=Player(SCREEN_WID*0.5,SCREEN_HIGHT*0.5)
        enemys.clear()
        level=1
        islost_sound=False
        max_enemys=levels[level-1]["max"]
        tonum=levels[level-1]["end_points"]
        bg_img.setbg(levels[level-1]["image"])
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run =False    
        elif len(enemys)<max_enemys:
            create_enemys(1)
        if(pl_char.gun.hits>tonum):
            level+=1
            max_enemys+=levels[level-1]["max"]
            tonum=levels[level-1]["end_points"]
            enemys.clear()
            newlevel=True
        
    if newlevel:
        timer=100
        
        bg_img.setbg(levels[level-1]["image"])
        newlevel=False
        transtion=True
        pass
    
    
    if timer>=0  :
        timer-=1
    #    screen.blit(levelup_img,(300,150))
        if timer==0:
            transtion=False

    pygame.display.update()        


pygame.quit()            
