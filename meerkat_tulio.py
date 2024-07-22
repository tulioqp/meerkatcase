import requests
import streamlit as st
import bs4


# function to perform web scraping
def scrape():
    '''
    inputs: void; outputs: the content from 'http://bianca.com'
    '''

    url = 'http://bianca.com'
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    content = soup.find('h1')
    if content:
        return content.text.strip()
    else:
        return 'Content not found'
    

# aesthetic purpose only
def beautify():
    '''
    inputs: void; outputs: '\n' 4 times, returns None
    '''

    for i in range(4):
        st.text("\n")
    
    return None
            

# streamlit code
st.html("<h1 style='text-align: center; color: violet;'>Case Meerkat</h1>")
st.html("<h4 style='text-align: center; color: white;'><i>Web Scraping</i></h4>")
st.header("", divider='violet')
beautify()

button = st.button('Realizar Web Scraping', type='primary', help='Clique para realizar o web scraping')
if button:
    with st.container(border=True):
        st.title(scrape(), anchor=False)
        st.write(':heart:\n')
        button = st.button("Fechar", help='Clique para fechar')
    st.balloons()
else:
    st.write('Clique para exibir o conteúdo')
