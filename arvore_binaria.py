class BinaryTree:
    def __init__(self, key=None):
        self.leftchild = None
        self.rightchild = None
        self.key = key

    def add(self, value):
        # Se a árvore estiver vazia, insere o valor como raiz
        if self.key is None:
            self.key = value
            return
        
        # Se o valor já existir na árvore, não faz nada (evita duplicatas)
        if self.key == value:
            return
        
        # Se o valor for menor, adiciona à subárvore esquerda
        if value < self.key:
            if self.leftchild:
                self.leftchild.add(value)
            else:
                self.leftchild = BinaryTree(value)
        # Se o valor for maior, adiciona à subárvore direita
        else:
            if self.rightchild:
                self.rightchild.add(value)
            else:
                self.rightchild = BinaryTree(value)

    def search(self, value):
        # Verifica se o valor está presente no nó atual
        if self.key == value:
            print(f"O nó com valor {value} está presente na árvore.")
            return True

        # Se o valor for menor, busca na subárvore esquerda
        if value < self.key:
            if self.leftchild:
                return self.leftchild.search(value)
            else:
                print(f"O nó com valor {value} não está presente na árvore.")
                return False

        # Se o valor for maior, busca na subárvore direita
        if value > self.key:
            if self.rightchild:
                return self.rightchild.search(value)
            else:
                print(f"O nó com valor {value} não está presente na árvore.")
                return False

    def check(self, value):
        # Verifica se a árvore está vazia
        if self.key is None:
            print("A árvore está vazia.")
            return False
        print("A árvore não está vazia.")
        return True

    def delete(self):
        # Função para deletar a árvore
        print("Deletando a árvore...")
        self.key = None
        self.leftchild = None
        self.rightchild = None
        print("Árvore deletada.")

# Exemplo de uso
if __name__ == "__main__":
    root = BinaryTree(50)  # 50 é a chave da raiz
    elements = [20, 56, 3, 4, 7, 10, 17, 20]  # Lista de elementos a serem inseridos

    for i in elements:
        root.add(i)  # Adiciona elementos na árvore

    # Busca por um valor específico
    root.search(10)
    root.search(100)

    # Verifica se a árvore está vazia
    root.check(50)

    # Deleta a árvore
    root.delete()

    # Verifica novamente após deletar
    root.check(50)

