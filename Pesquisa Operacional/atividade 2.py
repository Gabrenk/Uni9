#Breno Gaspar Caetano
#RA: 923116534
from scipy.optimize import linprog

def linear_prog(n, Obj, A, B, X, A_eq=None, B_eq=None):
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
        A_eq: (list of lists/matrix) equality constraint matrix
        B_eq: (list) equality constraint vector

    """
    opt = linprog(Obj, A, B, A_eq, B_eq, method="highs")
    print("--------------------------")
    print(f"Exercício {n}")
    if opt.success:
        print("O resultado máximo é alcançado quando:")
        for n in range(len(X)):
            print(X[n], "= ", int(opt.x[n]))
    else:
        print("o sistema não possui solução")
    
linear_prog(1, [-5, -2], [[10,12], [2,1]], [60, 6], ["sapato", "cinto"])

linear_prog(2, [-100, -150], [[2, 3], [1, 0], [0, 1]],
           [120, 40, 30], ["p1", "p2"])

linear_prog(3, [-20, -10, -30], [[1, 1, 1], [0, 0, 1]], [800, 200],
             ["laranja", "Pessego", "Tangerina"], A_eq =  [ [0, 1, 0], [1,0,1]],
            B_eq= [[100], [700]])

linear_prog(4, [-30000, -10000], [[20, 10]],
         [80], ["Programa A", "Programa B"], A_eq=[[1, 1]], B_eq=[[5]])

linear_prog(5, [-4, -3], [[2, 1], [1, 1], [1, 0], [0,1]], [1000, 800, 400, 700], ["M1", "M2"])
        