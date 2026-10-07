# puzzle.py
PUZZLES = {
    "easy": [
        {"id": 1, "match": "Emir Duhan Akgun vs. Mesut Atabay (2026)", "fen": "5r1k/7p/5Pp1/4Q3/P2p4/q3n1PP/5R1K/2R5 w - - 1 38", "moves": ["f7"], "desc": "Checkmate in one move."},
        {"id": 2, "match": "Emir Duhan Akgun vs. Idris Can Demircan (2026)", "fen": "r1b1r3/pp3Rpp/2ppk3/6B1/2PP4/8/PP4PP/5RK1 w - - 6 21", "moves": ["rg7", "bd7", "rf6"], "desc": "Checkmate in two moves."}
    ],
    "mid": [
        {"id": 3, "match": "Emir Duhan Akgun vs. GM Şehriyar Memmedyarov (2022)", "fen": "r2q1r1k/1bpnp1bp/1p1p2p1/5p2/3P1B2/1QP2NP1/P3PPBP/R3R1K1 w - - 0 14", "moves": ["ng5", "bxg2", "nxf8"], "desc": "Win the exchange or create severe threats."},
        {"id": 4, "match": "GM Magnus Carlsen vs. Emir Duhan Akgun (2022)", "fen": "3r2k1/1q1P1pp1/pnp1p2p/1p2N3/4P3/8/PPQ2PPP/3R2K1 w - - 1 26", "moves": ["qc5", "nxd7", "qe7"], "desc": "Dominate the 7th rank."}
    ],
    "hard": []  # (Coming Soon)
}