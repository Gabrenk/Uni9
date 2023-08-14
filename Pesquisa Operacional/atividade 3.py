#Breno Gaspar Caetano
#RA: 923116534
from scipy.optimize import linprog

def linear_prog(n, Obj, A, B, X, bounds=(0, None), A_eq=None, B_eq=None,):
    """ 
    Function that will use the linprog method to calculate the best possible
    outcome of a linear programming problem, then print the answer in an easy
    to read manner.

    Args:
        n: (int) number of the exercise
        Obj: (list) list with the values we want to maximize
        A:(list of lists/ matrix) inequality constraint matrix
        B: (list)  inequality constraint vector
        X: (list) list with the names of the variables
        bounds: (list of pairs) define the min|max values of a variable.
        A_eq: (list of lists/matrix) equality constraint matrix
        B_eq: (list) equality constraint vector

    """
    opt = linprog(Obj, A, B, A_eq, B_eq, bounds, method="highs")
    print("--------------------------")
    print(f"Exercício {n}")
    if opt.success:
        print("O resultado máximo é alcançado quando:")
        for n in range(len(X)):
            print(X[n], "= ", (opt.x[n]))
    else:
        print("o sistema não possui solução")

linear_prog(1, [-120, -150], [[2, 4], [3, 2], [5,3]], [100, 90, 120], [ 'P1', 'P2'])

linear_prog(2, [-30, -40], [[3, 5]], [[50]], ['Produto A', ' Produto B'])

linear_prog(3, [0.4, 0.3, 0.15, 0.55], [[1, 1, 1, 1]], [1],
            bounds =[(0.10, 0.25), (0.08, 0.25),(0.10, 0.30), (0.03, 0.10)],
            X=['Ferro', 'Carvão', 'Silício', 'Niquel'])

linear_prog(4, [0.8, 0.6], [[0.2, 0.32]], [0.25], ['Bovina', 'Suina'], 
            A_eq=[[1,1]], B_eq=[1],)

