import streamlit as st
import pandas as pd


def lower(text):
    return str(text).lower()

df = pd.read_csv("cardlist.csv", encoding= 'unicode_escape')

id_check_tab, advanced_tab = st.tabs(["ID", "Advanced"])


with id_check_tab:
    search_IDs=st.text_input("Input ID")
    st.write("example: bt1-001,st1-01")
    search_ID_list=list(map(str.lower,search_IDs.split(',')))

    if search_IDs != '':
        selected_df=df[df["ID Code"].apply(lower).isin(search_ID_list)]
        st.write(selected_df)

with advanced_tab:
    search_names=st.multiselect("Select Card Names",options=set(df['Card Name'].tolist()))
    if search_names == []:
        search_names = set(df['Card Name'].tolist())

    search_types=st.multiselect("Select Types",options=set(df['Type'].tolist()))
    if search_types == []:
        search_types = set(df['Type'].tolist())

    search_level=st.multiselect("Select Level",options=set(df['Level'].tolist()))
    if search_level == []:
        search_level = set(df['Level'].tolist())
    
    selected_df=df[(df["Card Name"].isin(search_names)) & (df["Type"].isin(search_types)) & (df["Level"].isin(search_level)) ]
    st.write(selected_df)


if st.checkbox("Show All Cards"):
    st.write(df)