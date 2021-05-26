from tkinter import *
from tkinter import scrolledtext
from BidirecionalSearch import BidirectionalSearch
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
        self.aresta=scrolledtext.ScrolledText(self.segundoContainer,height=3,width=7,wrap=WORD,)
        self.aresta.pack(side=LEFT)
        self.aresta.insert('1.0',"0,4\n1,4\n2,5\n3,5\n4,6\n5,6\n6,7\n7,8\n8,9\n8,10\n9,11\n9,12\n10,13\n10,14")

        self.scrLabel=Label(self.terceiroContainer,text="vertice de inicio")
        self.scrLabel.pack(side=LEFT)
        self.scr=Entry(self.terceiroContainer,width=5,font=self.fontePadrao)
        self.scr.pack(side=LEFT)
        self.scr.insert(0,0)
        self.destLabel=Label(self.terceiroContainer,text="vertice de destino")
        self.destLabel.pack(side=LEFT)
        self.dest=Entry(self.terceiroContainer,width=5,font=self.fontePadrao)
        self.dest.pack(side=LEFT)
        self.dest.insert(0,14)
        # self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        # self.senhaLabel.pack(side=LEFT)

        # self.senha = Entry(self.terceiroContainer)
        # self.senha["width"] = 30
        # self.senha["font"] = self.fontePadrao
        # self.senha["show"] = "*"
        # self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Buscar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.Buscar
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
    def Buscar(self):
        n=int(self.nvertice.get())
        self.grafo_busca=BidirectionalSearch(n)
        arestas=self.aresta.get("1.0",END)[:-1]
        scr=int(self.scr.get())
        dest=int(self.dest.get())
        for arest in arestas.split('\n'):
            arest.split(',')
            self.grafo_busca.add_edge(int(arest.split(',')[0]), int(arest.split(',')[1]))
        path,intersecting_node =self.grafo_busca.bidirectional_search(scr, dest)
        if(path==-1):
            path="não existe caminho entre os vertices {} e {}".format(str(scr),str(dest))
        self.mensagem["text"]=str(path)
        
        

root = Tk()
root.title("Busca Bidirecional")
root.resizable(width=False, height=False)
Application(root)
root.mainloop()