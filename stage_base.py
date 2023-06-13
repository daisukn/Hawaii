
# ステージ間で引き継ぐデータ
class GameState:
    def __init__(self):
        self.score      = 0
        self.max_combo  = 0
        self.life       = 100

    ## Setter/Getter
    def SetState(self, life, score, max_combo):
        self.life = life
        self.score = score
        self.max_combo = max_combo

    def GetScore(self):
        return self.score
    def GetLife(self):
        return self.life
    def GetMaxCombo(self):
        return self.max_combo


# レイアウトデータ格納
class LayoutData:
    def __init__(self, frame, pos_x, pos_y, type, pattern):
        # 出現フレーム
        self.frame = int(frame)
        # 出現1
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        # 出現敵のタイプ
        self.type = int(type)
        self.pattern = int(pattern)
 

# ステージの基底クラス
class BaseStage:
    def __init__(self, app, game_state):
        self.owner_app = app
        self.game_state = game_state

        # GameStateのデータを引き継ぐ
        self.score      = self.game_state.GetScore()
        self.max_combo  = self.game_state.GetMaxCombo()
        self.life       = self.game_state.life

        # ライフの最大値
        self.max_life = 100

        self.score_table = []
        self.combo_count = 0

        # 移動距離
        self.journey = 0
        self.max_journey = 1000
        # 距離情報
        self.distance = 0
        self.max_distance = 1000

        #カウンター
        self.counter = 0
        # アクター
        self.actors = []

        # レイアウトデータ
        self.layout = []
        # 最後に出たenemy
        self.last_enemy = 0


        self.LoadStageDate()

        # ボスのライフ
        self.boss_life  = 100
        self.boss_flag  = False


        pass


    def InitStage(self):
        # 変数の初期化
        pass

    def LoadStageDate(self):
        # Actorのインスタンス作成
        # アセットのロード
        pass


    # レイアウト読み込み
    def LoadLayoutData(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if line[0] != '#':
                        values = line.split(',')
                        item = LayoutData(*values)
                        self.layout.append(item)
        self.layout.sort(key=lambda item:item.frame)
        pass

    def Update(self):
        # Actorのアップデート
        # 入力処理
        pass

    # ステージを遷移する
    def Transition(self):
        self.game_state.SetState(self.life, self.score, self.max_combo)        
        self.owner_app.TransitionStage()


    # Actorを登録
    def AddActor(self, actor):
        self.actors.append(actor)

    def Release(self):
        pass




    def GetLife(self):
        return self.life
    def SetLife(self, life):
        self.life = life
    def GetMaxLife(self):
        return self.max_life
    def GetScore(self):
        return self.score
    def GetComboCount(self):
        return self.combo_count
    def GetJourney(self):
        return self.journey
    def GetMaxJourney(self):
        return self.max_journey
    def GetDistance(self):
        return self.distance
    def GetMaxDistance(self):
        return self.max_distance
    def GetBossLife(self):
        return self.boss_life
    def GetBossFlag(self):
        return self.boss_flag