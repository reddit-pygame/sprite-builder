import os
import pygame as pg
from tools import strip_from_sheet, load_all_gfx


def load_images(sheet, strip_size, num_columns, num_rows,
                                                 sprite_size, sprites_per_row):
    """Load sprite component images into a dict of dicts."""
    d = {}
    strips = strip_from_sheet(sheet, (0, 0), strip_size, num_columns,
                                                    num_rows)
    for i, strip in enumerate(strips):
        d[i] = {}
        imgs = strip_from_sheet(strip, (0, 0), sprite_size, sprites_per_row)
        for j, img in enumerate(imgs):        
            d[i][j] = img
    return d


SCREEN_SIZE = (1280, 720)
ORIGINAL_CAPTION = "Sprite Builder"

pg.mixer.pre_init(44100, -16, 1, 512)

pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


GFX   = load_all_gfx(os.path.join("resources", "graphics"))

#Sprite component image loading
HATS = load_images(GFX["hats"], (816, 116), 1, 34, (68, 116), 12)
SPECIAL_HATS = strip_from_sheet(GFX["special-hats"], (0, 0), (68, 116), 5)
HAIR = load_images(GFX["hair"], (1020, 116), 1, 5, (68, 116), 15)                                          
SKIN = strip_from_sheet(GFX["skin"], (0, 0), (68, 112), 12)
EYES = strip_from_sheet(GFX["eyes"], (0, 0), (68, 112), 17)
FACIAL_HAIR = load_images(GFX["facial-hair"], (1088, 116), 1, 5, (68, 116), 16)
TOPS = load_images(GFX["tops"], (1496, 116), 1, 34, (68, 116), 22)
BOTTOMS = load_images(GFX["bottoms"], (544, 116), 1, 34, (68, 116), 8)
SHOES = strip_from_sheet(GFX["shoes"], (0, 0), (68, 114), 17, 2)
MASKS = load_images(GFX["masks"], (408, 116), 1, 34, (68, 116), 6)
SPECIAL_MASKS = strip_from_sheet(GFX["special-masks"], (0, 0), (68, 116), 12, 2)




    