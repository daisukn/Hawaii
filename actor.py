class Actor:
    def __init__(self, app, stage):
        self.owner_app = app
        self.owner_stage = stage
        self.owner_stage.AddActor(self)
        self.Init()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.radius = 0
        self.move_x = 0
        self.move_y = 0
        self.move_val = 0
        self.speed = 0



    def __del__(self):
        pass

    # 派生先でオーバーライドする    
    def Init(self):
        self.disp = False
        self.active = False
        self.cnt = 0
        self.move_cnt = 0
        self.move_val = 0
        pass
    def Update(self):
        pass
    def Draw(self):
        pass



    def SetTarget(self, x, y, val):
        self.move_val = val
        self.move_cnt = 0
        self.target_x = x
        self.target_y = y

        self.move_x = (self.target_x - self.x) /val
        self.move_y = (self.target_y - self.y) /val

    def MoveToTarget(self):
        if self.move_cnt < self.move_val:
            self.x += self.move_x
            self.y += self.move_y
            self.move_cnt += 1



    # Getter / Setter
    def GetDisp(self):
        return self.disp
    def SetDisp(self, disp):
        self.disp = disp
    def GetX(self):
        return self.x
    def SetX(self, x):
        self.x = x
    def GetY(self):
        return self.y
    def GetW(self):
        return self.w
    def SetW(self,w):
        self.w = w
    def GetH(self):
        return self.h
    def SetH(self, h):
        self.h = h    
    def GetRadius(self):
        return self.radius
    def SetRadius(self, r):
        self.radius = r
    def SetY(self, y):
        self.y = y
    def GetCnt(self):
        return self.cnt
    def SetCnt(self, cnt):
        self.cnt = cnt
    def GetActive(self):
        return self.active
    def SetActive(self, active):
        self.active = active
