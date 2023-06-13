from actor import Actor

WHITE = (255,255,255)

class UIElement(Actor):
    def __init__(self, app, stage):
        super().__init__(app, stage)
        self.Init()

        self.sprite_rainbow = "rainbow"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_rainbow, "Asset/rainbow.png")
        self.sprite_japan = "japan"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_japan, "Asset/syachiku.png")
        self.sprite_hawaii = "hawaii"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_hawaii, "Asset/hawaii.png")
        self.sprite_traveler = "traveler"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_traveler, "Asset/traveler.png")


        self.sprite_guage = "life_gauge"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_guage, "Asset/life_1.png")
        self.sprite_meter = "life_meter"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_meter, "Asset/life_2.png")
        
        self.font_UI = "font_ui"
        self.owner_app.GetRenderer().CreateFont(self.font_UI, "Asset/rounded-mplus-1c-bold.ttf", 30)


    def Init(self):
        super().Init()
        self.disp = True
        self.score = 0
        self.combo = 0
        self.distance = 0
        self.max_distance = self.owner_stage.GetMaxDistance()
        self.max_journey = self.owner_stage.GetMaxJourney()
        
    def __del__(self):
        pass

    def Update(self):
        self.score = self.owner_stage.GetScore()
        self.life = self.owner_stage.GetLife()
        self.max_life = self.owner_stage.GetMaxLife()
        self.combo = self.owner_stage.GetComboCount()

        self.journey = self.owner_stage.GetJourney()
        self.distance = self.max_distance * (self.max_journey - self.journey) / self.max_journey
        if(self.distance < 0):
            self.distance = 0

        if self.disp == True:
            pass
                
    def Draw(self):
        if(self.disp == True):
            self.owner_app.GetRenderer().DrawSprite(self.sprite_rainbow, 0, 640)
            self.owner_app.GetRenderer().DrawSprite(self.sprite_japan, 50, 640)
            self.owner_app.GetRenderer().DrawSprite(self.sprite_hawaii, 1130, 600)
            self.owner_app.GetRenderer().DrawSprite(self.sprite_traveler, (self.journey / self.max_journey)*1000 + 100, 640)
        
            txt = "スコア:  " + str(self.score)
            self.owner_app.GetRenderer().DrawText(self.font_UI, txt, 10, 10, WHITE)

            txt = "コンボ:  " + str(self.combo)
            self.owner_app.GetRenderer().DrawText(self.font_UI, txt, 300, 10, WHITE)


            txt = "ハワイまであと" + str(int(self.distance)) + "キロ"
            self.owner_app.GetRenderer().DrawText(self.font_UI, txt, 900, 10, WHITE)

            # ライフゲージ表示
            guage_size = 130
            size = int(guage_size * self.life / self.max_life)
            if size < 0 :
                size = 0
            self.owner_app.GetRenderer().DrawSpriteRect(self.sprite_meter, 0, 0, size, 15, 15, 65)
            self.owner_app.GetRenderer().DrawSprite(self.sprite_guage, 10, 60)

            if self.owner_stage.GetBossFlag() == True:
                guage_size = 130
                size = int(guage_size *  self.owner_stage.GetBossLife() / self.max_life)
                if size < 0 :
                    size = 0
                self.owner_app.GetRenderer().DrawSpriteRect(self.sprite_meter, 0, 0, size, 15, 1105+(130-size), 65)
                self.owner_app.GetRenderer().DrawSprite(self.sprite_guage, 1100, 60)

