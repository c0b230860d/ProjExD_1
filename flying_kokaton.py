import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #ゲームの初期化
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    #背景
    bg_img = pg.image.load("fig/pg_bg.jpg") #loadで背景画像を読み込む
    bg_img_han = pg.transform.flip(bg_img,True,False)
    #こうかとん
    kk_img = pg.image.load("fig/3.png") #こうとん画像を読み込む
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rect = kk_img.get_rect() # こうかとんrectを取得
    kk_rect.center = 300, 200 # 座標設定

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

        #キーボード操作
        kk_move_x = 0
        kk_move_y = 0
        key_lst = pg.key.get_pressed() # キーが押されているか？
        if key_lst[pg.K_UP]:
            kk_move_y -= 1
            # kk_rect.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kk_move_y += 1
            # kk_rect.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            kk_move_x -= 1
            # kk_rect.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_move_x += 2
            # kk_rect.move_ip((+2,0))
        
        kk_move_x -= 1 #何も押されていない場合の処理
        print(kk_move_x, kk_move_y)
        kk_rect.move_ip((kk_move_x, kk_move_y))

        screen.blit(kk_img, kk_rect) # こうかとんの描画

        pg.display.update()
        
        tmr += 1 
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()