import pygame
import random
pygame.init()

clock = pygame.time.Clock()





def gameloop():
    def draw_snake(gameWindow, color, snake_list, snake_size):
        for x, y in snake_list:
            pygame.draw.rect(gameWindow, color, [x,y,snake_size,snake_size])


    def show_score(text, color, x,y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])
    snake_length = 3
    snake_list = []
    screen_width = 1200
    screen_height = 800

    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    font = pygame.font.SysFont(None, 50)
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Snek Game")
    pygame.display.update()

    exit_game = False
    game_over = False
    snake_x = screen_width/2
    snake_y = screen_height/2
    snake_size = 10
    fps = 60
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    vel_x = 0
    vel_y = 0
    score = 0
    init_vel = 0.3
    high_score =0

    while not exit_game:
        if game_over:
            gameWindow.fill(red)
            show_score("  Game Over! Press Enter To Continue or Press esc to exit", black, 0, screen_height/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True  
                if event.type == pygame.K_RETURN:
                    break       
        else:    
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = init_vel
                        vel_y = 0

                    if event.key == pygame.K_LEFT:
                        vel_x = -init_vel
                        vel_y = 0
                    if event.key == pygame.K_UP:
                        vel_x = 0
                        vel_y = -init_vel
                    if event.key == pygame.K_DOWN:
                        vel_x = 0
                        vel_y = init_vel

            snake_x += vel_x
            snake_y += vel_y

            if event.type == pygame.QUIT:
                exit_game = True
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 1
                init_vel +=0.2 if init_vel<=1.2 else 0
                # print("Score= ", score)
                snake_length +=10 + 2*score
                food_x = random.randint(0, screen_width/2)
                food_y = random.randint(0, screen_height/2)
            gameWindow.fill(white)
            show_score("Score: " + str(score), red, 5,5)
            show_score("High Score: " + str(score if score > high_score else high_score), black, 0,50)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            # print(snake_list)
            # print(head)
            if snake_x <0 or snake_x >screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("Gaym Over Nigga")
            if len(snake_list) > snake_length:
                del snake_list[0]
   
            draw_snake(gameWindow, black, snake_list, snake_size)               
            pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
            if score > high_score:
                high_score = score
            # clock.tick(fps)
        pygame.display.update()

if __name__ == "__main__":
    gameloop()