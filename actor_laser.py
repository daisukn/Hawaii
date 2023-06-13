from actor import Actor


class Laser(Actor):
    def __init__(self, app, stage):
        super().__init__(app, stage)
        self.Init()

        self.spritename = "laser"
        self.owner_app.GetRenderer().CreateSprite(self.spritename, "Asset/laser.png")

        # スプライトから当たり判定用のサイズ取得
        self.w, self.h = self.owner_app.GetRenderer().GetSpriteSize(self.spritename)
        self.w = self.w / 2
        self.h = self.h / 2
        self.radius = self.w / 2 # このアクターでは使わない


    def __del__(self):
        pass

    def Init(self):
        super().Init()

    def Update(self):
        self.x += 15
        if self.x > self.owner_app.GetRenderer().GetScreenW():
            self.disp = False
            
    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSpriteAdjustCenter(self.spritename, self.x, self.y)

  
    # レーザー出現
    def Append(self, x, y):
        self.disp = True
        self.x = x
        self.y = y
        self.combcnt = 0


