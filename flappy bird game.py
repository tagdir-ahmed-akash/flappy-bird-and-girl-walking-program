import pgzrun
import random

WIDTH = 350
HEIGHT = 600

# Initialize the score variable
score = 0

# Load images for the game objects
background = Actor('background')
bird = Actor('bird')
bird.x = 50
bird.y = HEIGHT / 2
bird.gravity = 0.5  # Gravity for the bird


# Create obstacles with random initial positions and speeds
def create_bar():
    bar_up = Actor('bar_up')
    bar_down = Actor('bar_down')

    # Set initial positions
    bar_up.x = WIDTH
    bar_down.x = WIDTH
    gap_size = 150  # Vertical gap between bars

    # Set random y position for upper bar, and place lower bar accordingly
    bar_up.y = random.randint(-100, 100)
    bar_down.y = bar_up.y + gap_size + bar_down.height

    # Set random speed for each bar
    bar_speed = random.randint(2, 5)
    bar_up.speed = bar_speed
    bar_down.speed = bar_speed

    return bar_up, bar_down


# Initialize the first set of bars
bar_up, bar_down = create_bar()


def draw():
    # Draw the background, bird, and obstacles
    background.draw()
    bird.draw()
    bar_up.draw()
    bar_down.draw()

    # Draw the score at the top-left corner
    screen.draw.text(f'Score: {score}', (10, 10), color="white", fontsize=24)


def update():
    global score, bar_up, bar_down

    # Apply gravity to the bird, making it fall over time
    bird.y += bird.gravity * 5

    # Move the obstacles to the left
    bar_up.x -= bar_up.speed
    bar_down.x -= bar_down.speed

    # Check if obstacles move off-screen, reset them and increase score
    if bar_up.x < -bar_up.width:
        bar_up, bar_down = create_bar()  # Create a new pair of obstacles
        score += 1  # Increase score when bird successfully passes

    # Collision detection
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) or bird.y > HEIGHT:
        reset_game()  # Reset the game if the bird hits an obstacle or falls off


def on_mouse_down():
    bird.y -= 50  # Make the bird fly up slightly


def reset_game():
    global score, bar_up, bar_down
    bird.y = HEIGHT / 2  # Reset bird's position
    score = 0  # Reset score
    bar_up, bar_down = create_bar()  # Create new obstacles


pgzrun.go()
