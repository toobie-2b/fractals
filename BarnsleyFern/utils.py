fern_type = {
    'original':[[0.0, 0, 0.0, 0.16, 0.0, 0.0, 0.01],
        [0.85, 0.04, -0.04, 0.85, 0.0, 1.60, 0.85],
        [0.20, -0.26, 0.23, 0.22, 0.0, 1.60, 0.07],
        [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07]],

    'mutant':[[0.0, 0.0, 0.0, 0.25, 0.0, -0.4, 0.02],
        [0.95, 0.005, -0.005, 0.93, -0.002, 0.5, 0.84],
        [0.035, -0.2, 0.16, 0.04, -0.09, 0.02, 0.07],
        [-0.04, 0.2, 0.16, 0.04, 0.083, 0.12, 0.07]]
}


def calculate(x, y, prob, fern):
    if prob < fern[0][6]:
        X = fern[0][0] * x + fern[0][1] * y + fern[0][4]
        Y = fern[0][2] * x + fern[0][3] * y + fern[0][5]
    elif prob < fern[0][6] + fern[1][6]:
        X = fern[1][0] * x + fern[1][1] * y + fern[1][4]
        Y = fern[1][2] * x + fern[1][3] * y + fern[1][5]
    elif prob < fern [0][6] + fern[1][6] + fern[2][6]:
        X = fern[2][0] * x + fern[2][1] * y + fern[2][4]
        Y = fern[2][2] * x + fern[2][3] * y + fern[2][5]
    else:
        X = fern[3][0] * x + fern[3][1] * y + fern[3][4]
        Y = fern[3][2] * x + fern[3][3] * y + fern[3][5]

    return X, Y