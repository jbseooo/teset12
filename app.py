import streamlit as st
from pathlib import Path
import base64

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path,img_id):
    img_html = "<img src='data:image/png;base64,{}' img id='{}'>".format(
        img_to_bytes(img_path),img_id,
    )
    return img_html



with open('./styles/0_style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown('''
    <div class='image_container'>
        {}
    </div>
'''.format(img_to_html('image/12.png','char0')), unsafe_allow_html=True)
# JavaScript 코드
javascript_code = """
<script>
    // Function to open the popup and display the clicked image
    function openPopup(imgSrc) {
        document.getElementById('popup-img').src = imgSrc;
        document.getElementById('popup').style.display = 'block';
    }

    // Function to close the popup
    function closePopup() {
        document.getElementById('popup').style.display = 'none';
    }

    // Attach click event listener to all images with class 'img-clickable'
    var clickableImages = document.querySelectorAll('.img-clickable');
    clickableImages.forEach(function (img) {
        img.addEventListener('click', function () {
            openPopup(this.src);
        });
    });
</script>
"""

# HTML 코드
html_code = '''
<div class='image_container'>
    {}
</div>

<!-- The Modal -->
<div id="popup" class="modal" style="display:none;">
    <span class="close-btn" onclick="closePopup()">&times;</span>
    <img class="modal-content" id="popup-img" style="max-width:100%;">
</div>
'''

# Streamlit에서 이미지를 표시하고 HTML 및 JavaScript 코드를 표시
st.markdown(html_code.format(img_to_html('image/12.png', 'char0')), unsafe_allow_html=True)
st.markdown(javascript_code, unsafe_allow_html=True)



st.markdown("""
<div>
<span class="highlight">브랜드의 가치</span>
</div>
""",unsafe_allow_html=True)

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




with st.sidebar:
    st.markdown('''<div style="font-weight:bold;">Brand Cookbook</div>''', unsafe_allow_html=True)
    st.write("dd")
    st.write("CON")

