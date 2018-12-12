def soma_matrizes(m1, m2):
    dim1 = (str(len(m1))+'X'+str(len(m1[0])))
    dim2 = (str(len(m2))+'X'+str(len(m2[0])))
    if dim1 == dim2:
        res = []
        for x in range(len(m1)):
            row = []
            for j in range(len(m1[0])):
                row.append(m1[x][j] + m2[x][j])
            res.append(row)
        return res
    else:
        return False