from stage_base import BaseStage

import pygame


WHITE = (255,255,255)
GRAY = (128, 128, 128)

class TitleStage(BaseStage):
    def __init__(self, app, game_state):
        super().__init__(app, game_state)

    def __del__(self):
        self.Release()
        pass

    def StageMain(self):

        self.owner_app.GetRenderer().DrawSprite("title_hawaii", 0, 0)
        self.owner_app.GetRenderer().DrawText("title", "憧れのハワイ航路", 100, 300, GRAY)
        self.owner_app.GetRenderer().DrawText("title", "憧れのハワイ航路", 95, 295, WHITE)
        self.owner_app.GetRenderer().DrawText("score", "ハワイを目指して press enter", 200, 500, GRAY)
        self.owner_app.GetRenderer().DrawText("score", "ハワイを目指して press enter", 197, 497, WHITE)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN] == True:
            self.owner_app.TransitionStage()


    def InitStage(self):
        pass

    def LoadStageDate(self):

        # タイトル画面の背景
        self.sprite_bg = "title_hawaii"
        self.owner_app.GetRenderer().CreateSprite(self.sprite_bg , "Asset/title_hawaii.jpg")

        self.owner_app.GetRenderer().CreateFont("score", "Asset/rounded-mplus-1c-bold.ttf", 30)
        self.owner_app.GetRenderer().CreateFont("title", "Asset/rounded-mplus-1c-bold.ttf", 100)

        pass


    def Update(self):
        pass

    def Release(self):
        return super().Release()
    