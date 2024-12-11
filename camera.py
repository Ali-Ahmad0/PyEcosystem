import pygame

class Camera:
    # Camera offset
    offset_x = 0
    offset_y = 0

    zoom = 1

    # Move the camera
    @staticmethod
    def move(dx, dy):
        Camera.offset_x += dx
        Camera.offset_y += dy

    # Render object
    @staticmethod
    def apply(surface, rect, screen):
        """Apply camera transformations (offset and zoom) to a surface
        
        Args:
            surface (Surface): Surface to render
            rect (Rect): Position rectangle
            screen (Surface): Screen to render to
        """
        # Handle zoom
        if Camera.zoom != 1:
            # Calculate scaled dimensions
            scaled_w = int(surface.get_width() * Camera.zoom)
            scaled_h = int(surface.get_height() * Camera.zoom)
            
            # Scale the surface
            scaled_surface = pygame.transform.scale(surface, (scaled_w, scaled_h))
            
            # Create a new rect with scaled dimensions
            scaled_rect = pygame.Rect(
                rect.x * Camera.zoom,
                rect.y * Camera.zoom,
                scaled_w,
                scaled_h
            )
        else:
            scaled_surface = surface
            scaled_rect = rect

        # Apply camera offset to the scaled rect
        new_rect = scaled_rect.move(-Camera.offset_x, -Camera.offset_y)
        screen.blit(scaled_surface, new_rect)