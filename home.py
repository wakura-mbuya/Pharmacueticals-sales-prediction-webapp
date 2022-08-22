import streamlit as st



def write():
   
    with st.spinner("Loading Home ..."):
        st.title('Rossmann Pharmaceuticals Sales Prediction')
        #st.image('../assets/ross.jpg', use_column_width=True)
        st.write(
            """
            Rossman Pharmacueticals sales prediction web app.
            """
        )