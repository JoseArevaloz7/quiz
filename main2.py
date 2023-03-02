import streamlit as st
import vali as m
import json

with open("db.json", 'r') as file:
    content = file.read()

st.set_page_config(layout="wide")
data = json.loads(content)
st.title('Login app')
ban = False


menu = ['Login',]
start = st.sidebar.selectbox('Menu', menu)
q2=''
q3=''

if start == 'Login':
    st.sidebar.subheader('Login')
    st.sidebar.text_input('Usuario', placeholder='Usuario', key="userIn")
    st.sidebar.text_input('Contraseña', type='password', placeholder='Contraseña', key="passIn")

    if st.sidebar.checkbox('Ingresar'):

        user = st.session_state['userIn']
        _pass = st.session_state['passIn']
        checkLogin = m.checkPass(data, _pass, user)
        index = checkLogin[1]
        if checkLogin[0]:
            col1, empty, col2 = st.columns([1.5, 0.5, 1.5])

            st.sidebar.success('Usuario y contraseña correctos!')
            menu = ['Perfil', 'Menu', 'Encuesta']
            # menu = ['Login']
            with col1:
                choice = st.selectbox('Menu', menu, key="menuB")

            if choice == 'Perfil':
                with col2:
                    st.title(data[index]['name'])
            if choice == 'Menu':
                st.info('Este apartado esta en desarrollo, vuelva pronto!')
            if choice == 'Encuesta':
                with col2:
                    st.radio(
                        "¿Qué cosa es que cuanto más le quitas más grande es? 😊",
                        key="q1",
                        options=["Un lago", "Una Sandia", "Un agujero"],
                    )
                    if st.session_state.q1 == 'Un agujero':
                        st.radio(
                            "Si tengo 5 tv en una mano y 5 en la otra mano, ¿Qué tengo? 😊",
                            key="q2",
                            options=["10 tv", "7 tv", "Unas manotas"],
                        )
                        q2 = st.session_state.q2
                    if q2 == "Unas manotas":
                        st.radio(
                            "Has completado bien de manera correcta las adivinanzas, ¿List@ para la encuesta final? 😊",
                            key="q3",
                            options=["No", "Si"],
                        )
                        q3 = st.session_state.q3
                    if q3 == "Si":
                        st.radio(
                            "Señorita Shanik, ¿Quisiera usted ser mi novia? 🫶❤️",
                            key="qf",
                            options=[ 'Mi momento mas humilde', "Si ❤", "No :(",
                                     "Ni que tuvieras tanta suerte",],
                        )
                        if st.session_state.qf == 'Si ❤':
                            st.info('La quiero mucho! ❤️')
                        if st.session_state.qf == 'No :(':
                            st.info('Pa saber, Que al cabo ni queria! :(')
                        if st.session_state.qf == 'Ni que tuvieras tanta suerte':
                            st.info('Ya pongale que si, pa que se hace! ')
        else:
            st.write('no')

