import streamlit as st

st.set_page_config(page_title="Информация о студенте", layout="wide")

# Заголовок
st.markdown("<h1 style='text-align: center;'> Информацией о разработчике моделей ML</h1>", unsafe_allow_html=True)

# Основная информация
st.markdown("""
<p style='font-size: 20px;'>
<strong>ФИО:</strong> Кузина Варвара Михайловна<br>
<strong>Группа:</strong> МО-231<br>
<strong>Тема РГР:</strong> Разработка Web-приложения для инференса моделей ML и анализа данных
</p>
""", unsafe_allow_html=True)

#Фото (если есть)
st.image("nnlKausKnVY.jpg", caption="Фото студента", width=300)

# Подвал
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 16px;'>Омск 2025</p>",
            unsafe_allow_html=True)