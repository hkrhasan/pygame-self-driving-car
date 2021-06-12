import pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('images/track6.png')
car = pygame.image.load('images/tesla.png')
car = pygame.transform.scale(car, (30, 60))
text = font.render('Food Station', False, (0, 0, 0))
car_X = 153
car_Y = 300
focal_dist = 25
cam_x_offset = 0
cam_y_offset = 0
clock = pygame.time.Clock()
direction = 'up'
run = True
white = (255,255,255,255)
black = (0, 0, 0, 255)
# print("Ye Event hai >> ",pygame.event.get())

while run:

    clock.tick(60)
    cam_X = car_X + cam_x_offset + 15
    cam_Y = car_Y + cam_y_offset + 15
    up_px = window.get_at((cam_X, cam_Y - focal_dist))
    right_px = window.get_at((cam_X + focal_dist, cam_Y))
    down_px = window.get_at((cam_X, cam_Y + focal_dist))
    left_px = window.get_at((cam_X + focal_dist, cam_Y))

    check_food = up_px  if up_px == black else right_px if right_px == black else left_px if left_px == black else down_px if down_px == black else None
    # print(up_px) #, right_px, down_px, left_px
    # print("Camera offset ", cam_x_offset)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction == 'up' and up_px == black:
                    car_Y = car_Y - 20
                elif direction == 'right' and right_px == black:
                    car_X = car_X + 20
                if direction == 'down' and down_px == black:
                    car_Y = car_Y + 20
                if direction == 'left' and left_px == black:
                    car_X = car_X + 20



    # turn car
    if direction == 'up' and up_px[0] != 255 and right_px[0] == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px[0] != 255 and down_px[0] == 255:
        direction = 'down'
        car_X = car_X + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px[0] != 255 and left_px[0] == 255:
        direction = 'left'
        car_Y = car_Y + 30
        cam_y_offset = 0
        cam_x_offset = 30
        car = pygame.transform.rotate(car, 90)
    elif direction == 'left' and left_px[0] != 255 and up_px[0] == 255:
        direction = 'up'
        car_X = car_X + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)


    # car movement
    if direction == 'up' and up_px[0] == 255:
        car_Y = car_Y - 2
    elif direction == 'right' and right_px[0] == 255:
        car_X = car_X + 2
    elif direction == 'down' and down_px[0] == 255:
        car_Y = car_Y + 2
    elif direction == 'left' and left_px[0] == 255:
        car_X = car_X + 2

    window.blit(track, (0, 0))
    window.blit(car, (car_X, car_Y))
    pygame.draw.circle(window, (0, 255, 0), (cam_X, cam_Y), 5, 5)
    if check_food:
        window.blit(text, (0, 0))
    pygame.display.update()