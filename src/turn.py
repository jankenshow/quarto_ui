class Turn:

    def __init__(self):
        self.first_player_active = True
        # self.selected_piece_id = 0
        self.turn_id = 0

    # def update_selected_piece(self, id):
    #     self.selected_piece_id = id

    def change_turn(self):
        self.first_player_active = False
        self.turn_id += 1

    def get_info(self):
        return self.turn_id, self.first_player_active

    def reset(self):
        self.first_player_active = True
        self.turn_id = 0


if __name__ == '__main__':
    turn = Turn()
    print(turn.get_info())
    turn.change_turn()
    print(turn.get_info())
