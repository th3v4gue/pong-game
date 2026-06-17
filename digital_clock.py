import pygame
import datetime
import pytz
from collections import OrderedDict

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (25, 25, 112)
CYAN = (0, 255, 255)
LIGHT_GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Digital Clock - Multiple Time Zones")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 1  # Update once per second

# Fonts
title_font = pygame.font.Font(None, 48)
timezone_font = pygame.font.Font(None, 36)
time_font = pygame.font.Font(None, 72)
info_font = pygame.font.Font(None, 24)

# Time zones to display
# OrderedDict maintains the order of insertion
timezones = OrderedDict([
    ("New York", "America/New_York"),
    ("London", "Europe/London"),
    ("Tokyo", "Asia/Tokyo"),
    ("Sydney", "Australia/Sydney"),
    ("Dubai", "Asia/Dubai"),
    ("Los Angeles", "America/Los_Angeles"),
    ("Singapore", "Asia/Singapore"),
    ("Toronto", "America/Toronto"),
])

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Draw everything
    screen.fill(DARK_BLUE)
    
    # Draw title
    title_text = title_font.render("Global Digital Clock", True, CYAN)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    screen.blit(title_text, title_rect)
    
    # Draw subtitle with current date
    now_utc = datetime.datetime.now(pytz.UTC)
    date_text = info_font.render(f"Current Date (UTC): {now_utc.strftime('%A, %B %d, %Y')}", True, LIGHT_GRAY)
    date_rect = date_text.get_rect(center=(SCREEN_WIDTH // 2, 70))
    screen.blit(date_text, date_rect)
    
    # Draw separator line
    pygame.draw.line(screen, CYAN, (50, 100), (SCREEN_WIDTH - 50, 100), 2)
    
    # Calculate positions for timezone clocks
    clocks_per_row = 2
    clock_width = (SCREEN_WIDTH - 100) // clocks_per_row
    clock_height = 150
    start_y = 130
    start_x = 50
    spacing_y = 160
    
    # Draw time zones
    tz_list = list(timezones.items())
    for idx, (city, tz_name) in enumerate(tz_list):
        # Calculate position
        row = idx // clocks_per_row
        col = idx % clocks_per_row
        x = start_x + (col * clock_width)
        y = start_y + (row * spacing_y)
        
        # Get current time in that timezone
        tz = pytz.timezone(tz_name)
        local_time = datetime.datetime.now(tz)
        
        # Format time
        time_str = local_time.strftime("%H:%M:%S")
        date_str = local_time.strftime("%b %d")
        
        # Draw clock box
        box_rect = pygame.Rect(x, y, clock_width - 20, 140)
        pygame.draw.rect(screen, (40, 40, 80), box_rect)
        pygame.draw.rect(screen, CYAN, box_rect, 2)
        
        # Draw city name
        city_text = timezone_font.render(city, True, YELLOW)
        city_rect = city_text.get_rect(center=(x + (clock_width - 20) // 2, y + 15))
        screen.blit(city_text, city_rect)
        
        # Draw time
        time_text = time_font.render(time_str, True, GREEN)
        time_rect = time_text.get_rect(center=(x + (clock_width - 20) // 2, y + 60))
        screen.blit(time_text, time_rect)
        
        # Draw date
        date_display = info_font.render(date_str, True, LIGHT_GRAY)
        date_display_rect = date_display.get_rect(center=(x + (clock_width - 20) // 2, y + 115))
        screen.blit(date_display, date_display_rect)
    
    # Draw footer
    pygame.draw.line(screen, CYAN, (50, SCREEN_HEIGHT - 50), (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50), 2)
    footer_text = info_font.render("Press ESC to exit | Updates every second", True, LIGHT_GRAY)
    footer_rect = footer_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
    screen.blit(footer_text, footer_rect)
    
    pygame.display.flip()

pygame.quit()
