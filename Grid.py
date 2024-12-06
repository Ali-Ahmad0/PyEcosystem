import pygame
import random
import heapq

class Grid:
    def __init__(self, screen, grid_size, cell_size):
        # Initialize move counter first
        self.move_count = 0
        
        self.screen = screen
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.window_size = self.grid_size * self.cell_size
        
        # Initialize grid
        self.grid = [[0 for _ in range(self.grid_size)] 
                     for _ in range(self.grid_size)]
        
        # Create player and goal positions
        self.player_pos = self._random_position()
        self.goal_pos = self._random_position()
        while self.goal_pos == self.player_pos:
            self.goal_pos = self._random_position()
            
        # Draw initial grid
        self.draw_grid()
        
        # Start movement
        self.path = self.a_star(self.player_pos, self.goal_pos)
        self.move_player()
        
    def _random_position(self):
        return (random.randint(0, self.grid_size-1), 
                random.randint(0, self.grid_size-1))
        
    def draw_grid(self):
        # Clear screen
        self.screen.fill((255, 255, 255))
        
        # Draw grid lines
        for i in range(self.grid_size + 1):
            # Vertical lines
            x = i * self.cell_size
            pygame.draw.line(self.screen, (128, 128, 128), (x, 0), (x, self.window_size))
            
            # Horizontal lines
            y = i * self.cell_size
            pygame.draw.line(self.screen, (128, 128, 128), (0, y), (self.window_size, y))
        
        # Draw goal (yellow square)
        goal_x = self.goal_pos[1] * self.cell_size
        goal_y = self.goal_pos[0] * self.cell_size
        pygame.draw.rect(self.screen, (255, 255, 0), 
                         (goal_x + 2, goal_y + 2, 
                          self.cell_size - 4, self.cell_size - 4))
        
        # Draw player (green square)
        player_x = self.player_pos[1] * self.cell_size
        player_y = self.player_pos[0] * self.cell_size
        pygame.draw.rect(self.screen, (0, 255, 0), 
                         (player_x + 2, player_y + 2, 
                          self.cell_size - 4, self.cell_size - 4))
        
        # Update move counter
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Moves: {self.move_count}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
        
        pygame.display.flip()
        
    def move_player(self):
        if self.path:
            self.player_pos = self.path.pop(0)
            self.move_count += 1
            
            # Redraw grid
            self.draw_grid()
            
            # Schedule next move
            pygame.time.set_timer(pygame.USEREVENT, 100)
        else:
            # Game over - display win message
            font = pygame.font.SysFont(None, 48)
            text = font.render(f"Goal reached in {self.move_count} moves!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(self.window_size // 2, self.window_size // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
    
    def a_star(self, start, goal):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path
            
            neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            neighbors = [n for n in neighbors if 0 <= n[0] < self.grid_size and 0 <= n[1] < self.grid_size]
            
            for neighbor in neighbors:
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return []