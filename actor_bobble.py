from actor import Actor

MSG_COLOR = (255,80,80)

# メッセージ用吹き出し
class Bobble(Actor):
    def __init__(self, app, stage) :
        super().__init__(app, stage)


        self.sprite_name = "bobble"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_name, "Asset/speech_bubble.png")
        self.font_name = "score_message"
        self.font_size = 20
        self.owner_app.GetRenderer().CreateFont("score_message", "Asset/rounded-mplus-1c-bold.ttf", self.font_size)

    def __del__(self):
        pass

    def Init(self):
        return super().Init()

    
    def Update(self):
        if self.disp == False:
            return

        self.cnt += 1
        self.y -= self.spped
        if(self.cnt > 30):
            self.disp = False
                
    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSpriteAdjustCenter(self.sprite_name, self.x, self.y )
            self.owner_app.GetRenderer().DrawTextAdjustCenter(self.font_name, self.msg, self.x, self.y, MSG_COLOR)

    def Append(self, x, y):
        self.disp = True
        self.x = x
        self.y = y
        self.cnt = 0
        self.spped = 5

    def SetMessage(self, msg):
        self.msg = msg
