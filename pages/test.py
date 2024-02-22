import streamlit as st

already_scrolled = False  # 이미 스크롤되었는지를 추적하는 변수

def scroll(js_path:str='main', 
           behavior:str='smooth', 
           block:str='center', 
           inline:str='center'
           ) -> None:
    global already_scrolled
    
    # 이미 스크롤되었는지 확인
    if not already_scrolled:
        js = f'''
            <script>
                const element = window.parent.{js_path};
                element.scrollIntoView({{
                    behavior: "{behavior}", 
                    block: "{block}", 
                    inline: "{inline}"}});
            </script>
            '''
        
        st.components.v1.html(js)
        already_scrolled = True  # 이미 스크롤되었음을 표시

st.title("Streamlit Scroll Test")

with st.container():
    st.header("AP 브랜드 가치")
    
    for i in range(20):
        st.write(f"1st Area : {i}")

with st.container():
    st.header("CD 브랜드 가치")
    for j in range(20):
        st.write(f"2nd Area : {j}")
    
if st.sidebar.button('scroll to bottom of 1st container'):
    js_path = 'document.querySelector("#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(10) > div > div > p")'
    scroll(js_path=js_path)
    
if st.sidebar.button('scroll to bottom of 2nd container'):
    js_path = 'document.querySelector(document.querySelector(document.querySelector("#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(12) > div > div > p"))'
    scroll(js_path=js_path)
    
    
if st.sidebar.button('scroll to bottom of main'):
    scroll(js_path='document.querySelector("footer")')
