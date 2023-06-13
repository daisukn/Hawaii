import pygame


class SoundMixer:
    def __init__(self):

        self.bgm = None
        self.sound_effects = {}

        self.volume = 0.3

        self.bgm_enabled = True
        self.sound_enabled = True

        pygame.mixer.init()

    def SetBGMEnable(self, bgm_enable):
        self.bgm_enabled = bgm_enable

    def SetSoundEnable(self, sound_enable):
        self.sound_enabled = sound_enable

    def SetVolume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

        for sound in self.sound_effects:
            sound.set_volume(1)#self.volume)

    def CreateBGM(self, file_name):
        pygame.mixer.music.load(file_name)

    # ループ再生
    def PlayBGM(self):
        if self.bgm_enabled == True:
            pygame.mixer.music.play(-1)

    def StopBGM(self):
        pygame.mixer.music.stop()
        
    def CreateSoundEffects(self, name, file_name):
        if name in self.sound_effects:
            pass
        else:
            se = pygame.mixer.Sound(file_name)
            self.sound_effects[name] = se
    
    def PlaySound(self, name):
        if self.sound_enabled == True:
            if name in self.sound_effects:
                self.sound_effects[name].set_volume(self.volume)
                self.sound_effects[name].play()

