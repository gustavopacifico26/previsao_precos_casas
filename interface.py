import tkinter as ttk
from tkinter import *
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def regressao_multipla(root,rend,idade,comodos,quartos,pop,med,lat,lon):

    california_data = fetch_california_housing()
    X = california_data.data
    y = california_data.target

    df = pd.DataFrame(X, columns=california_data.feature_names)
    df['Preço'] = y 

    df.rename(columns={'MedInc': 'mediana_renda', 
                   'HouseAge': 'idade_casa', 
                   'AveRooms': 'media_comodo', 
                   'AveBedrms': 'media_quartos_dormir',
                   'Population': 'pessoas_bairro',
                   'AveOccup': 'media_pessoas_habitação'}, inplace=True)

    df =df.loc[(df['media_comodo'] < 30) & (df['media_quartos_dormir'] <14) & (df['pessoas_bairro'] <= 8000) & (df['media_pessoas_habitação']< 10)]

    X = df.drop('Preço', axis=1)
    y = df['Preço']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)

    model = RandomForestRegressor(n_estimators=100, max_depth=20, min_samples_leaf=2, min_samples_split=2, random_state=42)

    model.fit(X_train, y_train)

    rend = rend/10000

    new_example = [[rend,idade,comodos,quartos,pop,med,lat,lon]]
    price_pred = float(model.predict(new_example))

    texto = ("Preço previsto: $ {:.2f}".format(round(price_pred*100000, 2)))

    mensagem = Label(root, text = texto, font=('Bebas Neue',25),padx=25,pady=10,fg='green')
    mensagem.place(x=220,y=80)

def previsao():
    
    root1=Tk()
    root1.geometry('900x800')
    root1.title('Prever preço de casa')
    
    legenda1 = Label(root1, text= "Coloque as informações sobre o bairro", font=('Bebas Neue',16),padx=25,pady=10)
    legenda1.place(x=240,y=200)

    legenda2=Label(root1,text='Renda Média:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda2.place(x=140,y=300)
    e1=Entry(root1,width=50)
    e1.place(x=80,y=350)

    legenda3=Label(root1,text='Média da Idade das Casas:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda3.place(x=95,y=400)
    e2 = Entry(root1,width=50)
    e2.place(x=80,y=450)

    legenda3=Label(root1,text='Média de Cômodos:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda3.place(x=120,y=500)
    e3 = Entry(root1,width=50)
    e3.place(x=80,y=550)

    legenda4=Label(root1,text='Média de Quartos:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda4.place(x=125,y=600)
    e4 = Entry(root1,width=50)
    e4.place(x=80,y=650)

    legenda5=Label(root1,text='População:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda5.place(x=575,y=300)
    e5 = Entry(root1,width=50)
    e5.place(x=500,y=350)

    legenda6=Label(root1,text='Média de Pessoas por Habitação:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda6.place(x=485,y=400)
    e6 = Entry(root1,width=50)
    e6.place(x=500,y=450)

    legenda7=Label(root1,text='Latitude:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda7.place(x=595,y=500)
    e7 = Entry(root1,width=50)
    e7.place(x=500,y=550)

    legenda7=Label(root1,text='Longitude:',font=('Bebas Neue',14),padx=25,pady=10)
    legenda7.place(x=590,y=600)
    e8 = Entry(root1,width=50)
    e8.place(x=500,y=650)

    cad = lambda  : regressao_multipla(root1,float(e1.get()),float(e2.get()),float(e3.get()),float(e4.get()),float(e5.get()),float(e6.get()),float(e7.get()),float(e8.get()))

    botao2=ttk.Button(root1, text='Fazer Previsão', command=cad)
    botao2.configure(bg='white')
    botao2.place(x=330,y=720,width=200,height=40)

    root1.mainloop()


def menuPrincipal():
    
    root = Tk()
    root.geometry('500x700')
    root.title('Previsor de preços de casas')

    legenda = Label(root, text= "Prever preço de casa", font=('Bebas Neue',14),padx=25,pady=10)
    legenda.place(x=140,y=100)

    imagem=PhotoImage(file='casa.png')
    imagem = imagem.subsample(2)
    figura1=Label(root, image=imagem)
    figura1.place(x=140,y=160)

    botao1 = ttk.Button(root, text='Fazer Previsão', command=previsao)
    botao1.configure(bg='white')
    botao1.place(x=130,y=420,width=250,height=50)

    botaoFechar=ttk.Button(root, text='Desligar Sistema',command=root.destroy)
    botaoFechar.configure(bg='white')
    botaoFechar.place(x=130,y=500,width=250,height=50)

    root.mainloop()

menuPrincipal()


