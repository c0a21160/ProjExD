import pygame as pg
import random
import sys


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def check_bound2(obj_rct2, scr_rct2):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko2, tate2 = +1, +1
    if obj_rct2.left < scr_rct2.left or scr_rct2.right < obj_rct2.right:
        yoko2 = -1
    if obj_rct2.top < scr_rct2.top or scr_rct2.bottom < obj_rct2.bottom:
        tate2 = -1
    return yoko2, tate2


def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    # 練習５
    bomb_sfc = pg.image.load("fig/5.png") # 正方形の空のSurface
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +7, +7

    bomb_sfc2 = pg.image.load("fig/5.png") # 正方形の空のSurface
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = random.randint(0, scrn_rct.width)
    bomb_rct2.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc2, bomb_rct2) 
    vx2, vy2 = +7, +7






    gg = 0
    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 5
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 5
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 5
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 5
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 5
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 5
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 5
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 5            
        scrn_sfc.blit(tori_sfc, tori_rct) 

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc2, bomb_rct2) 
        yoko2, tate2 = check_bound2(bomb_rct2, scrn_rct)
        vx2 *= yoko2
        vy2 *= tate2



        # 練習８
        if tori_rct.colliderect(bomb_rct):
            tori_sfc = pg.image.load("fig/7.png")
            tori_sfc = pg.transform.scale(tori_sfc, (100, 100))

            gg +=50

            if gg >=900:
                tori_sfc = pg.image.load("fig/8.png")
                if gg >=1810:
                    tori_sfc = pg.transform.scale(tori_sfc, (400, 400))
                    if gg >=1880:
                        tori_sfc = pg.transform.scale(tori_sfc, (600, 600))
                        if gg >=1070:
                            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()