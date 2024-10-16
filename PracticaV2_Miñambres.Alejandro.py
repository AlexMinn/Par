#ALEJANDRO MIÑAMBRES MATEOS
import wx
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#fichero,filas,lineas,fallo,instruccion,puntuacion
propie=['',12,0,False,0,0]
bloques=[]
lineasfichero=[]
simbol={'A':wx.Colour(88,214,141),'a':wx.Colour(88,214,141),'B':wx.Colour(93,173,226),'b':wx.Colour(93,173,226),'C':wx.Colour(215, 61, 23),'c':wx.Colour(215, 61, 23 ),'<':-1,'>':1} #diccionario de simbolos de colores
change={'A':'a','a':'A','B':'b','b':'B','C':'c','c':'C',' ':' ','x':'x'}      #diccionario de cambiar enla fusion
elichange={'A':'A','a':'A','B':'B','b':'B','C':'C','c':'C'}                   #diccionario de ver si eliminacion completa

class Prueba (object):
    def __init__(self,filas):
        del bloques[0:50]
        for x in range(0,filas):                                                
            lista=[]
            for y in range(10):
                lista.append(' ')
            lista.append('x')
            bloques.append(lista)

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0)  | wx.DEFAULT_FRAME_STYLE | wx.FRAME_SHAPED
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((615, 564))
        self.SetTitle("DESLIZATOR")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 5)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_5, 0, wx.ALL | wx.EXPAND, 5)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Abrir Fichero")
        sizer_4.Add(self.button_1, 0, wx.ALL | wx.EXPAND, 5)
        self.button_1.SetBackgroundColour(wx.Colour(215, 61, 23))

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "Nueva Partida")
        sizer_4.Add(self.button_2, 0, wx.ALL | wx.EXPAND, 5)

        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, "Cambiar filas")
        sizer_4.Add(self.button_3, 0, wx.ALL | wx.EXPAND, 5)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_7, 0, wx.ALL | wx.EXPAND, 5)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Jugada: ")
        sizer_7.Add(label_4, 0, 0, 0)

        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        sizer_7.Add(self.text_ctrl_2, 0, 0, 0)

        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "Lista de Jugadas")
        sizer_4.Add(label_5, 0, wx.ALL | wx.EXPAND, 5)

        self.list_box_1 = wx.ListBox(self.panel_1, wx.ID_ANY)
        sizer_4.Add(self.list_box_1, 1, wx.ALL | wx.EXPAND, 5)

        self.label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "Puntuación= 0", style=4)
        self.label_6.SetMinSize((159, 31))
        sizer_4.Add(self.label_6, 0, wx.ALL | wx.EXPAND | wx.SHAPED, 10)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.panel_2.SetBackgroundColour(wx.Colour(225, 225, 225))
        sizer_3.Add(self.panel_2, 1, wx.ALL|wx.EXPAND, 10)

        self.label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Introduzca jugada o ‐‐‐ o FIN:", style=wx.ALIGN_LEFT)
        sizer_2.Add(self.label_1, 0, wx.ALL | wx.EXPAND|wx.FIXED_MINSIZE, 5)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()

        self.dialog = MyDialog(None,wx.ID_ANY, "")
        self.perdido=Desli_lose(None,wx.ID_ANY, "")
        self.nwfilas=chan_filas(None,wx.ID_ANY, "")
        #////////////
        self.Bind(wx.EVT_BUTTON,self.onClick,self.button_2)
        self.Bind(wx.EVT_BUTTON,self.newfichero,self.button_1)
        self.Bind(wx.EVT_BUTTON,self.filaschange,self.button_3)
        self.Bind(wx.EVT_TEXT_ENTER,self.new_move,self.text_ctrl_2)
        self.panel_2.Bind(wx.EVT_SIZE,self.cambiotam)

        # end wxGlade
    
    def cambiotam(self,event):
        self.dibtab(wx.ClientDC(self.panel_2))
        return None

    def newfichero(self,event):
        Tk().withdraw()
        filename =askopenfilename() 
        propie[0]=filename
        try:
            f = open (propie[0],'r')
            otrablanc=0             
            maslineas=True
            while maslineas==True:                                               
                nuevalinea=[]
                nuevalinea=f.readline()
                lineasfichero.append(nuevalinea)
                if nuevalinea=='':
                    if otrablanc==1:
                        maslineas=False
                    otrablanc=otrablanc+1
            f.close()
            self.button_1.SetBackgroundColour(wx.Colour(22, 213, 38))
            self.partida()
        except(Exception):
            self.button_1.SetBackgroundColour(wx.Colour(215, 61, 23))
            self.dialog.Show()
        return None

    def onClick(self, event): 
        self.partida()
        return None

    def filaschange(self, event):
        self.nwfilas.Show()
        self.partida()

    def partida(self):
        propie[5]=0
        fila=propie[1]
        propie[2]=0
        propie[3]=False
        propie[4]=0
        Prueba(propie[1])
        if propie[0]!='':
            self.movi()
        else:
            self.dialog.Show()
        return None

    def movi(self):
        linea=propie[2]
        fallo =propie[3]
        puntuacion=propie[5]
        if fallo==False:
            self.bajada()

            elimina=True
            while elimina==True:
                elimi=self.eliminacion(puntuacion)
                elimina=elimi[0]
                puntuacion=puntuacion+elimi[1]
            
            self.bajada()
            elimi=self.eliminacion(puntuacion)
            puntuacion=puntuacion+elimi[1]
            self.bajada()

            propie[5]=puntuacion
            for n in range(10):                                                 #SI SE RELLENA LA PRIMERA FILA PIERDES
                if bloques[0][n]!=' ':
                    fallo=True

        if fallo==True:
            self.perdido.Show()
            self.partida()
        else:
            #separa la linea nueva y la coloca en la matriz
            for x in range(0,10):
                bloques[0][x]=lineasfichero[linea][x]
            #imprime
            self.dibtab(wx.ClientDC(self.panel_2))
        
            propie[2]=propie[2]+1
            if lineasfichero[propie[2]]=='':
                propie[2]=0
        return None

    def dibtab (self, dc):
        posic=self.panel_2.GetSize()
        m=posic[0]/340
        n=(posic[1]/400)
        self.label_6.SetLabel('Puntuación: '+ str(propie[5]) )
        dc.Clear()
        dc.Pen=wx.Pen(wx.Colour(234,237,237))
        last=0
        #letras
        for num in range(propie[1]):       
            dc.DrawText(chr(num+65),int(10*m),int((15+num*30)*n))
            last=(5+num*30)
            dc.DrawLine(int(15*m),int((last+30)*n),int(340*m),int((last+30)*n))
        #numeros
        for num in range(10):
            dc.DrawText(chr(48+num),int((40+num*30)*m),int((last+40)*n))
            dc.DrawLine(int((30+num*30)*m),int(10*n),int((30+num*30)*m),int((last+45)*n))
        #bloques
        dc.Pen=wx.Pen(wx.Colour(0,0,0))
        for y in range(propie[1]):
            x=0
            while x<10:
                if bloques[y][x]!=' ':
                    dc.Brush=wx.Brush(simbol[bloques[y][x]])
                    if bloques[y][x]==bloques[y][x+1]:
                        if bloques[y][x+1]==bloques[y][x+2]:
                            if bloques[y][x+2]==bloques[y][x+3]:
                                dc.DrawRoundedRectangle(int((30*(x+1))*m),int((5+30*y)*n),int(120*m),int(30*n),5)
                                x=x+4
                            else:
                                dc.DrawRoundedRectangle(int((30*(x+1))*m),int((5+30*y)*n),int(90*m),int(30*n),5)
                                x=x+3
                        else:
                            dc.DrawRoundedRectangle(int((30*(x+1))*m),int((5+30*y)*n),int(60*m),int(30*n),5)
                            x=x+2
                    else:
                        dc.DrawRoundedRectangle(int((30*(x+1))*m),int((5+30*y)*n),int(30*m),int(30*n),5)
                        x=x+1
                else:
                    x=x+1
        
        return None

    def bajada(self):                                            #bajada de los bloques
        lis1=[]
        ind=propie[1]-2
        while ind>=0:
            lis1.append(ind)
            ind=ind-1
        #lis1=[10,9,8,7,6,5,4,3,2,1,0]
        for y in lis1:                                                            #recorre la matriz de abajo a arriba
            j=y
            pabajo=True
            while pabajo==True:                                                     #recorre la matriz desde arriba a abajo para llevar lomas bajo posible     
                conti=True
                x=0
                vacio=True
                while conti==True:
                    if bloques[j][x]!=' ':
                        if bloques[j][x]!=bloques[j][x+1]:            #bloque de 1
                            if bloques[j+1][x]==' ':
                                bloques[j+1][x]=bloques[j][x]
                                bloques[j][x]=' '
                                self.fusion(x,x,j+1)
                                vacio=False
                            x=x+1
                        elif bloques[j][x+1]!=bloques[j][x+2]:        #bloque de 2
                            if bloques[j+1][x]==' ' and bloques[j+1][x+1]==' ':
                                bloques[j+1][x]=bloques[j][x]
                                bloques[j+1][x+1]=bloques[j][x+1]
                                bloques[j][x]=' '
                                bloques[j][x+1]=' '
                                self.fusion(x,x+1,j+1)
                                vacio=False
                            x=x+2
                        elif bloques[j][x+2]!=bloques[j][x+3]:              #bloque de 3
                            if bloques[j+1][x]==' ' and bloques[j+1][x+1]==' ' and bloques[j+1][x+2]==' ':
                                bloques[j+1][x]=bloques[j][x]
                                bloques[j+1][x+1]=bloques[j][x+1]
                                bloques[j+1][x+2]=bloques[j][x+2]
                                bloques[j][x]=' '
                                bloques[j][x+1]=' '
                                bloques[j][x+2]=' '
                                self.fusion(x,x+2,j+1)
                                vacio=False
                            x=x+3
                        elif bloques[j][x+3]!=bloques[j][x+4]:                  #bloque de 4
                            if bloques[j+1][x]==' ' and bloques[j+1][x+1]==' ' \
                            and bloques[j+1][x+2]==' ' and bloques[j+1][x+3]==' ':
                                bloques[j+1][x]=bloques[j][x]
                                bloques[j+1][x+1]=bloques[j][x+1]
                                bloques[j+1][x+2]=bloques[j][x+2]
                                bloques[j+1][x+3]=bloques[j][x+3]
                                bloques[j][x]=' '
                                bloques[j][x+1]=' '
                                bloques[j][x+2]=' '
                                bloques[j][x+3]=' '
                                self.fusion(x,x+3,j+1)
                                vacio=False
                            x=x+4
                        else:
                            x=x+1
                    else: 
                        x=x+1
                    if x==10:
                            conti=False   
                j=j+1
                if vacio==False:
                    self.dibtab(wx.ClientDC(self.panel_2))
                    time.sleep(0.1)
                if j==propie[1]-1:
                    pabajo=False
        return None

    def fusion(self,izq,der,col):                                #si ocurre fusion intercambian mayusculas y minusculas
        if (izq!=100):
            if bloques[col][izq]==' ':
                return None
            if(bloques[col][izq]==bloques[col][izq-1]):
                acabo=False
                p=izq-1
                while acabo==False:
                    bloques[col][p]=change[bloques[col][p]]
                    p=p-1
                    if p<0:
                        acabo=True
        if (der!=100):
            if (bloques[col][der]==bloques[col][der+1]):
                acabo=False
                p=der+1
                while acabo==False:
                    bloques[col][p]=change[bloques[col][p]]
                    p=p+1
                    if p>10:
                        acabo=True      
        return None

    def eliminacion(self,puntuacion):                            #eliminación de las filas llenas
        complete=True
        col=propie[1]-1
        puntu=0
        while col>-1:
            fil=0
            elimi=True
            while fil<10:                                           #SI UNA LINEA TIENE ' ' NO LA ELIMINA
                if(bloques[col][fil]==' '):
                    elimi=False
                fil=fil+1
            if(elimi==True):
                for v in range(9):                                  #SI CADA PARAMETRO DE UNA LINEA ES IGUAL 
                    if(elichange[bloques[col][v]]!=elichange[bloques[col][v+1]]):
                        complete=False
                if complete==True:                                  #SI CUMPLE ANTERIOR, ELIMINACION COMPLETA
                    for x in range(propie[1]):
                        for y in range(10):
                            if bloques[x][y]!=' ':
                                bloques[x][y]=' '
                                puntu=puntu+1
                else:                                               #SI NO CUMPLE SOLO ELIMINA UNA LINEA
                    for x in range(10):
                        bloques[col][x]=' '
                        puntu=puntu+1
                col=propie[1]
            col=col-1
        return elimi,puntu

    def qinstru (self):                                        #si las instrucciones son correctas
        ins=propie[4]
        repit=False
        coords=[-1,-1,-1]
        try:
            coords[2]=ins[2]
            coords[0]=ord(ins[0])-65
            coords[1]=ord(ins[1])-48
        except Exception :
            self.label_1.SetLabel("Faltan instrucciones")
            repit=True
        if (coords[0]<0 or coords[0]>11) and repit==False:
            self.label_1.SetLabel("Error de sintaxis en jugada")
            repit=True
        elif (coords[1]<0 or coords[1]>9):
            self.label_1.SetLabel("Error de sintaxis en jugada")
            repit=True
        elif (coords[2]=='<' or coords[2]=='>' ):
            if (bloques[coords[0]][coords[1]]==' '):
                self.label_1.SetLabel("No hay ningún bloque en esa celda")
                repit=True
            else:
                a=simbol[coords[2]]
                if bloques[coords[0]][coords[1]+a]==' ':            #bloque de 1
                    self.movimiento(coords)
                elif bloques[coords[0]][coords[1]+a]==bloques[coords[0]][coords[1]]:
                    if bloques[coords[0]][coords[1]+a*2]==' ':      #bloque de 2
                        coords[1]=coords[1]+a 
                        self.movimiento(coords)
                    elif bloques[coords[0]][coords[1]+a*2]==bloques[coords[0]][coords[1]]:
                        if bloques[coords[0]][coords[1]+a*3]==' ':              #bloque de 3
                            coords[1]=coords[1]+a*2
                            self.movimiento(coords)
                        elif bloques[coords[0]][coords[1]+a*3]==bloques[coords[0]][coords[1]]:
                            if bloques[coords[0]][coords[1]+a*4]==' ':              #bloque de 4
                                coords[1]=coords[1]+a*3
                                self.movimiento(coords)
                            else:
                                self.label_1.SetLabel("El bloque no puede moverse en esa dirección")
                                repit=True 
                        else:
                            self.label_1.SetLabel("El bloque no puede moverse en esa dirección")
                            repit=True 
                    else:
                        self.label_1.SetLabel("El bloque no puede moverse en esa dirección")
                        repit=True   
                else:      
                    self.label_1.SetLabel("El bloque no puede moverse en esa dirección")
                    repit=True
        else:
            self.label_1.SetLabel("Error de sintaxis en jugada")
            repit=True
        return repit

    def movimiento(self,coords):                                 #el movimiento de esas instrucciones
        nomasb=False
        a=simbol[coords[2]]
        i=2*a
        while nomasb==False:
            if bloques[coords[0]][coords[1]+i]!=' ':
                i=i-(1*a)
                nomasb=True
                bloques[coords[0]][coords[1]+i]=bloques[coords[0]][coords[1]]   #bloque 1
                bloques[coords[0]][coords[1]]=' '
                if bloques[coords[0]][coords[1]-(1*a)]==bloques[coords[0]][coords[1]+i]:    #bloque 2
                    bloques[coords[0]][coords[1]+i-(1*a)]=bloques[coords[0]][coords[1]+i]
                    bloques[coords[0]][coords[1]-1*a]=' '
                    if bloques[coords[0]][coords[1]-2*a]==bloques[coords[0]][coords[1]+i]:      #bloque 3
                        bloques[coords[0]][coords[1]+i-(2*a)]=bloques[coords[0]][coords[1]+i]
                        bloques[coords[0]][coords[1]-2*a]=' '
                        if bloques[coords[0]][coords[1]-3*a]==bloques[coords[0]][coords[1]+i]:      #bloque 4
                            bloques[coords[0]][coords[1]+i-(3*a)]=bloques[coords[0]][coords[1]+i]
                            bloques[coords[0]][coords[1]-3*a]=' '
                if(a==1):
                    self.fusion(100,coords[1]+i,coords[0])
                elif(a==-1):
                    self.fusion(coords[1]+i,100,coords[0])
                self.dibtab(wx.ClientDC(self.panel_2))
                time.sleep(0.1)
            i=i+(1*a)
        return None

    def new_move(self, event):
        propie[4]=self.text_ctrl_2.GetLineText(0)
        instruccion=propie[4]
        self.text_ctrl_2.SetValue('')
        self.list_box_1.Append(propie[4])

        repit=True
        self.label_1.SetLabel("Introduzca jugada o ‐‐‐ o FIN:")
        if instruccion=='FIN':
            repit=False
            propie[3]=True
        elif instruccion=='---':
            repit=False
        else:
            repit=self.qinstru()

        if repit==False:
            self.movi()
        return None

