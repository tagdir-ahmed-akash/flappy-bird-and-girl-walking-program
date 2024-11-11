import pgzrun

WIDTH = 1200
HEIGHT = 600

Anims = [Actor('1'), Actor('2'), Actor('3'), Actor('4'), Actor('5')]
numAnims = len(Anims)
animIndex = 0
animSpeed = 0

player_x = WIDTH / 2
player_y = HEIGHT / 2
moving_right = True  # Track the movement direction

for i in range(numAnims):
    Anims[i].x = player_x
    Anims[i].y = player_y

def draw():
    screen.fill('gray')
    Anims[animIndex].draw()  # Draw the character normally, no flipping

def update():
    global animIndex, player_x, animSpeed, moving_right
    
    if keyboard.right:
        moving_right = True
        player_x += 5  # Move to the right
        for i in range(numAnims):
            Anims[i].x = player_x

        if player_x >= WIDTH:
            player_x = 0  # Wrap around to the left
        animSpeed += 1
        if animSpeed % 5 == 0:
            animIndex = (animIndex + 1) % numAnims  # Loop through walking animations

    elif keyboard.left:
        moving_right = False
        player_x -= 5  # Move to the left (backward like Michael Jackson's move)
        for i in range(numAnims):
            Anims[i].x = player_x

        if player_x < 0:
            player_x = WIDTH  # Wrap around to the right
        animSpeed += 1
        if animSpeed % 5 == 0:
            animIndex = (animIndex + 1) % numAnims  # Loop through walking animations

pgzrun.go()
