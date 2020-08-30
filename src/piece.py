import itertools


class Piece:
    def __init__(self, id,
                 is_round, is_tall, is_dark, has_tophole, is_used=False):
        self.id = id
        self.is_round = is_round
        self.is_tall = is_tall
        self.is_dark = is_dark
        self.has_tophole = has_tophole
        self.is_used = is_used

    def used(self):
        self.is_used = True

    # def check_is_used(self):
    #     return self.is_used

    def get_piece_fetures(self):
        features = [
            self.is_round,
            self.is_tall,
            self.is_dark,
            self.has_tophole]
        return features

    def to_string(self):
        shape = 'round' if self.is_round else 'square'
        height = 'tall' if self.is_tall else 'low'
        color = 'dark' if self.is_dark else 'light'
        top = 'hole on top' if self.has_tophole else 'flat top'
        return self.id, shape + '\n' + height + '\n' + color + '\n' + top

    def reset(self):
        self.is_used = False


class Pieces:
    def __init__(self):
        self.all_pieces_ids = [i for i in range(1, 17)]

        bool_list = [True, False]
        h = list(itertools.product(bool_list, bool_list, bool_list, bool_list))
        self.pieces = {id: Piece(id, *v)
                       for id, v in zip(self.all_pieces_ids, h)}

    # def get_all_pieces_ids(self):
    #     return self.all_pieces_ids

    # def get_all_pieces(self):
    #     return self.pieces

    def get_piece_by_id(self, id):
        return self.pieces[id]

    def get_used_pieces_ids(self):
        used_pieces_ids = [
            k for k, v in self.pieces.items() if v.is_used]
        return used_pieces_ids

    def get_used_pieces(self):
        used_pieces = {k: v for k, v in self.pieces.items() if v.is_used}
        return used_pieces

    def get_not_used_pieces_ids(self):
        not_used_pieces_ids = [
            k for k, v in self.pieces.items() if not v.is_used]
        return not_used_pieces_ids

    def get_not_used_pieces(self):
        not_used_pieces = {k: v for k, v
                           in self.pieces.items() if not v.is_used}
        return not_used_pieces

    def update_used_piece(self, id):
        self.pieces[id].used()

    def reset(self):
        for piece in self.pices.values():
            piece.reset()


if __name__ == "__main__":
    pieces = Pieces()
    print(type(pieces.get_piece_by_id(1)), len(pieces.pieces))

    use_piece_id = 3
    pieces.update_used_piece(use_piece_id)
    used_pieces = pieces.get_used_pieces()
    print(len(used_pieces))

    used_piece_id, used_piece_feature = used_pieces[use_piece_id].to_string()
    print(used_piece_feature)
