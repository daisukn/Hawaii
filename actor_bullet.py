from actor import Actor

import math

class Bullet(Actor):
    def __init__(self, app, stage):
        super().__init__(app, stage)
        self.Init()

        self.spritename = "bullet"
        self.owner_app.GetRenderer().CreateSprite(self.spritename, "Asset/bullet.png")
        self.owner_app.GetRenderer().SetColorkey(self.spritename, (0,0,0))
        self.w, self.h = self.owner_app.GetRenderer().GetSpriteSize(self.spritename)
        self.radius = self.h

        self.angle = 0
        self.speed = 5

    def __del__(self):
        pass

    def Init(self):
        super().Init()
        self.anim = 0

    def SetAngle(self, angle):
        self.angle = angle
    def SetSpeed(self, speed):
        self.speed = speed

    def Update(self):
        if self.disp == False:
            return

        self.cnt += 1
        if(self.cnt % 15 == 0):
            self.anim += 1
            if self.anim == 6:
                self.anim = 0
        
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y += math.sin(math.radians(self.angle)) * self.speed

        if self. x < 0 or self.x > self.owner_app.GetRenderer().GetScreenW() or self.y < 0 or self.y > self.owner_app.GetRenderer().GetScreenH():
            self.disp = False
                
    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSpriteRectAdjustCenter(self.spritename, self.anim*14, 0, 14, 14, self.x, self.y )

    def Append(self, x, y):
        self.disp = True
        self.x = x
        self.y = y
