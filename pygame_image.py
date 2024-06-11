import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #ゲームの初期化
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #loadで背景画像を読み込む
    bg_img_han = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png") #こうとん画像を読み込む
    kk_img = pg.transform.flip(kk_img, True, False)

    tmr = 0

    #ゲームのループ
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % (3200)
        screen.blit(bg_img, [-x, 0]) #(0,0)左上に背景を張り付け
        screen.blit(bg_img_han, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(bg_img_han, [-x+(1600*3), 0])
        # screen.blit(kk_img,[300, 200])これだと固定されてしまうので・・・
        kk_rect = kk_img.get_rect() # こうかとんrectを取得
        kk_rect.center = 300, 200 # 座標設定
        screen.blit(kk_img, kk_rect) # こうかとんの描画

        pg.display.update()
        tmr += 1 
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()