#Breno Gaspar Caetano
#RA: 923116534
import numpy as np

def Linear_solver(A_list, B_list, X_list, Ex_number):
    A = np.array(A_list)
    B = np.array(B_list)
    X = X_list

    print("---------------")
    print(f"Exercício {Ex_number}: ")
    #A^-1 only possible if det(A) != 0
    if np.linalg.det(A) == 0.0:
        print("Matriz Possível e indeterminada")
    else:
        results = np.linalg.solve(A,B)
        for n in range(len(X)):
            print(X[n]," =", int(results[n]))

#
Linear_solver([[2,-1],[1, 5]], [[7], [-2]], ["x", "y"], "1")
Linear_solver([[1, 2, -1],[3, -4, 5], [1, 1, 9]], [[0], [10], [1]],
              ["x", "y", "z"], "2")
Linear_solver([[1,2],[2, 3]], [[5], [-4]], ["x", "y"], "3")
Linear_solver([[1, 1],[2, 2]], [[5], [10]], ["x", "y"], "4")
Linear_solver([[2,-1, 1],[1, -1, 2], [1, 1, 1]], [[3], [-3], [6]],
              ["x", "y", "z"], "5")
Linear_solver([[1, 4, 7],[2, 3, 6], [5, 1, -1]], [[2], [2], [8]],
              ["x", "y", "z"], "6")

Linear_solver([[0.15, 0.1, 0.06], [1, 1, -1], [1, 1, 1]],
               [[20000], [0], [200000]],
                 ["x", "y", "z"], "7")

