import sys
from classes import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker")
clock = pygame.time.Clock()

current_time = 0
results_check = False

time = seconds
one = True

delta_time = pygame.time.get_ticks()

sec = 60

text_time = text_time_font.render("Time:", True, (255, 255, 255))
text_score = text_score_font.render(str(score), True, (255, 255, 255))
Outcomes = []
number_of_outcomes = 0
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

    if not button_results.press:
        button_reset.draw(screen, time)
        button1.draw(screen, time)  # Click me

        button_save.draw(screen, time)  # Save

        button_up.draw(screen, time)
        button_down.draw(screen, time)
    else:
        plik = open('wyniki.txt', 'r')
        zawartosc = plik.readlines()
        plik.close()

        if number_of_outcomes < len(zawartosc):
            for linie in zawartosc:
                linie = linie.strip()
                Outcomes.append(Outcome(linie, 200 + number_of_outcomes * 100))
                number_of_outcomes += 1
        elif len(zawartosc) < number_of_outcomes:
            number_of_outcomes = 0
            Outcomes = []
            for linie in zawartosc:
                linie = linie.strip()
                Outcomes.append(Outcome(linie, 200 + number_of_outcomes * 100))
                number_of_outcomes += 1

        for outcome in Outcomes:
            outcome.draw(screen)

    button_results.draw(screen, time)

    screen.blit(text_time, (1000, 50))
    screen.blit(text_score, (100, 50))
    if not check:
        txt_time = txt_time_font.render(str(seconds), True, (255, 255, 255))
        time = seconds
        screen.blit(txt_time, (1040, 150))

    pygame.display.update()
    clock.tick(60)
