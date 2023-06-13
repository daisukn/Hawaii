# 衝突判定用の関数

import math
from actor import Actor


# Actor同士で判定
def CollisionSqure(a, b):
    ## 中心点を調整
    x_a = a.GetX() - a.GetW()/2
    y_a = a.GetY() - a.GetH()/2
    w_a = a.GetW()
    h_a = a.GetH()
    
    x_b = b.GetX() - b.GetW()/2
    y_b = b.GetY() - b.GetH()/2
    w_b = b.GetW()
    h_b = b.GetH()

    return CollisionDetectionSquare(x_a, y_a, w_a, h_a, x_b, y_b, w_b, h_b)


# Actor同士で判定    
def CollisionCircle(a, b):
    x_a = a.GetX()
    y_a = a.GetY()
    r_a = a.GetRadius()
    
    x_b = b.GetX()
    y_b = b.GetY()
    r_b = b.GetRadius()
    
    return CollisionDetectionCircle(x_a, y_a, r_a, x_b, y_b, r_b)


def Distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 距離による判定
def CollisionDetectionCircle(x1, y1, radius_a, x2, y2, radius_b):
    if Distance(x1, y1, x2, y2) <= (radius_a + radius_b):
        return True
    else:
        return False
    
# 矩形による判定
def CollisionDetectionSquare(x_a, y_a, w_a, h_a, x_b, y_b, w_b, h_b):
    if x_a < x_b + w_b and x_a + w_a > x_b and y_a < y_b + h_b and y_a + h_a > y_b:
        return True
    else:
        return False
