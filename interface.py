from tkinter import *
from tkinter import scrolledtext
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do Grafo")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.numeroLabel = Label(self.segundoContainer,text="numero de vertices", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)

        self.nvertice = Entry(self.segundoContainer)
        self.nvertice["width"] = 5
        self.nvertice["font"] = self.fontePadrao
        self.nvertice.pack(side=LEFT)
        self.nvertice.insert(0,15)

        self.arestasLabel=Label(self.segundoContainer,text="arestas")
        self.arestasLabel.pack(side=LEFT)
        self.aresta=scrolledtext.ScrolledText(self.segundoContainer,height=5,width=3,wrap=WORD,)
        self.aresta.pack(side=LEFT)
        self.aresta.insert('1.0',"1,2\n2,3")

        # self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        # self.senhaLabel.pack(side=LEFT)

        # self.senha = Entry(self.terceiroContainer)
        # self.senha["width"] = 30
        # self.senha["font"] = self.fontePadrao
        # self.senha["show"] = "*"
        # self.senha.pack(side=LEFT)

        self.autenticar = Button(self.terceiroContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
root.title("Busca Bidirecional")
Application(root)
root.mainloop()