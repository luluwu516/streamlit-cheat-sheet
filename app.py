import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

logo = Image.open('logo.png')

installation = "$ pip install streamlit"
run_streamlit = "$ streamlit run [streamlit_script.py]"
terminal_code = """$ streamlit --help
$ streamlit run streamlit_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version"""

basics = """import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
st.dataframe(df.head())

df.add_rows(df2)
st.dataframe(df) # df + df2
"""

plotly = """df = pd.read_csv("data.csv")
df = df.iloc[0:10, ::]
st.dataframe(df)

# Pie Chart
fig = px.pie(df, values='Price',names='Item',
             title='Pie Chart of Product')
st.plotly_chart(fig)

# Bar Chart
fig2 = px.bar(df,x='Item',y='Price')
st.plotly_chart(fig2)"""

text_input = """# Text Input
fname = st.text_input("Enter Firstname")
st.write(fname)

# Text Input Hide Password
password = st.text_input("Enter Password",type='password')
st.write(password)

# Text Area
message = st.text_area("Enter Message",height=100)
st.write(message)

# Numbers
number = st.number_input("Enter Number",1.0,25.0)
st.write(number)

# Date and Time Input
appointment_date = st.date_input("Appointment Date")
appointment_time = st.time_input("Appointment Time")

# Color Picker
my_color = color_picker('Pick a color')

# Camera Input
photo = camera_input("Smile!")
"""

display_text = """# Display Text
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader"
st.text("This is some text.")
st.markdown("# This is markdown H1")
st.markdown("This is markdown ~~delete~~ *italic* **bold**")

# Status
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")
st.progress(progress_variable_1_to_100)
st.balloons()
st.snow()

# Superfunction
st.write("### This is markdown text")
st.write("This is normal text")
st.write(1+2)

# Code
st.code('print("My first Streamlit App")', language='python')
st.code('vector %>% as.dataframe()', language='r')

# Help Info 
st.help(print)"""

widgets = """# Select
program_lang = ["Python","R","Julia","Go","Rust"]
choice = st.selectbox("Programming languages",program_lang)
st.write("You choose {}".format(choice))

# Multiselect
spoken_lang = ("English","中文","日本語","Español","Français")
my_lang = st.multiselect("Language", spoken_lang, default="English")

# Slider
age = st.slider("Age", 1, 100)
color = st.select_slider("Select color",
                         options=["Yellow","Red","Blue","Green","Black","White"],
                         value=("Yellow","Red"))

# expander
with st.expander("click to expand"):
    st.write("words in the container") 
    st.success("words in the container")
st.error("words outside the container")

# button
if st.button('Submit'):
    st.success("Success!")
else:
    st.warning("Failed!")"""

layout = """st.set_page_config(
    page_title="Layout",
    page_icon="random", # st.image / random / emoji ("🐧" or ":penguin:")
    layout="wide", # centered
    initial_sidebar_state="collapsed", # expanded or auto(default)
)
menu = st.sidebar.selectbox("Menu",["Home","About"])

if menu == "Home":
    # Columns
    col1, col2 = st.columns(2)
    with col1:
        st.title('Col1')

    with col2:
        st.title("Col2")   
else:
    st.write("About")"""

upload = """# Sidebar
uploaded_file = st.sidebar.file_uploader("Please upload your csv file.", type=["csv"])

if uploaded_file is not None: 
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv('data_demo.csv')

# Main page
if uploaded_file is not None:
    st.write(df)
    		
    with st.expander("Descriptive Summary"):
    	st.dataframe(df.describe())

else:
    st.write('Wait for the uploaded data. This is a demo.')
    st.dataframe(df)"""

download = """df_csv = df.to_csv().encode('utf-8')

st.download_button(
     label = "Download csv file",
     data = df_csv,
     file_name='download_df.csv',
     mime='text/csv',
 )

st.download_button(
     label = "Download txt file",
     data = df_csv,
     file_name='download_df.txt',
     mime='text/csv',
 )

# Download image
from PIL import Image
image = Image.open('image.png')
st.image(image, caption='A beacutiful image')

with open("image.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="image.png",
             mime="image/png"
           )"""

display_charts = """ # Display charts
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.pyplot(fig)
st.altair_chart(data)
st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.graphviz_chart(data)
st.map(data)"""



def main():
    st.set_page_config(
        page_title="Streamlit Cheat Sheet",
        page_icon="💡",
        layout="wide",)
    
    st.title("Streamlit Cheat Sheet")
    
    with st.sidebar:
        st.image(logo)
        st.title("Streamlit")
        st.text("A open-source app framework\nin pure Python")
        st.header("Installation")
        st.code(installation, language="r")
        st.header("Get Started")
        st.code(run_streamlit, language="r")
        st.header("Command Line")
        st.code(terminal_code, language="r")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Basics")
        st.code(basics, language="python")
        st.header("Display Text")
        st.code(display_text, language="python")
        st.header("Widgets")
        st.code(widgets, language="python")
        
    
    with col2:
        st.header("Plotly")
        st.code(plotly, language="python")
        st.header("Text Input")
        st.code(text_input, language="python")
        st.header("Upload")
        st.code(upload, language="python")
        
        
    with col3:
        st.header("Display Charts")
        st.code(display_charts, language="python")
        st.header("Layout")
        st.code(layout, language="python")
        st.header("Download")
        st.code(download, language="python")
        
        
    

if __name__ == '__main__':
    main()










































