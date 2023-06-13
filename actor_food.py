from actor import Actor
import math

class Food(Actor):
    def __init__(self, app, stage):
        super().__init__(app, stage)
        self.Init()

        self.cnt = 0
        self.move_cnt = 0
        self.move_val = 0

        self.blink = False

        self.spritename = "item"
        self.owner_app.GetRenderer().CreateSprite(self.spritename, "Asset/food_locomoco_don.png")
        # スプライトから当たり判定用のサイズ取得
        self.w, self.h = self.owner_app.GetRenderer().GetSpriteSize(self.spritename)
        self.w = self.w / 2
        self.h = self.h / 2
        self.radius = self.w

        self.ang = 0


        # 行動パターンをリスト化
        self.Behavior = [
            self.Behavior_0, 
            self.Behavior_1, 
            self.Behavior_2, 
            self.Behavior_3, 
            self.Behavior_4]

        self.behave_cnt = 0
        self.behave_id = 0


    def __del__(self):
        pass

    def Init(self):
        super().Init()

        self.disp = False


    def Update(self):
        
        self.cnt += 1
        self.Behavior[self.behave_id]()
            

    def Behavior_0(self):
        self.behave_cnt += 1
        if self.behave_cnt == 200:
            self.blink = True
        if self.behave_cnt == 300:
            self.disp = False

        self.x -= 5
        pass

    def Behavior_1(self):    
        pass

    def Behavior_2(self):
        pass

    def Behavior_3(self):
        pass

    def Behavior_4(self):
        pass


    def Draw(self):
        if(self.disp == True):
            if self.blink == True:
                if self.cnt % 2 == 0:
                    return
            self.owner_app.GetRenderer().DrawSpriteAdjustCenter(self.spritename, self.x, self.y)


  
    # 出現
    def Append(self, x, y):
        self.disp = True
        self.x = x
        self.y = y
        self.behave_id = 0
        self.blink = False
        self.behave_cnt = 0


    # 振る舞いIDを変更（同時にカウンタもリセット）
    def SetBehaveID(self, behave_id):
        self.behave_id = behave_id
        self.behave_cnt = 0
    


