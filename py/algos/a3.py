class ZobristHash:
    def __init__(self, board_size, num_pieces):
        self.board_size = board_size
        self.num_pieces = num_pieces
        self.hash_table = [[0] * num_pieces for _ in range(board_size)]
        # Initialize the hash table with random values

    def calculate_hash(self, board):
        hash_value = 0
        for row in range(self.board_size):
            for col in range(self.board_size):
                piece = board[row][col]
                hash_value ^= self.hash_table[row][piece]
        return hash_value
