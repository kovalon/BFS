import time

# Создадим матрицу смежности для создания математической модели графа.
# В матрице каждый элемент - это вершина графа, к нему добавлен список, в котором 1 и 0 указывает,
# с какими вершинами имеется связь (1), с какими - нет (0).
# None означает, что данная вершина не была пройдена. Если она пройдена,
# то вместо None будет стоять значение глубины уровня.
# В проекте есть фотография, в котором визуализрован данный граф.
mathGraph = {1: [[0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], None],
             2: [[1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], None],
             3: [[0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], None],
             4: [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], None],
             5: [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], None],
             6: [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], None],
             7: [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], None],
             8: [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], None],
             9: [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0], None],
             10: [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], None],
             11: [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], None],
             12: [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], None]}


#  Функция, выводящая граф в нужном нам виде.
def printGraph(graph):
    for string in graph:
        print(graph.get(string))


# Введем в очередь, из которой будут браться вершины для анализа, изначальную вершину, с которой хотим начать обход
queue = [1]
mathGraph.get(1)[1] = 0  # у данной вершины уровень глубины равен 0


def bfsResolver():
    while True:  # пополнять очередь будем в цикле
        index = queue.pop(0)  # достаем очередную вершину, от которй будем
        # искать еще не пройденные вершины и присавивать им их уровень
        for element in range(12):  # проходимся по вершинам, которые смежны с данной вершиной
            # если они еще не пройдены
            if mathGraph.get(index)[0][element] is 1 and mathGraph.get(element + 1)[1] is None:
                queue.append(element + 1)  # тогда добавляем их в очередь
                mathGraph.get(element + 1)[1] = (mathGraph.get(index)[1] + 1) # и присваиваем им уровень
        printGraph(mathGraph)  # выводим текущий результат
        print("queue = " + str(queue) + "\n") # выводим текущее состояние очереди
        time.sleep(1)
        if not queue: # работаем, пока очередь не опустеет
            break

    print("Done!")


bfsResolver() # запускаем реализацию алгоритма
