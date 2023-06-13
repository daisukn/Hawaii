from actor import Actor

class Fire(Actor):
    def __init__(self, app, stage):
        super().__init__(app, stage)
        self.Init()

        self.spritename = "fire"
        self.owner_app.GetRenderer().CreateSprite(self.spritename, "Asset/bomb.png")
        self.w, self.h = self.owner_app.GetRenderer().GetSpriteSize(self.spritename)


    def __del__(self):
        pass

    def Init(self):
        super().Init()
        self.anim = 0

    def Update(self):
        if self.disp == False:
            return

        self.cnt += 1
        if(self.cnt % 3 == 0):
            self.anim += 1
            if self.anim == 15:
                self.anim = 0
                self.disp = False
                
    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSpriteRectAdjustCenter(self.spritename, self.anim*80, 0, 80, 80, self.x, self.y )

    def Append(self, x, y):
        self.disp = True
        self.x = x
        self.y = y
