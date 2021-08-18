import sys
from classes import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker")
clock = pygame.time.Clock()

current_time = 0

time = seconds
one = True


delta_time = pygame.time.get_ticks()

sec = 60




text_time = text_time_font.render("Time:", True, (255, 255, 255))
text_score = text_score_font.render(str(score), True, (255, 255, 255))

while True:
    from classes import score, seconds

    text_score = text_score_font.render(str(score), True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = pygame.time.get_ticks()

    screen.fill((50, 50, 50))
    if score > 0:
        check = True
        if one:
            delta_time = pygame.time.get_ticks()
            one = False
        if check:
            if seconds - (current_time - delta_time) // 1000 >= 0:
                time = seconds - (current_time - delta_time) // 1000

            txt_time = txt_time_font.render(str(time), True, (255, 255, 255))
            screen.blit(txt_time, (1040, 150))
    else:
        check = False
        one = True

    button_reset.draw(screen,time,restart)
    button1.draw(screen, time ,button_reset.restart)  # Click me

    button_save.draw(screen,time, button_reset.restart)  # Save

    button_up.draw(screen,time, button_reset.restart)
    button_down.draw(screen,time, button_reset.restart)


    screen.blit(text_time, (1000, 50))
    screen.blit(text_score, (100, 50))
    if not check:
        txt_time = txt_time_font.render(str(seconds), True, (255, 255, 255))
        time = seconds
        screen.blit(txt_time, (1040, 150))

    pygame.display.update()
    clock.tick(60)
