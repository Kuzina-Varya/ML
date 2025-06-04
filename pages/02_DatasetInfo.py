import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Описание данных", layout="wide")
st.title("Описание датасета — стоимости дома в Мумбаи")

st.markdown("""
Данные представляют собой набор информации о характеристиках дома. Цель — прогнозирование стоимости дома (`price`) 
на основе ряда признаков. Датасет содержит как числовые, так и категориальные данные, закодированные с помощью one-hot encoding.
""")

st.header("Структура датасета")

data_description = {
    "price" : "цена", 
    "area":"площадь",
    "latitude": "ширина", 
    "longitude":"длинна",
    "Bedrooms": "спальни", 	
    "Bathrooms":"ванные комнаты" ,	
    "Balcony": "балкон",
    "Status":	"статус", 
    "neworold": "новый или старый дом", 
    "parking"	: "парковка",
    "Furnished_status":"наличие мебели" ,	
    "Lift": "лифт", 	
    "type_of_building": "тип здания" 
}

st.subheader(" Признаки и их описание:")
for feature, desc in data_description.items():
    st.markdown(f"**{feature}**: {desc}")

st.subheader(" Целевая переменная")
st.markdown("`price` — ценна дома в местной валюте.")

st.subheader(" Тип задачи")
st.markdown("Задача регрессии: предсказание непрерывной числовой величины — стоимости дома.")

st.write(f"Количество признаков: {len(data_description)}")

st.markdown("---")

st.header("Этапы предобработки данных (EDA)")
st.markdown("""
**Заполнить пропущенные значения:**

- Заполнить столбецы 'Furnished_status','Status' значением 'unknown' , т.к. пропущенных значений много, а продается ли квартира с мебелью или нет может влиять на еее стоимость.

**Изменение типа данных:**

- тип данных столбца 'price' переведен с float64 на int64;
- тип данных столбца 'area' переведен с float64 на int64;
- тип данных столбца 'Bedrooms'переведен с float64 на int64;
- тип данных столбца 'Bathrooms' переведен с float64 на int64;
- тип данных столбца 'Balcony' переведен с float64 на int64;
- тип данных столбца 'parking' переведен с float64 на int64;
- тип данных столбца 'Lift' переведен с float64 на int64;
- столбцы с категориальными типами данных ('Furnished_status','Status') были переведены в столбцы с числовыми типами данных.

**Удаление выбросов:**
- Выбросы параметров: 'area','Bedrooms','Bathrooms'.

**Изучение ценового фактора:**
- Факторы, влияющие на цену: 'area','Bedrooms','Bathrooms'.
""")
