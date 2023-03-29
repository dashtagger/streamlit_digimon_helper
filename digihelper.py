import streamlit as st
import pandas as pd


def lower(text):
    return str(text).lower()

df = pd.read_csv("cardlist.csv", encoding= 'unicode_escape')

id_check_tab, advanced_tab = st.tabs(["ID", "Advanced"])


with id_check_tab:
    search_IDs=st.text_input("Input ID").replace(" ", "")
    st.write("example: bt1-001,st1-01")
    search_ID_list=list(map(str.lower,search_IDs.split(',')))

    if search_IDs != '':
        selected_df=df[df["ID Code"].apply(lower).isin(search_ID_list)]
        st.write(selected_df)

        for index, row in selected_df.iterrows():
            #Color	Card Name	Stage	Level	Rarity	DP	Play Cost	DigiCost	Main Effect	Inherited Effect	Security	Attribute	Type

            st.header(row['Card Name'])
            left, right = st.columns(2)
            left.write("Color 1: " + str(row['Color 1']))
            left.write("Color 2: " + str(row['Color 2']))
            left.write("Type: " + str(row['Type']))
            left.write("Stage: " + str(row['Stage']))
            left.write("Attribute: " + str(row['Attribute']))
            right.write("DigiCost 1: " + str(row['DigiCost 1']))
            right.write("DigiCost 2: " + str(row['DigiCost 2']))
            right.write("Level: " + str(row['Level']))
            right.write("DP: " + str(row['DP']))
            right.write("Play Cost: " + str(row['Play Cost']))
            st.subheader("Main Effect")
            st.write(row['Main Effect'])
            st.subheader("Inherited Effect")
            st.write(row['Inherited Effect'])
            st.subheader("Security")
            st.write(row['Security'])
            if pd.notna(row["Url"]):
                st.image(row['Url'])

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