import streamlit as st
from pathlib import Path
import base64

st.markdown('''<style>.css-1egvi7u {margin-top: -4rem;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # lightmode
# Design change height of text input fields headers
st.markdown('''<style>.css-qrbaxs {min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design change spinner color to primary color
st.markdown('''<style>.stSpinner > div > div {border-top-color: #9d03fc;}</style>''',
    unsafe_allow_html=True)
# Design change min height of text input box
st.markdown('''<style>.css-15tx938{min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design hide top header line
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

st.markdown('Generate professional sounding emails based on your direct comments - powered by Artificial Intelligence (OpenAI GPT-3) Implemented by '
    '[stefanrmmr](https://www.linkedin.com/in/stefanrmmr/) - '
    'view project source code on '
    '[GitHub](https://github.com/stefanrmmr/gpt3_email_generator)')

st.write('\n')  # add spacing
st.write(
    """
    # Streamlit roadmap

    Welcome to our roadmap! 👋 This app shows some projects we're working on or have
    planned for the future. Plus, there's always more going on behind the scenes — we
    sometimes like to surprise you ✨
    """
)
st.info(
    """
    Need a feature that's not on here?
    [Let us know by opening a GitHub issue!](https://github.com/streamlit/streamlit/issues)
    """,
    icon="👾",
)
st.success(
    """
    Read [the blog post on Streamlit's 2023 roadmap](https://blog.streamlit.io/the-next-frontier-for-streamlit/)
    to understand our broader vision.
    """,
    icon="🗺",
)

# Design hide top header line
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


import streamlit as st

image_path = 'image/12.png'


st.image(image_path)
# Define the HTML hyperlink with the image
# html_string = f'<a href="{image_path}" target="_blank"><img src="{image_path}" width="200" caption="legend"></a>'

# # Display the image using `st.markdown`
# st.markdown(html_string, unsafe_allow_html=True)