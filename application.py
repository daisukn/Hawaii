from renderer import Renderer
from sound_mixer import SoundMixer
from stage_base import GameState
from stage_hawaii import HawaiiStage
from stage_title import TitleStage
from stage_endroll import EndrollStage
from enum import Enum

import pygame
import sys



# 定数
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLANK_COLOR = (0, 0, 64)


# ステージ識別
class STAGE_ID(Enum):
    TITLE   = 0
    HAWAII  = 1
    LUNA    = 2
    ENDROLL = 3
    CLEAR   = 4
    FAILE   = 5

 
class Application:
    # コンストラクタ
    def __init__(self):
        pygame.init()

        self.renderer = Renderer()
        self.Init()

        self.mixer = SoundMixer()
        self.mixer.SetBGMEnable(True)
        self.mixer.SetSoundEnable(True)
        self.mixer.SetVolume(0.1)

        self.game_state = GameState()

        self.current_stage = TitleStage(self, self.game_state)
        self.current_stage_id = STAGE_ID.TITLE

   


    # デストラクタ
    def __del__(self):
        pass


    def GetRenderer(self):
        return self.renderer
    
    def GetMixer(self):
        return self.mixer

    def Init(self):
        pass

    # 実行
    def Execute(self):
        # メインループ
        while True:
            for event in pygame.event.get():
                # 閉じるボタンで終了
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE] == True:
                pygame.quit()
                sys.exit()
            self.Update()
            self.renderer.UpdateDisplay()       

    # Stageを呼ぶ
    def Update(self):
        self.current_stage.StageMain()

        #fps = self.renderer.clock.get_fps()
        #print(f'Current FPS: {fps}')


    # ステージを遷移する
    def TransitionStage(self):
        self.current_stage.Release()

        if(self.current_stage_id == STAGE_ID.TITLE):
            self.current_stage = HawaiiStage(self, self.game_state)
            self.current_stage_id = STAGE_ID.HAWAII

        elif(self.current_stage_id == STAGE_ID.HAWAII):
            self.current_stage = EndrollStage(self, self.game_state)
            self.current_stage_id = STAGE_ID.ENDROLL
        
        elif(self.current_stage_id == STAGE_ID.ENDROLL):
            self.current_stage = TitleStage(self, self.game_state)
            self.current_stage_id = STAGE_ID.TITLE

        self.current_stage.InitStage()            


