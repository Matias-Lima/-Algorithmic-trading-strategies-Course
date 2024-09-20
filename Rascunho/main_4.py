import streamlit as st

# Configuração da página
st.set_page_config(page_title="Guia Conceitual - Trading", layout="wide")

# Função para exibir imagens
def mostrar_imagem(imagem_path, legenda):
    st.image(imagem_path, caption=legenda, use_column_width=True)

# Menu de navegação
pagina = st.sidebar.selectbox(
    "Escolha uma Seção",
    ["Arquitetura", "Indicadores", "Táticas", "Pacotes Relacionados"]
)

# Conteúdo da página Arquitetura
if pagina == "Arquitetura":
    st.title("Arquitetura")
    subsecao = st.selectbox(
        "Escolha uma Sub-seção",
        ["Introdução", "Análise Técnica", "Análise Fundamentalista", "Day Trading", "Swing Trading"]
    )
    
    if subsecao == "Introdução":
        st.markdown("""
        Aqui explicaremos os conceitos centrais do trading, incluindo análise técnica e fundamentalista, com diferentes estratégias para day trading e swing trading.
        """)
    elif subsecao == "Análise Técnica":
        st.markdown("""
        A análise técnica envolve o estudo dos gráficos de preços e a utilização de indicadores técnicos para prever movimentos futuros.
        """)
        mostrar_imagem("https://example.com/imagem_analise_tecnica.png", "Análise Técnica")
    elif subsecao == "Análise Fundamentalista":
        st.markdown("""
        A análise fundamentalista se concentra em avaliar o valor intrínseco de um ativo com base em dados econômicos e financeiros.
        """)
        mostrar_imagem("https://example.com/imagem_analise_fundamentalista.png", "Análise Fundamentalista")
    elif subsecao == "Day Trading":
        st.markdown("""
        Day trading refere-se a estratégias que envolvem a compra e venda de ativos no mesmo dia.
        """)
        mostrar_imagem("https://example.com/imagem_day_trading.png", "Day Trading")
    elif subsecao == "Swing Trading":
        st.markdown("""
        Swing trading é uma abordagem que visa capturar movimentos de preço em um período médio de tempo.
        """)
        mostrar_imagem("https://example.com/imagem_swing_trading.png", "Swing Trading")

# Conteúdo da página Indicadores
elif pagina == "Indicadores":
    st.title("Indicadores")
    subsecao = st.selectbox(
        "Escolha uma Sub-seção",
        ["Introdução", "Médias Móveis", "RSI", "MACD"]
    )
    
    if subsecao == "Introdução":
        st.markdown("""
        Exploração dos principais indicadores como médias móveis, RSI, e MACD. Esses indicadores ajudam a identificar tendências e momentos para entrar ou sair de posições.
        """)
    elif subsecao == "Médias Móveis":
        st.markdown("""
        Médias móveis são usadas para suavizar os dados de preços e identificar tendências.
        """)
        mostrar_imagem("https://example.com/imagem_median_moveis.png", "Médias Móveis")
    elif subsecao == "RSI":
        st.markdown("""
        O Índice de Força Relativa (RSI) é um indicador de momentum que mede a velocidade e a mudança dos movimentos de preços.
        """)
        mostrar_imagem("https://example.com/imagem_rsi.png", "RSI")
    elif subsecao == "MACD":
        st.markdown("""
        O MACD (Moving Average Convergence Divergence) é um indicador de tendência que mostra a relação entre duas médias móveis.
        """)
        mostrar_imagem("https://example.com/imagem_macd.png", "MACD")

# Conteúdo da página Táticas
elif pagina == "Táticas":
    st.title("Táticas")
    subsecao = st.selectbox(
        "Escolha uma Sub-seção",
        ["Introdução", "Tape Reading", "Scalping", "Estratégias de Rompimento"]
    )
    
    if subsecao == "Introdução":
        st.markdown("""
        Explanação sobre as táticas mais usadas pelos traders, como tape reading, scalping e estratégias de rompimento.
        """)
    elif subsecao == "Tape Reading":
        st.markdown("""
        Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.
        """)
        mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")
    elif subsecao == "Scalping":
        st.markdown("""
        Scalping é uma estratégia de curto prazo que busca obter pequenos lucros a partir de movimentos de preços muito pequenos.
        """)
        mostrar_imagem("https://example.com/imagem_scalping.png", "Scalping")
    elif subsecao == "Estratégias de Rompimento":
        st.markdown("""
        Estratégias de rompimento envolvem a identificação e a negociação de momentos em que o preço ultrapassa níveis importantes de suporte ou resistência.
        """)
        mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")

# Conteúdo da página Pacotes Relacionados
elif pagina == "Pacotes Relacionados":
    st.title("Pacotes Relacionados")
    subsecao = st.selectbox(
        "Escolha uma Sub-seção",
        ["Introdução", "Backtrader", "QuantConnect", "Zipline"]
    )
    
    if subsecao == "Introdução":
        st.markdown("""
        **Ferramentas de backtesting**  
        Essas ferramentas permitem simular estratégias de trading usando dados históricos, o que ajuda os traders a entenderem a eficácia de suas abordagens antes de colocá-las em prática.
        """)
    elif subsecao == "Backtrader":
        st.markdown("""
        Backtrader é uma plataforma de backtesting que permite testar e otimizar estratégias de trading.
        """)
        mostrar_imagem("https://example.com/imagem_backtrader.png", "Backtrader")
    elif subsecao == "QuantConnect":
        st.markdown("""
        QuantConnect oferece uma plataforma de backtesting e desenvolvimento de estratégias com suporte para múltiplas classes de ativos.
        """)
    elif subsecao == "Zipline":
        st.markdown("""
        Zipline é uma biblioteca de backtesting de algoritmos de trading desenvolvida pela Quantopian.
        """)
