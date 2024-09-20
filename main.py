import streamlit as st

# Configuração da página
st.set_page_config(page_title="Guia Conceitual - ALGORITHMIC TRADING", layout="wide")

# Função para exibir imagens
def mostrar_imagem(imagem_path, legenda):
    st.image(imagem_path, caption=legenda, use_column_width=True)

# Sidebar para Modo de Seleção
st.sidebar.title("Seleção de Modo")
mode = st.sidebar.radio("Selecione o Modo:", options=["Navegação", "Chat"], index=0)

st.sidebar.markdown("---")

# Se o modo selecionado for "Navegação", exibe as páginas principais
if mode == "Navegação":
    st.sidebar.title("Seções")
    pagina = st.sidebar.radio(
        "Escolha uma seção", 
        [
            "1 . Introdução", 
            "2 . Backtesting e Execução Automática", 
            "3 . Os Fundamentos da Reversão à Média", 
            "4 . Estratégias de Reversão à Média", 
            "5 . Reversão à Média de Ações e ETFs", 
            "6 . Reversão à Média de Moedas e Futuros", 
            "7 . Estratégias de Momentum Interdiário", 
            "8 . Estratégias de Momentum Intradiário", 
            "9 . Gestão de Riscos", 
            "10 . Conclusão", 
            "Referências"
        ]
    )
    # Função para exibir subseções
    def mostrar_subsecoes(pagina_atual):
        subsecoes = {
            "2 . Backtesting e Execução Automática": [
                "Introdução",
                "Análise Técnica",
                "Análise Fundamentalista",
                "Day Trading",
                "Swing Trading"
            ],
            "3 . Os Fundamentos da Reversão à Média": [
                "1. Mean Reversion and Stationarity",
                "Médias Móveis",
                "RSI",
                "MACD"
            ],
            "Táticas": [
                "Introdução",
                "Tape Reading",
                "Scalping",
                "Estratégias de Rompimento"
            ],
            "Pacotes Relacionados": [
                "Introdução",
                "Backtrader",
                "QuantConnect",
                "Zipline"
            ]
        }
        if pagina_atual in subsecoes:
            return st.sidebar.radio("Subseções", subsecoes[pagina_atual])
        return None

    # Navegação das subseções
    subsecao = mostrar_subsecoes(pagina)
    
    if pagina == "1 . Introdução":
        st.title("Introdução ao Algoritmo Trading")
        
        st.markdown("""
        Este curso oferece um guia prático sobre estratégias de trading algorítmico que podem ser implementadas tanto por traders individuais quanto institucionais. Diferente de abordagens puramente teóricas, o foco está em estratégias que realmente funcionam no mercado.
                    
        Vamos explorar uma ampla gama de estratégias, divididas em dois grandes grupos: estratégias de reversão à média e estratégias de momentum. Cada categoria será explicada em detalhes, com ênfase tanto nas técnicas padrão de trading quanto nos fundamentos que justificam o funcionamento dessas estratégias.

        O objetivo é manter as estratégias simples e lineares, para evitar o risco de overfitting (ajuste excessivo dos dados) e data-snooping (enviesamento por exploração de dados), problemas comuns em estratégias mais complexas.
        Estratégias de Reversão à Média

        No campo das estratégias de reversão à média, cobriremos diversas técnicas estatísticas para detectar a reversão à média em séries temporais. Entre elas estão:

            Teste Dickey-Fuller Aumentado (ADF);
            Exponente de Hurst;
            Teste da Razão de Variância;
            Meia-vida.

        Também discutiremos a cointegração de um portfólio de instrumentos, utilizando testes como:

            Teste Dickey-Fuller Aumentado para Cointegração (CADF);
            Teste de Johansen.

        O foco será explicar de forma intuitiva o que cada um desses testes realmente mede e as equações matemáticas simples por trás deles.
        Técnicas de Trading com Reversão à Média

        Abordaremos as técnicas mais simples e eficazes para operar portfólios que seguem a reversão à média, como:

            Bandas de Bollinger;
            Filtro de Kalman.

        Discutiremos a melhor forma de usar dados de preços para essas estratégias: preços brutos, logaritmos dos preços ou suas razões. O filtro de Kalman, em especial, será apresentado como uma ferramenta valiosa em diversas estratégias. Também faremos distinção entre reversão à média em séries temporais e reversão à média cross-sectional (entre diferentes ativos).
        Exemplos Práticos

        Os exemplos de estratégias de reversão à média incluirão:

            Modelos de ações interdiários e intradiários;
            Pares e triplas de fundos negociados em bolsa (ETFs);
            Spreads de futuros.

        Além disso, vamos discutir como a ascensão dos dark pools e do high-frequency trading pode tornar essas estratégias mais desafiadoras nos últimos anos.
        Estratégias de Momentum

        Por outro lado, as estratégias de momentum são guiadas por quatro principais fatores que impulsionam esse comportamento em ações e futuros. Veremos como extrair momentum a partir de séries temporais e entre diferentes ativos. Novas abordagens, como aquelas baseadas em eventos de notícias, sentimento de mercado, fluxo de ordens e trading de alta frequência, também serão exploradas.
        Armadilhas Comuns

        Uma parte importante deste curso será dedicada a discutir as armadilhas comuns que podem fazer com que os resultados do trading ao vivo divergem significativamente dos backtests. Questões como overfitting e viés de sobrevivência serão abordadas.





        """)
      


    # Página: Arquitetura
    elif pagina == "Backtesting e Execução Automática":
        st.title("Backtesting and Automated Execution")

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

    # Página: Indicadores
    elif pagina == "3 . Os Fundamentos da Reversão à Média":
        st.title("3 . Os Fundamentos da Reversão à Média")

        if subsecao == "1. Mean Reversion and Stationarity":
            st.markdown("""
            1. Mean Reversion and Stationarity

                Essa seção explica como a reversão à média está relacionada à estacionaridade. Uma série temporal estacionária tem uma variância que cresce de forma mais lenta do que em um passeio aleatório geométrico. As séries que exibem reversão à média tendem a se mover para um valor central ao longo do tempo.
                Código para o Teste ADF (Augmented Dickey-Fuller Test):

                Este teste verifica se uma série temporal é estacionária e apresenta reversão à média
            """)


            code = '''
            import statsmodels.tsa.stattools as adf_test

            # Dados da série temporal
            prices = [...]  # Substitua pela sua série de preços

            # Aplicação do teste ADF
            result = adf_test.adfuller(prices)

            # Exibir os resultados
            print(f'Testatística ADF: {result[0]}')
            print(f'Valor-p: {result[1]}')
            print(f'Valores Críticos: {result[4]}')
            '''

            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


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

    # Página: Táticas
    elif pagina == "Táticas":
        st.title("Táticas")
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

    # Página: Pacotes Relacionados
    elif pagina == "Pacotes Relacionados":
        st.title("Pacotes Relacionados")
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
            mostrar_imagem("https://example.com/imagem_quantconnect.png", "QuantConnect")
        elif subsecao == "Zipline":
            st.markdown("""
            Zipline é uma biblioteca de backtesting de código aberto em Python.
            """)
            mostrar_imagem("https://example.com/imagem_zipline.png", "Zipline")


# Se o modo for "Chat", "Debug" ou "Configuração", o conteúdo é carregado a partir dos arquivos
elif mode == "Chat":
    chat_option = st.sidebar.radio("Opções de Chat:", options=["Conversar", "Configurações", "Debug"], index=0)

    if chat_option == "Conversar":
        with open("pag/chat.py", encoding="utf-8") as file:
                exec(file.read())

    elif chat_option == "Configurações":
        # Exibe o conteúdo de configurações
        with open("pag/02_Configuração.py", encoding="utf-8") as file:
            exec(file.read())

    elif chat_option == "Debug":
        # Exibe o conteúdo de debug
        with open("pag/01_Debug.py", encoding="utf-8") as file:
            exec(file.read())