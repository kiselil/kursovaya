class Group_of_sprite():
    def __init__(self, Character1, Character2):
        self.Character1 = Character1
        self.Character2 = Character2
    def go_to_initial_position(self):
        self.Character1.go_to_initial_position()
        self.Character2.go_to_initial_position()
    def set_level(self,current_level):
        self.Character1.set_level(current_level)
        self.Character2.set_level(current_level)
    def update(self):
        self.Character1.update()
        self.Character2.update()
    def draw(self, screen):
        self.Character1.draw(screen)
        self.Character2.draw(screen)
    def check_win_condition(self):
        return self.Character1.check_win_condition() and self.Character2.check_win_condition()
    def check_lose_condition(self):
        return self.Character1.check_lose_condition() or self.Character2.check_lose_condition()