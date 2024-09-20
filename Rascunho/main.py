import streamlit as st

# Configuração da página
st.set_page_config(page_title="Guia Conceitual - Trading", layout="wide")

# Função para exibir imagens
def mostrar_imagem(imagem_path, legenda):
    st.image(imagem_path, caption=legenda, use_column_width=True)

# Barra lateral para navegação entre "páginas"
st.sidebar.title("Seções")
pagina = st.sidebar.radio("Ir para:", ("Arquitetura", "Indicadores", "Táticas", "Pacotes Relacionados"))




# Página: Arquitetura
if pagina == "Arquitetura":
    st.title("Arquitetura")
    st.markdown("""
    Aqui explicaremos os conceitos centrais do trading, incluindo análise técnica e fundamentalista, com diferentes estratégias para day trading e swing trading.
    """)
    # Exibindo uma imagem
    mostrar_imagem("https://example.com/imagem_arquitetura.png", "Arquitetura do Trading")

# Página: Indicadores
elif pagina == "Indicadores":
    st.title("Indicadores")
    st.markdown("""
    Exploração dos principais indicadores como médias móveis, RSI, e MACD. Esses indicadores ajudam a identificar tendências e momentos para entrar ou sair de posições.
    """)
    # Exibindo uma imagem
    mostrar_imagem("https://example.com/imagem_indicadores.png", "Indicadores no Trading")

# Página: Táticas
elif pagina == "Táticas":
    st.title("Táticas")
    st.markdown("""
    Explanação sobre as táticas mais usadas pelos traders, como tape reading, scalping e estratégias de rompimento.
    """)
    # Exibindo uma imagem
    mostrar_imagem("https://example.com/imagem_taticas.png", "Táticas de Trading")

# Página: Pacotes Relacionados
elif pagina == "Pacotes Relacionados":
    st.title("Pacotes Relacionados")
    st.markdown("""
    **Ferramentas de backtesting**  
    Essas ferramentas permitem simular estratégias de trading usando dados históricos, o que ajuda os traders a entenderem a eficácia de suas abordagens antes de colocá-las em prática.
    """)
    # Exibindo uma imagem
    mostrar_imagem("https://example.com/imagem_backtesting.png", "Ferramentas de Backtesting")
