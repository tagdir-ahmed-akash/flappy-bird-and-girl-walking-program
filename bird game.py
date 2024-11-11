import pgzrun
import random

WIDTH = 350
HEIGHT = 600
GAP_SIZE = 200  # Define the gap size for the bird to pass through

background = Actor('background')
bird = Actor('bird')
bird.x = 50
bird.y = HEIGHT / 2

bar_up = Actor('bar_up')
bar_down = Actor('bar_down')

# Initialize variables
bar_speed = 2
target_speed = random.uniform(2, 4)
acceleration = 0.02
game_active = True
score = 0  # Track the player's score

# Function to reset game state
def reset_game():
    global bar_speed, target_speed, game_active, score
    bird.y = HEIGHT / 2
    bar_speed = 2
    target_speed = random.uniform(2, 4)
    reset_bars()
    score = 0
    game_active = True

# Function to reset bar positions and speeds
def reset_bars():
    bar_up.y = random.randint(-100, 100)
    bar_down.y = bar_up.y + GAP_SIZE + bar_up.height
    bar_up.x = WIDTH
    bar_down.x = WIDTH

reset_bars()

def draw():
    background.draw()
    bar_up.draw()
    bar_down.draw()
    bird.draw()

    # Display the score in the upper left corner
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")

    # Display the "Nice Try" message if the game is over
    if not game_active:
        screen.draw.text(
            "Nice Try,If you want to reset Press R",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=30,
            color="white"
        )

def update():
    global bar_speed, target_speed, game_active, score

    if game_active:
        # Gradually adjust the speed towards the target speed
        if bar_speed < target_speed:
            bar_speed += acceleration
        elif bar_speed > target_speed:
            bar_speed -= acceleration

        # Move the bars to the left
        bar_up.x -= bar_speed
        bar_down.x -= bar_speed

        # Reset bars and update score when they go off-screen
        if bar_up.x < 0:
            reset_bars()
            target_speed = random.uniform(2, 4)  # Set a new target speed
            score += 1  # Increment score each time the bird crosses the gap

            # Increase bar speed slightly every 10 points
            if score % 10 == 0:
                bar_speed += 0.5  # Increment speed to make the game harder

        # Apply gravity to the bird
        bird.y += 2

        # Check for collision with bars
        if bird.colliderect(bar_up) or bird.colliderect(bar_down):
            game_active = False  # Stop the game if collision occurs

    # Check if the bird hits the screen edges
    if bird.y > HEIGHT or bird.y < 0:
        bird.y = HEIGHT / 2  # Reset bird position if it goes out of bounds

def on_mouse_down():
    if game_active:
        bird.y -= 100  # Move the bird up only if the game is active

def on_key_down(key):
    if key == keys.R and not game_active:
        reset_game()  # Reset the game if "R" is pressed and game is over

pgzrun.go()
