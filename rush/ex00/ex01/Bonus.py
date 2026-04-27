def king_in_check(rows):
    size = len(rows)

    # ----- validate square board -----
    if size == 0:
        return None

    if any(len(row) != size for row in rows):
        return None

    # valid pieces
    allowed = {'.', 'K', 'Q', 'R', 'B', 'P'}

    king_count = 0
    kr, kc = -1, -1

    for r in range(size):
        for c in range(size):
            piece = rows[r][c]

            if piece not in allowed:
                return None

            if piece == 'K':
                king_count += 1
                kr, kc = r, c

    # must have exactly one king
    if king_count != 1:
        return None


    # ----- rook / queen attacks -----
    directions = [
        (-1,0),(1,0),(0,-1),(0,1),      # rook
        (-1,-1),(-1,1),(1,-1),(1,1)     # bishop
    ]

    for dr, dc in directions:
        r = kr + dr
        c = kc + dc

        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]

            if piece != '.':
                if (dr == 0 or dc == 0):      # straight
                    if piece in ('R','Q'):
                        return True
                else:                         # diagonal
                    if piece in ('B','Q'):
                        return True
                break

            r += dr
            c += dc


    # ----- pawn attacks (from above) -----
    for dc in (-1, 1):
        r = kr - 1
        c = kc + dc

        if 0 <= r < size and 0 <= c < size:
            if rows[r][c] == 'P':
                return True


    return False