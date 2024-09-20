import streamlit as st

# Configuração da página
st.set_page_config(page_title="Guia Conceitual - Trading", layout="wide")

# Função para exibir imagens
def mostrar_imagem(imagem_path, legenda):
    st.image(imagem_path, caption=legenda, use_column_width=True)

# Opções de navegação
secoes = {
    "Arquitetura": {
        "Introdução": "Aqui explicaremos os conceitos centrais do trading, incluindo análise técnica e fundamentalista, com diferentes estratégias para day trading e swing trading.",
        "Análise Técnica": "A análise técnica envolve o estudo dos gráficos de preços e a utilização de indicadores técnicos para prever movimentos futuros.",
        "Análise Fundamentalista": "A análise fundamentalista se concentra em avaliar o valor intrínseco de um ativo com base em dados econômicos e financeiros.",
        "Day Trading": "Day trading refere-se a estratégias que envolvem a compra e venda de ativos no mesmo dia.",
        "Swing Trading": "Swing trading é uma abordagem que visa capturar movimentos de preço em um período médio de tempo."
    },
    "Indicadores": {
        "Introdução": "Exploração dos principais indicadores como médias móveis, RSI, e MACD. Esses indicadores ajudam a identificar tendências e momentos para entrar ou sair de posições.",
        "Médias Móveis": "Médias móveis são usadas para suavizar os dados de preços e identificar tendências.",
        "RSI": "O Índice de Força Relativa (RSI) é um indicador de momentum que mede a velocidade e a mudança dos movimentos de preços.",
        "MACD": "O MACD (Moving Average Convergence Divergence) é um indicador de tendência que mostra a relação entre duas médias móveis."
    },
    "Táticas": {
        "Introdução": "Explanação sobre as táticas mais usadas pelos traders, como tape reading, scalping e estratégias de rompimento.",
        "Tape Reading": "Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.",
        "Scalping": "Scalping é uma estratégia de curto prazo que busca obter pequenos lucros a partir de movimentos de preços muito pequenos.",
        "Estratégias de Rompimento": "Estratégias de rompimento envolvem a identificação e a negociação de momentos em que o preço ultrapassa níveis importantes de suporte ou resistência."
    },
    "Pacotes Relacionados": {
        "Introdução": "Ferramentas de backtesting permitem simular estratégias de trading usando dados históricos.",
        "Backtrader": "Backtrader é uma plataforma de backtesting que permite testar e otimizar estratégias de trading.",
        "QuantConnect": "QuantConnect oferece uma plataforma de backtesting e desenvolvimento de estratégias com suporte para múltiplas classes de ativos.",
        "Zipline": "Zipline é uma biblioteca de backtesting focada em estratégias de trading algorítmico."
    }
}

# Barra lateral com seleção de seção
selecao_secao = st.sidebar.selectbox("Escolha uma seção", list(secoes.keys()))

# Exibir o conteúdo da seção selecionada
if selecao_secao:
    st.title(selecao_secao)
    
    for subsecao, descricao in secoes[selecao_secao].items():
        st.subheader(subsecao)
        st.markdown(descricao)
        # Aqui você pode adicionar imagens específicas para cada subseção, se desejar
        if subsecao == "Análise Técnica":
            mostrar_imagem("https://example.com/imagem_analise_tecnica.png", "Análise Técnica")
        elif subsecao == "Análise Fundamentalista":
            mostrar_imagem("https://example.com/imagem_analise_fundamentalista.png", "Análise Fundamentalista")
        elif subsecao == "Day Trading":
            mostrar_imagem("https://example.com/imagem_day_trading.png", "Day Trading")
        elif subsecao == "Swing Trading":
            mostrar_imagem("https://example.com/imagem_swing_trading.png", "Swing Trading")
        elif subsecao == "Médias Móveis":
            mostrar_imagem("https://example.com/imagem_median_moveis.png", "Médias Móveis")
        elif subsecao == "RSI":
            mostrar_imagem("https://example.com/imagem_rsi.png", "RSI")
        elif subsecao == "MACD":
            mostrar_imagem("https://example.com/imagem_macd.png", "MACD")
        elif subsecao == "Tape Reading":
            mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")
        elif subsecao == "Scalping":
            mostrar_imagem("https://example.com/imagem_scalping.png", "Scalping")
        elif subsecao == "Estratégias de Rompimento":
            mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")
        elif subsecao == "Backtrader":
            mostrar_imagem("https://example.com/imagem_backtrader.png", "Backtrader")
