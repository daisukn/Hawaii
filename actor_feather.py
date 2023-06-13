from actor import Actor
import math

class Feather(Actor):
    def __init__(self, app, stage, parent):
        super().__init__(app, stage)
        self.Init()

        self.cnt = 0
        self.move_cnt = 0
        self.move_val = 0

        self.spritename = "feather"
        self.owner_app.GetRenderer().CreateSprite(self.spritename, "Asset/feather_yellow.png")
        # スプライトから当たり判定用のサイズ取得
        self.w, self.h = self.owner_app.GetRenderer().GetSpriteSize(self.spritename)
        self.w = self.w / 2 / 2
        self.h = self.h / 2
        self.radius = self.w / 2 # （このアクターでは使わない）


        # 親となるActor
        self.parent_actor = parent

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
        self.offset_distance = 0
        self.offiset_angle = 0

        self.target_x = 0
        self.target_y = 0
        self.angle = 0
        self.speed = 0


    def Update(self):
        if self.disp == False:
            return

        
        self.cnt += 1
        self.Behavior[self.behave_id]()
            


    def Behavior_0(self):
        #if self.cnt < 100:        
        self.MoveToTarget()

        if self.x < -50:
            self.disp = False
            self.cnt = 0

        pass

    def Behavior_1(self):
        self.behave_cnt += 1

#        ang = self.behave_cnt * 10
        self.offiset_angle += 1
        self.x = self.parent_actor.GetX() + math.cos(math.radians(self.offiset_angle)) * self.offset_distance
        self.y = self.parent_actor.GetY() + math.sin(math.radians(self.offiset_angle)) * self.offset_distance

        pass

    def Behavior_2(self):
        pass

    def Behavior_3(self):
        pass

    def Behavior_4(self):
        pass


    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSpriteAdjustCenter(self.spritename, self.x, self.y)


  
    # レーザー出現
    def Append(self, x, y):
        self.disp = True
        self.x = x
        self.y = y

    def SetAngle(self, angle):
        self.angle = angle
    def SetSpeed(self, speed):
        self.speed = speed

    def SetOffset(self, distance, angle):
        self.offset_distance = distance
        self.offiset_angle = angle

    # 振る舞いIDを変更（同時にカウンタもリセット）
    def SetBehaveID(self, behave_id):
        self.behave_id = behave_id
        self.behave_cnt = 0
