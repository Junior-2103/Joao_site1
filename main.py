import streamlit as st

# streamlit run .\joao\streamlit_joao.py

st.set_page_config(page_title='Um pouco sobre minha rã')

st.title(':green[Site sobre a minha rã touro]')

st.subheader(':blue[a minha rã, é da especie Rã-touro, do nome cientifico (Lithobates castebeianus). Essa especie de rã pode atingir 20 centimetros de comprimento e pesar mais de 2kg, sendo a segunda maior especie de rã do mundo.]','left')

botao = st.button('clique aqui para saber mais sobre a minha rã')



if botao == True:
    st.write('A minha rã virou rã no dia 21 de dezembro de 2022, pois antes dela virar realmente uma rã, ela era um girino, mas para ela virar rã, ocorreu um processo chamado de metamorfose. E ai esta uma foto dela quando era girino: ')
    st.image(r'https://raw.githubusercontent.com/Junior-2103/Joao_site1/main/IMG_20220720_200754.jpg')
botao1 = st.button('ver foto atual')
if botao1 == True:
    st.write('essa e ela um pouco mais atual, mas oque você não sabe, é que na verdade, minha rã é macho e se chama Rana, eu pensei que era fêmea, por isso do nome, mas depois de um tempo descobri que na verdade era um macho, e decidi deixar o nome, ele tem 1 ano, o dia do aniversário dele é dia 21 de dezembro, pois nesse dia, foi o dia que ele passou de girino para Rã, se quizer saber mais, veja meu canal, se chama :frog word')
    st.image(r'https://raw.githubusercontent.com/Junior-2103/Joao_site1/main/IMG_20240225_184102.jpg')
