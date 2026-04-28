def checkmate(board):
    try:
        rows = board.splitlines()

        if not rows:
            return

        size = len(rows)

        if any(len(row) != size for row in rows):
            return

        # หา King
        kr, kc = -1, -1
        count = 0

        for r in range(size):
            for c in range(size):
                if rows[r][c] == "K":
                    kr, kc = r, c
                    count += 1

        if count != 1:
                return
        # Pawn check
        for dr, dc in [(-1, -1), (-1, 1)]:
            r = kr - dr
            c = kc - dc
            if 0 <= r < size and 0 <= c < size:
                if rows[r][c] == "P":
                    print("Success")
                    return

        # Rook / Bishop / Queen
        directions = [
            (-1,0),(1,0),(0,-1),(0,1),
            (-1,-1),(-1,1),(1,-1),(1,1)
        ]

        for dr, dc in directions:
            
            r = kr + dr
            c = kc + dc

            while 0 <= r < size and 0 <= c < size:
                piece = rows[r][c]
                    #ตั้งเงื่อนไขเเยกR/Q/B
                if piece != ".":
                    if (dr == 0 or dc == 0) and piece in ("R","Q"):
                        print("Success")
                        return

                    if (dr != 0 and dc != 0) and piece in ("B","Q"):
                        print("Success")
                        return

                    break

                r += dr
                c += dc

        print("Fail")

    except:
        return