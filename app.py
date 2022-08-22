# import the child scripts
import streamlit as st
import awesome_streamlit as ast
import home
import data 
import plots
import pred
import dashboard
from PIL import Image

ast.core.services.other.set_logging_format()

# create the pages
PAGES = {
    "Home": home,
    "Data":data,
    "Data visualisations": plots,
    "Predictions": pred,
    "predictions": dashboard
}


# render the pages
def main():
   
    st.sidebar.title("Sales Prediction")
    selection = st.sidebar.selectbox("Select", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    if selection =="Home":
        st.sidebar.title("INFORMATION")
        st.sidebar.info(
        """
        Rossman Pharmacueticals sales prediction web app. This web app allows store managers at Rossman Pharmacueticals to predict sales in their stores
        using Machine Learning
        """
    )
        image = Image.open('pic.jpg')
        st.image(image, caption='Pharmacueticals Sales Prediction using Machine Learning')
    elif selection=="Predictions":
        st.sidebar.title("")


if __name__ == "__main__":
    main()