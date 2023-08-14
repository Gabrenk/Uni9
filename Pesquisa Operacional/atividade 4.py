#Breno Gaspar Caetano
#RA: 923116534

import copy

class Main(object):
    """
    A collection of methods that will serve as tools in decision taking problems
    Function names are self explanatory, no further description needed
    """
    def __init__(self, names, decisions, probabilities=None):
        """
            Args:
            names (list[str]): names of each row
            decisions (list[list[int]]): matrix of values, with each entry 
                                        representing a row aka impact
            probabilities (list[int]): list of probabilistic values which inter-
                                        fere with the respective columns 
        """
        self.names = names
        self.decisions = decisions
        self.probabilities = probabilities

    def maximax(self):
        max_dic = {}
        for name, row in zip(self.names, self.decisions):
            max_dic[name] = max(row)
        
        temp = max(max_dic, key=max_dic.get)
        print("----------------------")
        print("Segundo o método Maximax, a melhor alternativa é a:")
        print (temp, max_dic[temp])
        
    def maximin(self):
        min_dic = {}
        for name, row in zip(self.names, self.decisions):
            min_dic[name] = min(row)
        
        temp = max(min_dic, key=min_dic.get)
        print("----------------------")
        print("Segundo o método Maximin, a melhor alternativa é a:")
        print (temp, min_dic[temp])

    def laplace(self):
        laplace_dic = {}
        for name, row in zip(self.names, self.decisions):
            laplace_dic[name] = sum(row)/len(row)
        
        temp = max(laplace_dic, key=laplace_dic.get)
        print("----------------------")
        print("Segundo o método Laplace, a melhor alternativa é a:")
        print (temp, laplace_dic[temp])

    def VEA(self):
        curr_decisions = copy.deepcopy(self.decisions)
        for row in curr_decisions:
            for i in range(len(row)):
                row[i] *= self.probabilities[i]


        VEA_dic = {}
        for name, row in zip(self.names, curr_decisions):
            VEA_dic[name] = sum(row)
        
        temp = max(VEA_dic, key=VEA_dic.get)
        print("----------------------")
        print("Segundo o método VEA, a melhor alternativa é a:")
        print (temp, VEA_dic[temp])


    def Bayes(self, min_or=True):
        """
        can be set to return the max or min values
            Args:
            min_or (Boolean): boolean value that serves as a switch.
        """
        curr_decisions = copy.deepcopy(self.decisions)
        if self.probabilities:##checar dps
            for row in curr_decisions:
                for i in range(len(row)):
                    row[i] *= self.probabilities[i]

        row_sum = {}
        for name, row in zip(self.names, curr_decisions):
            row_sum[name] = sum(row)

        if min_or == True:
            temp = min(row_sum, key=row_sum.get)
            print("----------------------")
            print("O resultado mínimo será alcançado com:")
            print (temp, row_sum[temp])
        else:
            temp = max(row_sum, key=row_sum.get)
            print("----------------------")
            print("O resultado máximo será alcançado com:")
            print (temp, row_sum[temp])


if __name__ == '__main__':
    print('Exercício 1')
    decisions = [[400, 900, 950], [850, 450, 800], [700, 700, 650]]
    names = ['d1', 'd2', 'd3']
    a = Main(names, decisions)
    a.Bayes()

    print('\n\nExercício 2')
    decisions = [[700, -100], [90, 90]]
    probabilities = [0.25, 0.75]
    names = ['perfurar', 'vender']
    b =Main(names, decisions, probabilities)
    b.Bayes(False)

    print('\n\nExercício 3')
    decisions = [[25, 12, 18], [8, 20, 34], [14, 30, 16], [20, 15, 25]]
    probabilities = [0.3, 0.25, 0,45]
    names = ['A1', 'A2', 'A3', 'A4']
    c = Main(names, decisions, probabilities)
    c.Bayes(False)

    print('\n\nExercício 4')
    c.maximax()
    c.maximin()
    c.laplace()

    print('\n\nExercício 5')
    decisions = [[4, 15], [-20, 50], [0, 0]]
    probabilities = [0.6, 0.4]
    names = ['Local', 'Nacional', 'Não lançar']
    d = Main(names, decisions, probabilities)
    d.maximax()
    d.maximin()
    d.laplace()
    d.VEA()

    print("""\n\nO metodo maximax busca sempre o valor com o melhor retorno máximo.
O método maximin, por sua vez, vai encontrar a decisão com o maior valor mínimo.
Já Laplace vai buscar a maior média máxima enquanto que VEA nos mostrará o maior
valor após sofrer com os pesos.
De forma geral, as  estratégias de mercado sempre tem que levar em conta o risco
das operações, assim a VEA é a mais indicada""")
    
