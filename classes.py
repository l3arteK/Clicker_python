import pygame
WIDTH = 1200
HEIGHT = 720
pygame.init()
score = 0
seconds = 10
button1_font = pygame.font.Font(None, 96)
button2_font = pygame.font.Font(None, 48)
text_time_font = pygame.font.SysFont("consolas", 64)
txt_time_font = pygame.font.SysFont("consolas", 48)
text_score_font = pygame.font.SysFont("consolas", 92)
arrows_font = pygame.font.SysFont('consolas', 36)
check = False



class Button:
    def __init__(self, text, width, height, pos, elevation, radius):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.text = text
        self.radius = radius
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'
        if text == "Click me":
            self.text_surf = button1_font.render(text, True, (255, 255, 255))
        elif text == "Save" or "Reset":
            self.text_surf = button2_font.render(text, True, (255, 255, 255))
        elif text == ">":
            self.text_surf = arrows_font.render(text, True, (255, 255, 255))
        elif text == "<":
            self.text_surf = arrows_font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        self.score = 0

    def draw(self, screen,sec, restart):
        self.sec = sec

        self.restart = restart
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center


        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=self.radius)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=self.radius)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        global score
        global seconds
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if (self.text == "Click me" and self.sec <= 0) or (
                    (self.text == "Save" or self.text == "Reset") and self.sec > 0):
                pass
            else:
                self.top_color = "#D74B4B"
                if pygame.mouse.get_pressed()[0]:
                    self.dynamic_elevation = 0
                    self.pressed = True
                else:
                    if self.pressed == True:
                        if self.text == "Click me":
                            score += 1
                            self.pressed = False
                            self.dynamic_elevation = self.elevation
                        elif self.text == ">":
                            self.pressed = False
                            self.dynamic_elevation = self.elevation
                            seconds += 1
                        elif self.text == "<":
                            self.pressed = False
                            self.dynamic_elevation = self.elevation
                            seconds -= 1
                        elif self.text == "Save":
                            self.pressed = False
                            self.dynamic_elevation = self.elevation
                            plik = open('wyniki.txt', 'a')
                            plik.write("Time: "+str(seconds)+"  Score: "+str(score) + "\n")
                        elif self.text == "Reset":
                            restart()
                            self.pressed = False
                            self.dynamic_elevation = self.elevation

        else:
            self.top_color = '#475F77'
            self.dynamic_elevation = self.elevation


button1 = Button('Click me', 450, 200, (WIDTH // 2 - 225, HEIGHT // 2 - 50), 12, 60)

button_save = Button('Save', 225, 100, (WIDTH // 2 - 300, HEIGHT // 2 + 200), 6, 30)
button_reset = Button('Reset', 225, 100, (WIDTH // 2 + 80, HEIGHT // 2 + 200), 6, 30)

button_down = Button('<', 50, 50, (990, 215), 5, 10)
button_up = Button('>', 50, 50, (1095, 215), 5, 10)


def restart():

    global score
    global seconds
    global check
    score = 0
    seconds = 10
    check = False
