import pygame
textures={}


def load_texture(path, scale):
    key = (path, scale)  # unique cache key for each file + scale
    if key in textures:
        return textures[key]

    texture = pygame.image.load(path).convert_alpha()
    old_x, old_y = texture.get_size()
    texture = pygame.transform.scale(texture, (int(old_x * scale), int(old_y * scale)))

    textures[key] = texture
    return texture



pygame.init()
screen_width = 1000
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))


texts = {}
def draw_text(text, x, y, width, height, red, green, blue, size):
    text_box = pygame.Rect(x, y, width, height) # Define the text box rect
    key = (text, red, green, blue, size) # Cache key (unique per text, color, size)
    if key in texts:  # Get or render the text surface
        text_surf = texts[key]
    else:
        font = pygame.font.Font("Images/JMH Typewriter-Black.otf", size)
        text_surf = font.render(str(text), True, (red, green, blue))
        texts[key] = text_surf

    text_rect = text_surf.get_rect(center=text_box.center)# Center the text surface in the text box
    screen.blit(text_surf, text_rect)  # Draw it



def draw_image(file, x, y, scale):
    image= load_texture(file,scale)
    screen.blit(image, (x, y))

def draw_image_c(file, screen_w, screen_h, scale):
    image = load_texture(file, scale)
    image_rect = image.get_rect(center=(screen_w // 2, screen_h // 2))
    screen.blit(image, image_rect)

