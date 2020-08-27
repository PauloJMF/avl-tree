def get_matrix_tree_preorder(tree):

    row, tree.current_row = 0, 0
    N, M = pow(2, tree.max_height+1), tree.max_height+2
    tree.final_matrix = [[None for x in range(M)] for y in range(N)] 
    tree.root.fill_matrix_preorder(None, tree, 0)

    tree.final_matrix[0][0] = '[root]'
    for i in range(N):
        if tree.final_matrix[i][0] == None:
            continue
        tree.final_matrix[i][0] = tree.final_matrix[i][0].replace("│      ", "  │    ")

    for j in range(1, M):
        for i in range(N):
            if tree.final_matrix[i][j] == None:
                continue
            tree.final_matrix[i][j] = tree.final_matrix[i][j].replace("│      ", "  │    ")
            if tree.final_matrix[i][j][0] == '└':
                tree.final_matrix[i][j] = tree.final_matrix[i][j].replace('└', '—')
                tree.final_matrix[i][j-1] = "{:7}".format("  └————")

    for j in range(M):
        for i in range(N-1, j, -1):
            if tree.final_matrix[i][j] == None:
                continue
            if tree.final_matrix[i][j][:3] == '  │':
                tree.final_matrix[i][j] = "{:8}".format("")
            else:
                break

    for j in range(M-3):
        son, dad = [], []
        for i in range(N):
            if tree.final_matrix[i][j] == None:
                continue
            if tree.final_matrix[i][j][2] == '└':
                son.append(i) 
            if tree.final_matrix[i][j][2] == '[':
                dad.append(i)

        for i, val in enumerate(dad):
            if i == 0:
                continue
            aux = -1
            for val2 in son:
                if val2 > aux and val2 < val:
                    aux = val2
            for z in range(aux+1, val):
                tree.final_matrix[z][j] = "{:8}".format("")

    return tree.final_matrix

def show_tree(matrix):
    N, M = len(matrix), len(matrix[0])
    for i in range(N):
        str_ = ""
        cond = False
        for j in range(M):
            if matrix[i][j] == None:
                cond = cond or False
                continue
            cond = cond or True
            str_ += str(matrix[i][j])
        if cond == False:
            break
        print(str_)
