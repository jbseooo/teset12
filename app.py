import streamlit as st
from pathlib import Path
import base64

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path, max_width='100%'):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' style='max-width:{};'>".format(
        img_to_bytes(img_path),
        max_width
    )
    return img_html

st.markdown(img_to_html('image/12.png', max_width='100%'),unsafe_allow_html=True)

# JavaScript 코드 생성
javascript_code = """
<script>
    var modal = document.getElementById('myModal');
    var img = document.getElementsByClassName('img-clickable')[0];
    var modalImg = document.getElementById("img01");

    img.onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
    }

    var span = document.getElementsByClassName("close")[0];

    span.onclick = function() { 
        modal.style.display = "none";
    }
</script>
"""

# JavaScript 코드 표시
st.markdown(javascript_code, unsafe_allow_html=True)

# 모달 창 HTML 코드 생성
modal_html = """
<div id="myModal" class="modal" style="display:none;">
  <span class="close">&times;</span>
  <img class="modal-content" id="img01" style="max-width:100%;">
</div>
"""

# 모달 창 HTML 코드 표시
st.markdown(modal_html, unsafe_allow_html=True)










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

image_path = 'image/12.png'


st.image(image_path)
# Define the HTML hyperlink with the image
# html_string = f'<a href="{image_path}" target="_blank"><img src="{image_path}" width="200" caption="legend"></a>'

# # Display the image using `st.markdown`
# st.markdown(html_string, unsafe_allow_html=True)
