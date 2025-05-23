class Livro:
    titulo = ''
    autor = ''
    ano = 0
    disponivel = False

    def exibir_info(self):
        print(f'informações:\n\nTITULO - {self.titulo}\nAUTOR - {self.autor}\nANO - {self.ano}')
        if self.disponivel:
            print("Livro disponivel\n")
        else:
            print('Livro emprestado\n')

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print('Livro emprestado com sucesso!\n')
        else:
            print('Livro não está disponível.\n')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print('Livro devolvido com sucesso!\n')
        else:
            print('O livro já esta disponível')


livro1 = Livro()
livro1.autor = 'Machado de Assis'
livro1.titulo = 'Domcasmurro'
livro1.ano = 1979

livro1.exibir_info()
livro1.emprestar()
livro1.exibir_info()
livro1.devolver()
livro1.exibir_info()
livro1.emprestar()
