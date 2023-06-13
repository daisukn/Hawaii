from actor import Actor

class Island(Actor):
    def __init__(self, app, stage):
        super().__init__(app, stage)
        self.Init()
        
        self.spritename = "island"
        self.owner_app.GetRenderer().CreateSprite(self.spritename, "Asset/vacation_island.png")

    def Init(self):
        super().Init()        
        self.x = 0
        self.y = 0

    def __del__(self):
        pass

    def Update(self):
        self.MoveToTarget()
                
    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSpriteAdjustCenter(self.spritename, self.x, self.y )

    def Append(self, x, y):
        self.disp = True
        self.x = 1500
        self.y = 600

        self.SetTarget(x, y, 100)
