import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from altair.vegalite.v3.theme import theme

st.set_page_config(page_title='FEVEREIRO 2023')
st.title(':red[RESOLVE FEVEREIRO]')

#leitura do excel, transformar em data frame
file = pd.read_excel('jogo.xlsx')
filepontos = pd.read_excel('jogo.xlsx', sheet_name='tabelapontos')

img0 = Image.open('henrique.bmp') #Com muita calma
img1 = Image.open('domingos.jpg') #Baui
img2 = Image.open('img2.png')
img3 = Image.open('img3.png')
img4 = Image.open('img4.png')
img5 = Image.open('img5.png')
img6 = Image.open('img6.png')
img7 = Image.open('img7.png')

df = pd.DataFrame(file)
dfp = pd.DataFrame(filepontos)
dfp = dfp.convert_dtypes(convert_string=True)
#inverter eixos
totalinv = df.T
#somar pontos de todas as categorias
for i in range(0, 8):
    totalinv[i][1] = totalinv[i][2:17].sum()




dfp

total = totalinv.loc[["Nomes", "Pontos Totais"]]
bar_total = px.bar(total.T,
             x='Nomes',
             y='Pontos Totais')


cbase = totalinv.loc[['Nomes', 'C. Base']]
bar_cbase = px.bar(cbase.T,
             x='Nomes',
             y='C. Base')

cessencial = totalinv.loc[['Nomes', 'C. Essencial']]
bar_cessencial = px.bar(cessencial.T,
             x='Nomes',
             y='C. Essencial')


ctotal = totalinv.loc[['Nomes', 'C. Total']]
bar_ctotal = px.bar(ctotal.T,
             x='Nomes',
             y='C. Total')

ctotalmais = totalinv.loc[['Nomes', 'C. Total +']]
bar_ctotalmais = px.bar(ctotalmais.T,
             x='Nomes',
             y='C. Total +')

techmensal = totalinv.loc[['Nomes', 'Tech Mensal']]
bar_techmensal = px.bar(techmensal.T,
             x='Nomes',
             y='Tech Mensal')

techanual = totalinv.loc[['Nomes', 'Tech Anual']]
bar_techanual = px.bar(techanual.T,
             x='Nomes',
             y='Tech Anual')

extgar = totalinv.loc[['Nomes', 'Ext. Garantia Resolve']]
bar_extgar = px.bar(extgar.T,
             x='Nomes',
             y='Ext. Garantia Resolve')

eqtestes = totalinv.loc[['Nomes', 'Euip. Com testes feitos']]
bar_eqtestes = px.bar(eqtestes.T,
             x='Nomes',
             y='Euip. Com testes feitos')

wsafe = totalinv.loc[['Nomes', 'W. Safe']]
bar_wsafe = px.bar(wsafe.T,
             x='Nomes',
             y='W. Safe')

errfatura = totalinv.loc[['Nomes', 'S/ fatura, fatura incorrecta ou ileg??vel']]
bar_errfatura = px.bar(errfatura.T,
             x='Nomes',
             y='S/ fatura, fatura incorrecta ou ileg??vel')

falhadescfis = totalinv.loc[['Nomes', 'Falha na descri????o f??sica']]
bar_falhadescfis = px.bar(falhadescfis.T,
             x='Nomes',
             y='Falha na descri????o f??sica')

falhadescacess = totalinv.loc[['Nomes', 'Falha na descri????o de acess??rios']]
bar_falhadescacess = px.bar(falhadescacess.T,
             x='Nomes',
             y='Falha na descri????o de acess??rios')

falhanumser = totalinv.loc[['Nomes', 'Falta de nro de s??rie']]
bar_falhanumser = px.bar(falhanumser.T,
             x='Nomes',
             y='Falta de nro de s??rie')

errsubst = totalinv.loc[['Nomes', 'Subst <30 dias incorrecta']]
bar_errsubst = px.bar(errsubst.T,
             x='Nomes',
             y='Subst <30 dias incorrecta')

pforcados = totalinv.loc[['Nomes', 'P. For??ados em falta']]
bar_pforcados = px.bar(pforcados.T,
             x='Nomes',
             y='P. For??ados em falta')




col1, col2 = st.columns(2)


with col1:

    st.title(':red[N??1 ATUAL]')
    st.image(img1, caption='Baui')

with col2:

    lista_graficos = list(df.columns.values)
    lista_graficos.pop(0)


    result = st.selectbox('Escolhe um grafico', lista_graficos)

    if result == "Pontos Totais":
        st.plotly_chart(bar_total)
    if result == 'C. Base':
        st.plotly_chart(bar_cbase)
    if result == 'C. Essencial':
        st.plotly_chart(bar_cessencial)
    if result == 'C. Total':
        st.plotly_chart(bar_ctotal)
    if result == 'C. Total +':
        st.plotly_chart(bar_ctotalmais)
    if result == 'Tech Mensal':
        st.plotly_chart(bar_techmensal)
    if result == 'Tech Anual':
        st.plotly_chart(bar_techanual)
    if result == 'Ext. Garantia Resolve':
        st.plotly_chart(bar_extgar)
    if result == 'Euip. Com testes feitos':
        st.plotly_chart(bar_eqtestes)
    if result == 'W. Safe':
        st.plotly_chart(bar_wsafe)
    if result == 'S/ fatura, fatura incorrecta ou ileg??vel':
        st.plotly_chart(bar_errfatura)
    if result == 'Falha na descri????o f??sica':
        st.plotly_chart(bar_falhadescfis)
    if result == 'Falha na descri????o de acess??rios':
        st.plotly_chart(bar_falhadescacess)
    if result == 'Falta de nro de s??rie':
        st.plotly_chart(bar_falhanumser)
    if result == 'Subst <30 dias incorrecta':
        st.plotly_chart(bar_errsubst)
    if result == 'P. For??ados em falta':
        st.plotly_chart(bar_pforcados)



