class Node:
    """Данный класс является элементарной частицей дерева. Каждый объект этого класса обладает значением, цветом (красным или чёрным) и ссылками на два других объекта этого же класса. Правая ссылка указывает на объект со значением больше, чем собственное, левая - меньше."""

    def __init__(self, value, left = None, right = None):
        """При инициализации нового узла, его цвет по умолчанию всегда красный."""
        self.value = value
        self.is_red = True
        self.left = left
        self.right = right

    def __str__(self):
        """Метод возвращает строку с полной информацией об узле: его значении, цвете, левой и правой ссылках (если они есть)"""        
        res = f'Значение узла: {self.value}'
        if self.is_red:
            res +=  f', цвет: красный'
        else:
            res +=  f', цвет: чёрный'
        if self.left:
            res +=  f', значение левого: {self.left.value}'
        if self.right:
            res +=  f', значение правого: {self.right.value}'            
        return res

class Tree:
    """Класс является левосторонним красно-черное деревом.
    Объект данного класса состоит из узлов (класс Node) с уникальными значениями, и обладает следующими характеристиками:
    • Каждый узел имеет цвет (красный или черный).
    • Корень дерева всегда черный.
    • Новый узел всегда красная.
    • У краной ноды все дети черного цвета.
    • Количество чёрных узлов во всех ветках одинаковое."""

    def __init__(self, root = None):
        self.root = root
        if root != None:
            self.root.is_red = False

    def search(self, node, data, parent = None): 
        """Рекурсивный поиск элемента по деверу.
        На вход принимает:
        node - элемент, с которого начинается поиск. При запуске поиска это значение должно быть равно self.root, чтобы поиск производился с самого начала дерева,
        data - значение искомого элемента,
        parent - родитель параметра node, по умолчанию равен None.
        На выходе метод выдаёт кортеж, состоящий из двух объектов класса Node, где первый - это искомый элемент или None, если элемент не найден, второй - родитель искомого узла."""       
        if node == None or data == node.value:              
            return [node, parent]
        if data > node.value:             
            return self.search(node.right, data, node)
        if data < node.value:            
            return self.search(node.left, data, node)        

    def add_node(self, value):
        """Метод добавления нового узла в дерево.
        Принимает на вход значение добавляемого узла.
        Прежде всего проверяет, если корень дерева равен None, значит добавляемый элемент первый, и он становится корнем.
        Если вставляемый элемент не первый, ведётся поиск элемента с добавляемым значением. Если элемент найден, выводится надпись, что такой элемент уже есть. Если элемент не найден, то есть первое значение полученного кортежа равно None, то родителем нового элемента становится узел, прописанный как второе значение полученного кортежа. В зависимости от того, больше вставляемое значение, чем значение родителя или меньше, у узла-родителя прописывается правая или левая ссылка на новый узел соответственно.
        После добаления нового узла, вызывается метод балансировки дерева, в который передаётся ссылка на новый узел."""
        if self.root == None:
            self.root = Node(value)
            self.root.is_red = False
        else:
            res = self.search(self.root, value)
            if res[0] == None:
                new_node = Node(value)                
                if value > res[1].value:
                    res[1].right = new_node
                else:
                    res[1].left = new_node
                if res[1] != self.root:
                    self.balance_tree(new_node)
            else:
                print('Ой все, такое значение уже есть')

    def print_tree(self, node):
        """Рекурсивный обход дерева для его распечатки от меньшего элемента к большему.
        На вход принимает элемент, с которого следует начать обход дерева. Чтобы обойти всё дерево, это значение должно быть self.root."""
        if node != None:
            self.print_tree(node.left)
            print(node)
            self.print_tree(node.right)

    def balance_tree(self, node):
        """Метод балансировки дерева.
        На вход принимает объект, с которого следует начать балансировку.
        Прежде всего вычисляет узлы-родители полученного объекта: отца и дедушку.
        Если отец является корнем дерева, значит балансировка не требуется, и метод прерывается.
        Далее вычисляется дядя полученного объекта, то есть второй потомок дедушки.
        Если дядя красный производится балансировка дерева при помощи смены цветов отдельных элементов.
        Если же дядя чёрный, а отец и сам узел красные, вызывается метод rotating().
        В конце метод рекурсивно вызывается снова для балансировки (или проверки её необходимости) не более высоком уровне."""
        parents = self.search(self.root, self.search(self.root, node.value)[1].value)
        if parents[0] == self.root:
            return
        if parents[1].left == parents[0]:
            uncle = parents[1].right
        else:
            uncle = parents[1].left
        if node.is_red and parents[0].is_red and (uncle == None or not uncle.is_red):
            self.rotating(node, parents, uncle)
            self.balance_tree(node)
        elif uncle.is_red:
            parents[1].is_red = True
            parents[0].is_red = False
            uncle.is_red = False
            if parents[1] == self.root:
                parents[1].is_red = False
            else:
                self.balance_tree(parents[1])
        
    def rotating(self, node, parents, uncle):   
        """Данный метод осуществляет поворот части дерева.
        На вход принимает:
        node - класс Node, объект послуживший необходимости начать балансировку,
        parents - кортеж (отец дедушка), оба также являются экземплярами класса Node,
        uncle - класс Node, дядя.
        Исходя из взаимного расположения дяди и изначального объекта, производится поворот части дерева в ту или иную сторону тем или иным образом.
        Поскольку при повороте вершина данной части дерева изменяется, в конце вызывается метод change_grand()."""             
        if parents[1].left == uncle and parents[0].right == node:
            parents[1].right = parents[0].left
            parents[0].left = parents[1]
            parents[0].is_red, parents[1].is_red = False, True
            self.change_grand(parents[1], parents[0])
        elif parents[1].right == uncle and parents[0].left == node:            
            parents[1].left = parents[0].right
            parents[0].right = parents[1]
            parents[0].is_red, parents[1].is_red = False, True
            self.change_grand(parents[1], parents[0])
        elif parents[1].left == uncle and parents[0].left == node:
            node.left, node.right = parents[1], parents[0]
            parents[1].right, parents[0].left = None, None
            node.is_red, parents[1].is_red = False, True
            self.change_grand(parents[1], node)
        elif parents[1].right == uncle and parents[0].right == node:
            node.left, node.right = parents[0], parents[1]
            parents[0].right, parents[1].left = None, None
            node.is_red, parents[1].is_red = False, True
            self.change_grand(parents[1], node)        

    def change_grand(self, parent, node):
        """Метод изменяет ссылку родителя повёрнутой части дерева на новую, с новой вершиной.
        На вход принимает:
        parent - класс Node, объект, на который ссылается родитель повёрнутой части поддерева,
        node - класс Node, объект, на который должен ссылаться родитель повёрнутой части поддерева.
        Если parent является корнем дерева, то корнем становится node. Если же нет, производится поиск родителя объекта parent, и ссылка на него переписывается на node."""
        if parent == self.root:
            self.root = node
        else:
            grand = self.search(self.root, parent.value)
            if grand[1].left == parent:
                grand[1].left = node
            else: grand[1].right = node    

tree_1 = Tree()
tree_1.add_node(60)
tree_1.add_node(50)
tree_1.add_node(66)
tree_1.add_node(40)
tree_1.add_node(55)
tree_1.add_node(70)
tree_1.add_node(31)
tree_1.add_node(45)
tree_1.add_node(42)
tree_1.add_node(43)
tree_1.add_node(69)
tree_1.add_node(67)
tree_1.add_node(68)
tree_1.add_node(81)

# tree_1.add_node(1)
# tree_1.add_node(2)
# tree_1.add_node(3)
# tree_1.add_node(4)
# tree_1.add_node(5)
# tree_1.add_node(6)
# tree_1.add_node(7)
# tree_1.add_node(8)

tree_1.print_tree(tree_1.root)