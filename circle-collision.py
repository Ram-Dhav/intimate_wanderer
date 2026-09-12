import math

def check_circle_collision(x1, y1, r1, x2, y2, r2, screen_width=800, screen_height=600):
    # 1. Check if Circle 1 is inside screen
    c1_in_screen = (0 <= x1 - r1) and (x1 + r1 <= screen_width) and \
                   (0 <= y1 - r1) and (y1 + r1 <= screen_height)
                   
    # 2. Check if Circle 2 is inside screen
    c2_in_screen = (0 <= x2 - r2) and (x2 + r2 <= screen_width) and \
                   (0 <= y2 - r2) and (y2 + r2 <= screen_height)
    
    # 3. Distance between centers
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 4. Collision check
    sum_radii = r1 + r2
    diff_radii = abs(r1 - r2)
    
    intersects = diff_radii < distance < sum_radii
    
    return {
        "c1_in_screen": c1_in_screen,
        "c2_in_screen": c2_in_screen,
        "distance": distance,
        "intersects": intersects
    }

# Example run using the problem values
result = check_circle_collision(100, 150, 80, 250, 230, 100)
print(result)
