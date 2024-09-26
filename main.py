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
                "A Importância do Backtesting",
                "Análise Fundamentalista",
                "Day Trading",
                "Swing Trading"
            ],
            "3 . Os Fundamentos da Reversão à Média": [
                "Introdução",
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
                    
        ### Estratégias de Reversão à Média
                    
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
                    
            Linear
            Bandas de Bollinger;
            Filtro de Kalman.

        Discutiremos a melhor forma de usar dados de preços para essas estratégias: preços brutos, logaritmos dos preços ou suas razões. O filtro de Kalman, em especial, será apresentado como uma ferramenta valiosa em diversas estratégias. Também faremos distinção entre reversão à média em séries temporais e reversão à média cross-sectional (entre diferentes ativos).
        Exemplos Práticos

        Os exemplos de estratégias de reversão à média incluirão:

            Modelos de ações interdiários e intradiários;
            Pares e triplas de fundos negociados em bolsa (ETFs);
            Spreads de futuros.

        Além disso, vamos discutir como a ascensão dos dark pools e do high-frequency trading pode tornar essas estratégias mais desafiadoras nos últimos anos.
                    
        ### Estratégias de Momentum

        Por outro lado, as estratégias de momentum são guiadas por quatro principais fatores que impulsionam esse comportamento em ações e futuros. Veremos como extrair momentum a partir de séries temporais e entre diferentes ativos. Novas abordagens, como aquelas baseadas em eventos de notícias, sentimento de mercado, fluxo de ordens e trading de alta frequência, também serão exploradas.
                    
        ### Armadilhas Comuns

        Uma parte importante deste curso será dedicada a discutir as armadilhas comuns que podem fazer com que os resultados do trading ao vivo divergem significativamente dos backtests. Questões como overfitting e viés de sobrevivência serão abordadas.

        """)
      
    # Página: Arquitetura
    elif pagina == "2 . Backtesting e Execução Automática":
        st.title("Backtesting e Execução Automática")

        if subsecao == "Introdução":
            st.markdown("""                      
            Embora o foco deste curso esteja nas categorias específicas de estratégias, é fundamental abordar algumas considerações importantes e armadilhas comuns antes de iniciar o backtesting (teste retroativo). Ignorar essas questões pode tornar o backtest inútil ou, pior, enganoso, resultando em perdas financeiras significativas.

            O backtesting é o processo de testar uma estratégia de trading com dados históricos para avaliar seu desempenho. No entanto, para que esse teste seja válido, é crucial evitar certas armadilhas comuns. Se essas precauções não forem tomadas, o resultado do backtest pode não refletir com precisão o desempenho futuro de uma estratégia.
                                    
            ### Importância da Significância Estatística

            Uma preocupação central no backtesting é a significância estatística dos resultados. Em outras palavras, até que ponto os resultados obtidos durante o teste podem ser considerados estatisticamente confiáveis? Para avaliar isso, utilizamos metodologias de testes de hipótese e simulações de Monte Carlo.

            * Quanto mais operações (trades) de ida e volta forem realizadas no backtest, maior será a confiabilidade estatística.
            * Mesmo que o backtest seja conduzido corretamente e com alta significância estatística, isso não garante que os retornos futuros serão previsíveis.

            ### Mudanças de Regime

            Outro fator importante são as mudanças de regime no mercado. Mesmo uma estratégia que tenha funcionado bem no passado pode ser completamente ineficaz no futuro devido a alterações nas condições de mercado. No curso, vamos discutir alguns exemplos históricos em que essas mudanças de regime prejudicaram estratégias previamente bem-sucedidas.
                                    
            ### Escolha da Plataforma de Software

            A escolha de uma plataforma de software adequada para realizar o backtest é outra consideração essencial que deve ser abordada desde o início. Uma plataforma eficiente pode aumentar significativamente sua produtividade, permitindo testar uma ampla gama de estratégias em diferentes classes de ativos.

            Além disso, uma boa plataforma de backtest ajuda a minimizar ou eliminar as armadilhas comuns, como overfitting (ajuste excessivo) e enviesamento de dados. Muitas vezes, a escolha da plataforma para backtesting está diretamente ligada à escolha de uma boa plataforma de execução automática, já que as melhores plataformas combinam ambas as funções.
                        
            """)
        elif subsecao == "A Importância do Backtesting":
            st.markdown("""
Backtesting é o processo de aplicar dados históricos a uma estratégia de trading para verificar como ela teria se comportado no passado. A ideia é que, se a estratégia funcionou bem com dados históricos, isso pode ser um indicativo de que ela também funcionará no futuro. A importância desse processo é evidente, especialmente quando desenvolvemos uma estratégia do zero. Queremos saber como ela teria performado antes de arriscarmos dinheiro real. Mesmo ao usar uma estratégia de uma publicação confiável, ainda é essencial realizar o backtesting por conta própria.
                        
### Por que fazer backtesting mesmo com estratégias publicadas?

Existem várias razões pelas quais realizar seu próprio backtesting, mesmo com uma estratégia publicada, é crucial:

1. Detalhes de Implementação Importam: Muitas vezes, a lucratividade de uma estratégia depende dos detalhes de sua implementação. Por exemplo:
    * As ordens de compra ou venda devem ser enviadas como ordens de "mercado na abertura" ou como ordens de mercado logo após a abertura?
    * Para contratos futuros, a ordem deve ser enviada antes do fechamento do mercado de ações (às 16h00) ou antes do fechamento do mercado futuro (às 16h15)?
    * Devemos usar o preço de compra, de venda ou o último preço para acionar uma negociação?

Esses detalhes, frequentemente ignorados em artigos publicados, podem afetar significativamente a lucratividade de uma estratégia quando ela é executada ao vivo. A única forma de garantir que implementamos esses detalhes corretamente em nosso sistema automatizado de execução é através do backtesting.

2. Transformar Backtesting em Execução Automática: Idealmente, o programa que usamos para backtestar a estratégia pode ser facilmente transformado em um programa de execução automática, garantindo que a estratégia seja implementada exatamente como planejado.

3. Evitar Armadilhas Comuns: O backtesting nos permite analisar de perto a estratégia e identificar possíveis armadilhas. Alguns exemplos:
    * Em uma estratégia que envolve posições longas e curtas, consideramos o fato de que algumas ações podem ser difíceis de tomar emprestadas para vendas a descoberto?
    * Em uma estratégia de pares entre mercados futuros, certificamos-nos de que os preços de fechamento dos dois mercados são registrados ao mesmo tempo?

Cada mercado e estratégia tem seu próprio conjunto de armadilhas específicas, e geralmente essas armadilhas inflacionam o desempenho da estratégia no backtest, fazendo parecer mais lucrativa do que realmente foi.

4. Teste Out-of-Sample (Fora da Amostra): Uma das grandes vantagens de fazer o backtesting de uma estratégia publicada é a possibilidade de realizar um verdadeiro teste fora da amostra. Isso significa testar o desempenho da estratégia em um período de tempo após sua publicação. Se os resultados forem ruins nesse período, é um sinal de que a estratégia pode ter funcionado apenas em um conjunto limitado de dados. Isso é mais importante do que parece. Alguns autores podem ajustar seus modelos para que pareçam bons mesmo com dados fora da amostra.

5. Refinar e Melhorar a Estratégia: Ao backtestar uma estratégia, podemos encontrar maneiras de refiná-la, tornando-a mais lucrativa ou menos arriscada. O processo de backtesting deve seguir o método científico:
        * Começamos com uma hipótese sobre uma oportunidade de arbitragem (baseada em nossa intuição ou em uma pesquisa).
        * Em seguida, confirmamos ou refutamos essa hipótese com um backtest.
        Se os resultados não forem bons, podemos modificar nossa hipótese e repetir o processo.

Alterações simples, como ajustar o período de tempo para calcular a média móvel ou mudar o momento de entrada das ordens, podem melhorar significativamente o desempenho da estratégia.
            """)
# Falta fazer abaixo
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



# Chapter 2 The Basics of Mean Reversion

    elif pagina == "3 . Os Fundamentos da Reversão à Média":
        st.title("3 . Os Fundamentos da Reversão à Média")

        if subsecao == "Introdução":
            st.markdown("""
                        
            A reversão à média é um conceito que está presente em vários aspectos da natureza, mesmo que muitas vezes não percebamos. Esse fenômeno também aparece em ciências sociais. "Exemplo melhor - Daniel Kahneman, por exemplo, citou o famoso caso da "maldição da capa da Sports Illustrated", que afirma que atletas que aparecem na capa da revista têm maior probabilidade de ter um desempenho ruim na temporada seguinte. A explicação científica para isso é que o desempenho de um atleta pode ser visto como algo distribuído ao redor de uma média. Assim, um desempenho excepcional em um ano (que o coloca na capa da revista) provavelmente será seguido por desempenhos mais próximos da média."
                        
            ### A Reversão à Média nos Preços dos Ativos Financeiros

            Será que a reversão à média também acontece nas séries de preços de ativos financeiros? Se fosse tão comum, a vida dos traders seria muito mais fácil e lucrativa. Bastaria comprar um ativo quando seu preço estivesse abaixo da média, esperar a reversão para a média e, em seguida, vender a um preço mais alto, repetindo o processo continuamente. No entanto, a maioria das séries de preços não é reversora à média. Em vez disso, seguem o que chamamos de caminho aleatório geométrico. Enquanto os retornos (e não os preços) tendem a se distribuir ao redor de uma média próxima de zero, não podemos lucrar diretamente com a reversão à média dos retornos.

            É importante não confundir a reversão à média dos retornos com a anticorrelação serial dos retornos, que é negociável. A anticorrelação serial dos retornos é equivalente à reversão à média dos preços, e esse tipo de comportamento dos preços pode, sim, ser explorado.
                        
            ### Testes de Estacionariedade

            Algumas séries de preços que exibem reversão à média são chamadas de séries estacionárias.  Discutiremos os testes estatísticos usados para identificar a estacionariedade de uma série de preços, como o teste ADF, o expoente de Hurst e o teste de razão de variâncias. No entanto, não existem muitos ativos negociados publicamente que possuam séries de preços naturalmente estacionárias.

            Felizmente, podemos criar mais séries de preços estacionárias combinando dois ou mais ativos que, individualmente, não são reversores à média, mas que juntos podem formar um portfólio cujo valor de mercado total seja estacionário. Essas séries de preços são chamadas de cointegradas, e descreveremos os testes estatísticos usados para verificar a cointegração, como o teste CADF e o teste de Johansen. Como resultado desses testes, também podemos determinar as ponderações exatas de cada ativo para criar um portfólio com reversão à média. Isso abre várias oportunidades para traders que buscam lucrar com a reversão à média.
            
            ### Estratégias de Trading Simples para Reversão à Média

            Como exemplo de como é possível lucrar com séries de preços reversoras à média, apresentaremos uma estratégia de trading simples, baseada em um modelo linear. Essa estratégia, notavelmente, é “sem parâmetros,” o que a torna fácil de implementar e testar.
                        
            ### Reversão à Média em Séries Temporais e Seções Cruzadas

            A reversão à média abordada neste capítulo é chamada de reversão à média em séries temporais, onde os preços tendem a reverter à média determinada por seus próprios históricos. Os testes e estratégias de trading descritos neste capítulo são específicos para esse tipo de reversão. Existe, entretanto, outro tipo de reversão à média chamado de reversão à média em seções cruzadas. Nesse caso, os retornos acumulados de um conjunto de ativos tendem a reverter ao retorno acumulado do conjunto. Isso implica que os retornos relativos dos instrumentos são anticorrelacionados em curto prazo. Esse fenômeno ocorre com mais frequência em carteiras de ações.
            """)

        if subsecao == "1. Mean Reversion and Stationarity":
            st.markdown("""
                        
            A reversão à média e a estacionariedade são duas maneiras complementares de analisar o mesmo tipo de série de preços, cada uma com seus respectivos testes estatísticos.

            A descrição matemática de uma série de preços que reverte à média é que a mudança no próximo período é proporcional à diferença entre o preço atual e a média histórica. Isso leva ao teste ADF (Augmented Dickey-Fuller), que testa se podemos rejeitar a hipótese nula de que essa constante de proporcionalidade é zero (ou seja, não há reversão à média).

            Já uma série de preços estacionária é descrita matematicamente como uma série em que a variância dos logs dos preços aumenta mais lentamente do que em um caminho aleatório geométrico (onde a variância aumenta linearmente ao longo do tempo). Essa variação sublinear é geralmente aproximada por uma função do tempo, como τ2Hτ2H, onde ττ é o intervalo de tempo entre duas medições de preços e HH é o expoente de Hurst. Se HH for menor que 0,5, a série é estacionária; se for igual a 0,5, a série é um caminho aleatório. O teste de razão de variâncias é utilizado para verificar se podemos rejeitar a hipótese nula de que o expoente de Hurst é 0,5.

            Vale destacar que a estacionariedade não significa que os preços são necessariamente limitados dentro de um intervalo fixo, com variância independente do tempo (que resultaria em um expoente de Hurst igual a zero). Significa apenas que a variância aumenta de forma mais lenta que a difusão normal.

            Para uma exposição matemática detalhada dos testes ADF e de Razão de Variância, consulte as notas do curso de Walter Beckert (2011). No entanto, nosso foco aqui é a aplicação desses testes em estratégias práticas de trading.

            Esses testes são essenciais para identificar oportunidades de negociação com base na reversão à média, ajudando a distinguir se uma série de preços apresenta características que possam ser exploradas em estratégias de trading quantitativo.
            """)

            st.markdown("""
            ## Augmented Dickey-Fuller Test (ADF)

            Uma série de preços que apresenta **reversão à média** fornece informações sobre o movimento futuro dos preços com base no nível atual. Se o preço estiver acima da média, espera-se uma queda; se estiver abaixo, espera-se uma alta. O **teste ADF (Augmented Dickey-Fuller)** é baseado nessa premissa para determinar se uma série de preços segue um caminho aleatório ou não.

            ### Modelo Linear

            O modelo linear para as mudanças nos preços é descrito pela seguinte equação:
            """)

            st.latex(r"""
            \Delta y(t) = \lambda y(t-1) + \mu + \beta t + \alpha_1 \Delta y(t-1) + \dots + \alpha_k \Delta y(t-k) + \varepsilon_t
            """)

            st.markdown("""
            Onde:
            - \(\Delta y(t) = y(t) - y(t-1)\) representa a variação do preço.
            - \(\lambda\) é o coeficiente que indica a dependência da variação de preço atual em relação ao nível anterior.

            O teste ADF avalia se \(\lambda = 0\), ou seja, se o próximo movimento (\(\Delta y(t)\)) é independente do nível atual (\(y(t-1)\)), o que indicaria que a série de preços segue um caminho aleatório.

            ### Estatística do Teste
            O valor do teste estatístico é dado pela razão:
            """)

            st.latex(r"""
            \frac{\lambda}{SE(\lambda)}
            """)

            st.markdown("""
            Onde \(SE(\lambda)\) é o erro padrão do ajuste de regressão. Se essa razão for significativamente negativa, o teste rejeita a hipótese nula (\(\lambda = 0\)), indicando que a série de preços não segue um caminho aleatório e que há reversão à média.

            ### Interpretação

            Os valores críticos para o teste ADF foram tabulados por Dickey e Fuller, permitindo que os resultados sejam avaliados em diferentes níveis de confiança, como 95%. Para que a hipótese nula seja rejeitada, o valor da estatística \(\frac{\lambda}{SE(\lambda)}\) deve ser negativo e mais extremo do que o valor crítico tabelado.

            Adicionalmente, no contexto de negociação prática, o termo de drift constante (\(\beta\)) pode ser desprezado, pois as flutuações diárias são geralmente maiores que qualquer drift presente.

            ### Exemplo de Aplicação
            **Exemplo 2.1**: A aplicação do teste ADF em uma série de taxas de câmbio, como o par **USD/CAD**, pode ajudar a determinar se a série de preços reverte à média ou segue um caminho aleatório. Isso pode oferecer insights para estratégias de trading baseadas na reversão à média.
            """)

     
            code = '''
            # Importando as bibliotecas necessárias
            import yfinance as yf
            import statsmodels.tsa.stattools as adf_test

            # Passo 1: Baixar dados do par de moedas USD/CAD usando o pacote yfinance.
            # Aqui, escolhemos o intervalo de datas entre 22 de junho de 2007 e 28 de março de 2014.
            df_usdcad = yf.download('USDCAD=X', start="2007-06-22", end="2014-03-28")

            # Passo 2: Aplicação do teste de Dickey-Fuller Aumentado (ADF) na série temporal
            # O teste ADF ajuda a verificar se uma série temporal é estacionária ou não.
            # 'Close' refere-se ao preço de fechamento do par de moedas em cada dia de negociação.
            result = adf_test.adfuller(df_usdcad['Close'])

            # Passo 3: Exibir os resultados do teste ADF
            # result[0] contém o valor da estatística do teste ADF.
            # result[1] contém o valor-p, que indica se a hipótese nula (não estacionariedade) é rejeitada ou não.
            # result[4] contém os valores críticos, usados para comparar a estatística do teste.

            print(f'Testatística ADF: {result[0]}')  # Exibe a estatística ADF calculada
            print(f'Valor-p: {result[1]}')  # Exibe o valor-p do teste
            print(f'Valores Críticos: {result[4]}')  # Exibe os valores críticos para diferentes níveis de confiança

            ====================== Output ============================
                Testatística ADF: -1.8310737300524096
                Valor-p: 0.3651471887306743
                Valores Críticos: {'1%': -3.434120287918905, '5%': -2.8632053717943005, '10%': -2.5676565959447415}

            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            col1, col2 = st.columns(2)
            # Exibir a imagem do primeiro gráfico
            with col1:
                st.image("img/usd_cad_serie.png", caption='Legenda: Este é o gráfico da função seno.', use_column_width=True)

            # Exibir a imagem do segundo gráfico
            with col2:
                st.image("img/ar_series.png", caption='Legenda: Este é o gráfico da função cosseno.', use_column_width=True)




            st.markdown("""
           
            """)

            st.markdown("""
           
            """)

            st.markdown("""
           
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