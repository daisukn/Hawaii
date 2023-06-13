import pygame

SCREEN_W = 1280
SCREEN_H = 720
WINDOW_TITLE = "ハワイ航路"


BLANK_COLOR = (255,255,255)

# アセット管理とレンダリング処理をするクラス
class Renderer:
    def __init__(self):

        self.screen_h = SCREEN_H
        self.screen_w = SCREEN_W
        self.WindowTitle = WINDOW_TITLE
        pygame.display.set_caption(self.WindowTitle)

        self.screen = pygame.display.set_mode(( self.screen_w, self.screen_h)) 
        self.clock = pygame.time.Clock()

        self.images = {}
        self.fonts = {}

    def __del__(self):
        pass

    # Getter/Stter
    def GetScreen(self):
        return self.screen    
    def GetScreenH(self):
        return self.screen_h
    def GetScreenW(self):
        return self.screen_w


    def FillBlankColor(self):
        self.screen.fill(BLANK_COLOR)
        pass

    # スプライトをロード
    def CreateSprite(self, name, file_name):
        if name in self.images:
            pass
        else:
            image = pygame.image.load(file_name)
            self.images[name] = image
    
    # スプライトの大きさを取得する
    def GetSpriteSize(self, name):
        if(name in self.images):
            w = self.images[name].get_width()
            h = self.images[name].get_height()
            return w,h

    # 描画
    def DrawSprite(self, name, x, y):
        if(name in self.images):
            self.screen.blit(self.images[name], [x, y])
        else:
            pass

    # 描画（センター補正）
    def DrawSpriteAdjustCenter(self, name, x, y):
        if(name in self.images):
            x -= self.images[name].get_width() / 2
            y -= self.images[name].get_height() / 2

            self.screen.blit(self.images[name], [x, y])
        else:
            pass

    # 切り抜いて描画
    def DrawSpriteRect(self, name, src_x, src_y, src_w, src_h, dist_x, dist_y):
        if(name in self.images):
            rect = pygame.Rect(src_x, src_y, src_w, src_h)
            partial_image = self.images[name].subsurface(rect)
            self.screen.blit(partial_image, [dist_x, dist_y])
    
    # 切り抜いて描画（センター補正）
    def DrawSpriteRectAdjustCenter(self, name, src_x, src_y, src_w, src_h, dist_x, dist_y):
        if(name in self.images):
            rect = pygame.Rect(src_x, src_y, src_w, src_h)
            partial_image = self.images[name].subsurface(rect)
            dist_x -= partial_image.get_width() / 2
            dist_y -= partial_image.get_height() / 2
            self.screen.blit(partial_image, [dist_x, dist_y])

    # フリップ
    def UpdateDisplay(self):
        pygame.display.update()
         # FPS60に固定
        self.clock.tick(60)
    
    # フォント生成
    def CreateFont(self, name, font_filename, size):
        if name in self.fonts:
            pass
        else:
            font = pygame.font.Font (font_filename, size)
            self.fonts[name] = font

    # フォント描画
    def DrawText(self, name, text_string, x, y, color):
        if name in self.fonts:
            text = self.fonts[name].render(text_string, True, color) 
            self.screen.blit(text, (x,y))
    
    # フォント描画（センター補正）
    def DrawTextAdjustCenter(self, name, text_string, x, y, color):
        if name in self.fonts:
            
            w, h = self.fonts[name].size(text_string)
            x -= w/2
            y -= h/2
            text = self.fonts[name].render(text_string, True, color) 
            self.screen.blit(text, (x,y))

    # アフファ値の変更
    def SetAlpha(self, name, alpha):
        if name in self.images:     
            self.images[name].set_alpha(alpha)

    # カラーキーのセット
    def SetColorkey(self, name, key):
        if name in self.images:
            self.images[name].set_colorkey(key)