class MyDialog(wx.Dialog, MyFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("ERROR")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "NO SE PUDO ABRIR EL FICHERO")
        sizer_3.Add(label_1, 0, 0, 0)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_3.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())

        self.Layout()
        self.Centre()
        # end wxGlade

class Desli_lose(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Desli_lose.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("DESLIZATOR")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        self.label_1 = wx.StaticText(self, wx.ID_ANY, "HAS PERDIDO", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.label_1.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Times New Roman"))
        sizer_3.Add(self.label_1, 0, wx.ALL | wx.EXPAND, 10)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self, wx.ID_ANY, u"Puntuación:", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_2.SetFont(wx.Font(15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_2, 1, wx.ALL | wx.EXPAND, 10)

        self.pun_err = wx.StaticText(self, wx.ID_ANY, '0', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.pun_err.SetFont(wx.Font(25, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 1, ""))
        sizer_4.Add(self.pun_err, 1, wx.EXPAND, 10)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_INIT_DIALOG,self.puntu)
        # end wxGlade

    def puntu(self, event):
        self.pun_err.SetLabel(str(propie[5]))

class chan_filas(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: chan_filas.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((250, 200))
        self.SetTitle("DESLIZAZTOR")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "  Indique cuantas     filas quiere")
        label_1.SetFont(wx.Font(15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, 0, ""))
        sizer_3.Add(label_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "12", min=5, max=27)
        self.spin_ctrl_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_3.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.SHAPED, 10)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        sizer_2.Realize()

        self.SetSizer(sizer_1)

        self.Layout()
        self.Centre()

        # end wxGlade
        self.Bind(wx.EVT_SPINCTRL, self.spin,self.spin_ctrl_1)

    def spin(self, event):
        propie[1]=self.spin_ctrl_1.GetValue()
        return None

class Main(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class Main

if __name__ == "__main__":
    Desliza = Main(0)
    Desliza.MainLoop()
