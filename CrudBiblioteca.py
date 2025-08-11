class Livro:
    def __init__(self, id, titulo, autor, ano, categoria, status="Disponivel"):
        self._id=id
        self._titulo=titulo
        self._autor=autor
        self._ano=ano
        self._categoria=categoria
        self._status=status

    def __str__(self):
        return f"{self._id} - {self._titulo} - {self._autor} - {self._ano} - {self._categoria} - {self._status}"

class Biblioteca:
    def __init__(self):
        self.livros=[]
        self.proximo_id=1

    def criarLivro(self, titulo, autor, ano, categoria):
        livro=Livro(self.proximo_id,titulo, autor, ano, categoria)

        self.livros.append(livro)
        self.proximo_id+=1
        print("Livro Adicionando com sucesso")

    def listarLivros(self):
        if not self.livros:
            print("Nenhum Livro Cadastrado")
        else:
            for livro in self.livros:
                print(livro)

    def actualizarLivro(self, id, novo_titulo=None, novo_autor=None, nova_categoria=None, novo_status=None):
        for livro in self.livros:
            if livro._id==id:
                if novo_titulo:
                    livro.titulo=novotitulo
                if novo_autor:
                    livro.autor=novoautor
                if nova_categoria:
                    livro.categoria=novacategoria
                if novos_tatus:
                    livro.status=novostatus
                print("Livro Actualizado com sucesso")
                return
                print("Livro nao Encontrado")

    def DeletarLivro(self, id):
        for livro in self.livros:
            if livro._id==id:
                self.livros.remove(livro)
                print(f"Livro {livro._titulo} removido com sucesso")
                return
                print("Livro nao Encontrado.")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("Bem vindo ao Sistema da Biblioteca")

        print("1-Adicioanar Livros")
        print("2-Listar Livros")
        print("3-Actualizar Livros")
        print("4-Remover Livro")
        print("5-Sair")

        opcao=input("Escolha uma Opcao: ")

        if opcao == "1":
            titulo=input("Titulo: ")
            autor=input("Autor: ")
            ano=input("Ano: ")
            categoria=input("Categoria: ")
            biblioteca.criarLivro(titulo, autor, ano, categoria)
        elif opcao == "2":
            biblioteca.listarLivros()
        elif opcao == "3":
            id_livro=int(input("ID do livro a Actualizar:"))
            titulo=input("ID do livro a Actualizar:")
            autor=input("ID do livro a Actualizar:")
            ano=input("ID do livro a Actualizar:")
            novacategoria=input("Nova Categoriar: ") or None
            status=input("Novo Status: ") or None
            biblioteca.actualizarLivro(id_livro,titulo,autor, ano, categoria, status)

        elif opcao == "4":
            id_livro=int(input("ID do Livro a Remover: "))
            biblioteca.DeletarLivro(id_livro)
        elif opcao == "5":
            print("Saindo do Sistema....")
            break
        else:
            print("Opcao invalida, Tente novamente")
menu()  