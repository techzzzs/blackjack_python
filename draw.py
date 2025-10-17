def draw_text(text, x, y, width, hight, red, green, blue):
    text = font.render(text, True, (red, green, blue))
    text_box = pygame.Rect(x, y, width, hight)
    text_box_center = text.get_rect(center=text_box.center)
    screen.blit(text, text_box_center)

def draw_image(file, x, y, scale):
    image = pygame.image.load(file)
    image = pygame.Surface.convert_alpha(image)
    old_x, old_y = image.get_size()
    image = pygame.transform.scale(image, (old_x * scale, old_y * scale))
    screen.blit(image, (x, y))