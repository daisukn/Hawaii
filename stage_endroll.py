from stage_base import BaseStage

import pygame


WHITE = (255,255,255)
GRAY = (128, 128, 128)

class EndrollStage(BaseStage):
    def __init__(self, app, game_state):
        super().__init__(app, game_state)

    def __del__(self):
        self.Release()
        pass

    def LoadStageDate(self):

        # タイトル画面の背景
        self.image_party = "party"
        self.owner_app.GetRenderer().CreateSprite("party", "Asset/party.png")
        self.font_msg1 = "msg1"
        self.owner_app.GetRenderer().CreateFont(self.font_msg1, "Asset/rounded-mplus-1c-bold.ttf", 30)
        self.font_msg2 = "msg2"
        self.owner_app.GetRenderer().CreateFont(self.font_msg2, "Asset/rounded-mplus-1c-bold.ttf", 100)
        pass


    def StageMain(self):

        self.owner_app.GetRenderer().DrawSprite(self.image_party, 0, 0)
        txt = "おめでとうございます！"
        self.owner_app.GetRenderer().DrawText(self.font_msg2, txt, 108, 208, WHITE)
        self.owner_app.GetRenderer().DrawText(self.font_msg2, txt, 100, 200, (128, 64, 64))
        txt = "ハワイに着きました！"
        self.owner_app.GetRenderer().DrawText(self.font_msg2, txt, 108, 318, WHITE)
        self.owner_app.GetRenderer().DrawText(self.font_msg2, txt, 100, 310, (128, 64, 64))

        txt = "幾多の困難を乗り越えて手に入れた休暇を満喫してください"
        self.owner_app.GetRenderer().DrawText(self.font_msg1, txt, 204, 504, WHITE)
        self.owner_app.GetRenderer().DrawText(self.font_msg1, txt, 200, 500, (64, 64, 64))

        txt = "ちなみにあなたのスコアは、" + str(self.score) + "点でした。"
        self.owner_app.GetRenderer().DrawText(self.font_msg1, txt, 204, 584, WHITE)
        self.owner_app.GetRenderer().DrawText(self.font_msg1, txt, 200, 580, (64, 64, 64))

        txt = "最大コンボ数は、" + str(self.max_combo) + "でした。"
        self.owner_app.GetRenderer().DrawText(self.font_msg1, txt, 204, 624, WHITE)
        self.owner_app.GetRenderer().DrawText(self.font_msg1, txt, 200, 620, (64, 64, 64))


        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] == True:
            self.owner_app.TransitionStage()
            self.owner_app.GetMixer().StopBGM()

    def InitStage(self):
        pass



    def Update(self):
        pass

    def Release(self):
        return super().Release()
    