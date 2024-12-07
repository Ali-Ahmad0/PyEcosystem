
class Camera:
    # Camera offset
    offset_x = 0
    offset_y = 0

    # Move the camera
    @staticmethod
    def move(dx, dy):
        Camera.offset_x += dx
        Camera.offset_y += dy

    # Render object
    @staticmethod
    def apply(surface, rect, screen):
        new_rect = rect.move(-Camera.offset_x, -Camera.offset_y)
        screen.blit(surface, new_rect)