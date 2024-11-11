import pgzrun

WIDTH = 800
HEIGHT = 400

# Load the girl sprite as an Actor
girl = Actor('girl_walk1')
girl.x = WIDTH // 2
girl.y = HEIGHT // 2
girl_speed = 3

# Direction to control the image flip (initially facing right)
facing_right = True

# Animation frame variables
walk_frames = ['girl_walk1', 'girl_walk2', 'girl_walk3', 'girl_walk4']
current_frame = 0
frame_delay = 5  # Delay between frames to control speed of animation
frame_count = 0  # Counter to control when to switch frames


def draw():
    screen.clear()
    girl.draw()


def update():
    global facing_right, current_frame, frame_count

    moving = False  # Track if the girl is moving

    # Move the girl to the right
    if keyboard.right:
        girl.x += girl_speed
        if not facing_right:
            girl.flip_x = False  # Face right
            facing_right = True
        moving = True

    # Move the girl to the left
    elif keyboard.left:
        girl.x -= girl_speed
        if facing_right:
            girl.flip_x = True  # Face left
            facing_right = False
        moving = True

    # Handle animation if moving
    if moving:
        frame_count += 1
        if frame_count >= frame_delay:
            current_frame = (current_frame + 1) % len(walk_frames)
            girl.image = walk_frames[current_frame]
            frame_count = 0
    else:
        girl.image = walk_frames[0]  # Reset to the first frame when idle

    # Optional: Keep the girl within the screen boundaries
    if girl.x < 0:
        girl.x = 0
    elif girl.x > WIDTH:
        girl.x = WIDTH


pgzrun.go()
