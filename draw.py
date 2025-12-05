import pygame

textures = {}
texts = {}

def load_texture(path, scale):
    key = (path, scale)
    if key in textures:
        return textures[key]

    image = pygame.image.load(path).convert_alpha()
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


def draw_image(surface, file, x, y, scale):
    img = load_texture(file, scale)
    surface.blit(img, (x, y))


def draw_image_c(surface, file, screen_w, screen_h, scale):
    img = load_texture(file, scale)
    rect = img.get_rect(center=(screen_w // 2, screen_h // 2))
    surface.blit(img, rect)
