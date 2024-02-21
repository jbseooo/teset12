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


def img_to_html2(img_path, img_id):
    html = f"<img id='{img_id}' src='{img_path}' width='150' height='100' onclick='fnImgPop(this.src)'>"
    return html
with open('./styles/0_style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# html_code = """
# <body>
# {}
# </body>
# <script type="text/javascript">
# <!--
#  function fnImgPop(url){
#   var img=new Image();
#   img.src=url;
#   var img_width=img.width;
#   var win_width=img.width+25;
#   var img_height=img.height;
#   var win=img.height+30;
#   var OpenWindow=window.open('','_blank', 'width='+img_width+', height='+img_height+', menubars=no, scrollbars=auto');
#   OpenWindow.document.write("<style>body{margin:0px;}</style><img src='"+url+"' width='"+win_width+"'>");
#  }
# //-->
# </script>
# """

# st.markdown(html_code.format(img_to_html2('image/12.png', 'char0')), unsafe_allow_html=True)

st.markdown('''
            <div class='image_container'>
            {}
            </div>
            '''.format(img_to_html('assets/12.png','char0')), unsafe_allow_html=True)

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

