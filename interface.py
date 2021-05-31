from tkinter import *
from tkinter import scrolledtext
from BidirecionalSearch import BidirectionalSearch
import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.InstrucoesContainer = Frame(master)
        self.InstrucoesContainer["pady"] = 10
        self.InstrucoesContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.TextoContainer = Frame(master)
        self.TextoContainer["padx"] = 20
        self.TextoContainer.pack()
        
        self.exemplosContainer = Frame(master)
        self.exemplosContainer["padx"] = 20
        self.exemplosContainer.pack()


        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Busca Bidirecional")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.instrucoes = Label(self.InstrucoesContainer, text="""Instruções
        1º-preencha o numero de vertices desejado. Os vertices são representado pelos numeros do intervalo 0 a o numero de vertices -1.
        2º-No campo arestas preencha com os vertices de cada aresta da seguinte forma numero do vertice,numero do vertice.Cada linha representa uma aresta, entao ao terminar uma aresta precione enter.
        3º-Preencha o vertice de inicio e destino, lembrando que os vertices tem que estar detro do intervalo de 0 a numero de vertice -1
        4º-Para inserir as entradas dos exemplo é só clicar no botão referente ao exemplo.
        5º- para fazer a busca click no botão Buscar e uma imagem do grafo será exibida abaixo do botão.
        
        Os vertices em vermelho representam o passeio/percuso pecorrido pelas buscas e a interseção entre as buscas esta representado pela cor azul.
        Caso a imagem dé a impressão de estar errada ou não esteja dando para ver direito click em Buscar novamente.""")
        self.instrucoes["font"] = ("Arial", "10", "bold")
        self.instrucoes.pack()


        self.numeroLabel = Label(self.segundoContainer,text="numero de vertices", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)

        self.nvertice = Entry(self.segundoContainer)
        self.nvertice["width"] = 5
        self.nvertice["font"] = self.fontePadrao
        self.nvertice.pack(side=LEFT)
        self.nvertice.insert(0,15)

        self.arestasLabel=Label(self.segundoContainer,text="Arestas")
        self.arestasLabel.pack(side=LEFT)
        self.aresta=scrolledtext.ScrolledText(self.segundoContainer,height=3,width=7,wrap=WORD,)
        self.aresta.pack(side=LEFT)
        self.aresta.insert('1.0',"0,4\n1,4\n2,5\n3,5\n4,6\n5,6\n6,7\n7,8\n8,9\n8,10\n9,11\n9,12\n10,13\n10,14\n")

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
        

        self.buscar = Button(self.quartoContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.Buscar
        self.buscar.pack()

        self.exemplo1 = Button(self.exemplosContainer)
        self.exemplo1["text"] = "Exemplo 1"
        self.exemplo1["font"] = ("Calibri", "8")
        self.exemplo1["width"] = 12
        self.exemplo1["command"] = self.exemplo_1
        self.exemplo1.pack(side=LEFT)

        self.exemplo2 = Button(self.exemplosContainer)
        self.exemplo2["text"] = "Exemplo 2"
        self.exemplo2["font"] = ("Calibri", "8")
        self.exemplo2["width"] = 12
        self.exemplo2["command"] = self.exemplo_2
        self.exemplo2.pack(side=LEFT)

        self.exemplo3 = Button(self.exemplosContainer)
        self.exemplo3["text"] = "Exemplo 3"
        self.exemplo3["font"] = ("Calibri", "8")
        self.exemplo3["width"] = 12
        self.exemplo3["command"] = self.exemplo_3
        self.exemplo3.pack(side=LEFT)

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
    def verificar_entrada(self,vertices,arestas,inicio,destino):
        if not(vertices.isdigit()):
            self.mensagem.configure(image='')
            self.mensagem["text"]="O numero de vértices deve ser um número"
            return False
        elif not inicio.isdigit():
            self.mensagem.configure(image='')
            self.mensagem["text"]="O vertice de inicio não é um número"
            return False
        elif not destino.isdigit():
            self.mensagem.configure(image='')
            self.mensagem["text"]="O vertice de destino não é um número"
            return False
        elif int(inicio) > int(vertices)-1:
            self.mensagem.configure(image='')
            self.mensagem["text"]="O vertice de inicio esta fora do intervalo de 0 a {} ".format(int(vertices)-1)
            return False
        elif int(destino)> int(vertices)-1:
            self.mensagem.configure(image='')
            self.mensagem["text"]="O vertice de destino esta fora do intervalo de 0 a {} ".format(int(vertices)-1)
            return False
        elif arestas.split("\n")[-1] !='':
            self.mensagem.configure(image='')
            self.mensagem["text"]="falta apertar enter na ultima linha do campo das arestas"
            return False
        
        for i,arest in enumerate(arestas.split("\n")[:-1]):
            if not(arest.split(",")[0].isdigit() and arest.split(",")[1].isdigit()) and len(arestas)>=1:
                self.mensagem.configure(image='')
                self.mensagem["text"]="Existe um vertice que não é número no par de vertices na linha {}".format(i+1)
                return False
            elif (int(arest.split(",")[0]) > int(vertices)-1) or (int(arest.split(",")[1]) > int(vertices)-1):
                self.mensagem.configure(image='')
                self.mensagem["text"]="Existe um vertice que esta fora do intervalo de 0 a {} na linha {}".format(int(vertices)-1,i+1)
                return False    
        
        return True

    def exemplo_1(self):
        self.nvertice.delete(0,END)
        self.nvertice.insert(0,15)
        self.aresta.delete('1.0',END)
        self.aresta.insert('1.0',"0,4\n1,4\n2,5\n3,5\n4,6\n5,6\n6,7\n7,8\n8,9\n8,10\n9,11\n9,12\n10,13\n10,14\n")
        self.scr.delete(0,END)
        self.scr.insert(0,0)
        self.dest.delete(0,END)
        self.dest.insert(0,14)
    def exemplo_2(self):
        self.nvertice.delete(0,END)
        self.nvertice.insert(0,2)
        self.aresta.delete('1.0',END)
        self.aresta.insert('1.0',"0,1\n")
        self.scr.delete(0,END)
        self.scr.insert(0,0)
        self.dest.delete(0,END)
        self.dest.insert(0,1)
    def exemplo_3(self):
        self.nvertice.delete(0,END)
        self.nvertice.insert(0,15)
        self.aresta.delete('1.0',END)
        self.aresta.insert('1.0',"0,4\n1,4\n2,5\n3,5\n4,6\n5,6\n6,7\n7,8\n8,9\n8,10\n")
        self.scr.delete(0,END)
        self.scr.insert(0,0)
        self.dest.delete(0,END)
        self.dest.insert(0,10)
    

    def Buscar(self):
        if self.verificar_entrada(self.nvertice.get(),self.aresta.get("1.0",END)[:-1],self.scr.get(),self.dest.get()):
            n=int(self.nvertice.get())
            grafo_busca=BidirectionalSearch(n)
            arestas=self.aresta.get("1.0",END)[:-1]
            scr=int(self.scr.get())
            dest=int(self.dest.get())
            G = nx.Graph()
            for i in range(n):
                G.add_node(i)
            for arest in arestas.split('\n')[:-1]:
                a=int(arest.split(',')[0])
                b=int(arest.split(',')[1])
                G.add_edge(a, b)
                grafo_busca.add_edge(a, b)
            path,intersecting_node =grafo_busca.bidirectional_search(scr, dest)
            if(path==-1):
                path="não existe caminho entre os vertices {} e {}".format(str(scr),str(dest))
                self.mensagem.configure(image='')
                self.mensagem["text"]=str(path)
            else:
                val_map ={}
                values = []

                colorirvermelho=path[:path.index(str(intersecting_node))].split(' ')
                colorirvermelho.pop(colorirvermelho.index(''))
                colorirVerde=path[path.index(str(intersecting_node))+1:].split(' ')
                colorirVerde.pop(colorirVerde.index(''))
                for i in range(len(colorirvermelho)):
                    val_map[int(colorirvermelho[i])]=0.5714285714285714
                for i in range(len(colorirVerde)):
                    val_map[int(colorirVerde[i])]=0.5714285714285714
                val_map[int(intersecting_node)]=0.25
                values = [val_map.get(node,0.5) for node in G.nodes()]
                nx.draw(G, with_labels=True, cmap=plt.get_cmap('jet'), node_color=values,edge_color="skyblue", style="solid")
                plt.savefig('imd.png')
                plt.close()
                ima=PhotoImage(file='imd.png')
                self.mensagem.configure(image=ima)
                self.mensagem.imagem=ima
        
            
            
            

    
        
        

root = Tk()
root.title("Busca Bidirecional")
root.resizable(width=False, height=False)
Application(root)
root.mainloop()
