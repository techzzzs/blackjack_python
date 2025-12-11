import pygame

textures = {}
texts = {}
default_img_path = "BlackJack_v2/"

def load_texture(path, scale):
    key = (path, scale)
    if key in textures:
        return textures[key]

    image = pygame.image.load(default_img_path+path).convert_alpha()
    w, h = image.get_size()
    image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    textures[key] = image
    return image


def draw_text(surface, text, x, y, w, h, r, g, b, size):
    key = (text, r, g, b, size)
    if key in texts:
        surf = texts[key]
    else:
        font = pygame.font.Font("Images/JMH Typewriter-Black.otf", size)
        surf = font.render(str(text), True, (r, g, b))
        texts[key] = surf

    rect = pygame.Rect(x, y, w, h)
    text_rect = surf.get_rect(center=rect.center)
    surface.blit(surf, text_rect)


def draw_img(surface, file, x, y, scale,only_rect=False):
    img = load_texture(file, scale)
    rect = img.get_rect(topleft=(x, y))
    if not only_rect:
        surface.blit(img, rect)
    rect2=pygame.Rect(x,y,img.get_width(),img.get_width())
    return rect2


def draw_img_c(surface, file, screen_w, screen_h, scale):
    img = load_texture(file, scale)
    rect = img.get_rect(center=(screen_w // 2, screen_h // 2))
    surface.blit(img, rect)