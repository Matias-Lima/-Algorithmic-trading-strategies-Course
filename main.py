import streamlit as st
# Configuração da página
st.set_page_config(page_title="Guia Conceitual - Algorithmic Trading ", layout="wide")

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
                "Armadilhas Comuns no Backtesting",
                "Significância Estatística do Backtesting: Teste de Hipóteses",
                "Quando não fazer Backtest em uma estratégia",
                "Um Backtest Será Preditivo de Retornos Futuros?"

            ],
            "3 . Os Fundamentos da Reversão à Média": [
                "Introdução",
                "1. Mean Reversion and Stationarity",
                "2. Cointegração",
                "3. Prós e Contras da Reversão a média",
                "4. Resumo"
            ],
            "4 . Estratégias de Reversão à Média": [
                "Introdução",
                "Trading Pairs",
                "Bollinger Bands",
                "Estratégias de Rompimento",
                "Erros nos dados",
                "Conclusão"
            ],
            "5 . Reversão à Média de Ações e ETFs": [
                "Introdução",
                "Trading Pairs",
                "Scalping",
                "Estratégias de Rompimento"
            ],
            "6 . Reversão à Média de Moedas e Futuros": [
                "Introdução",
                "Trading Pairs",
                "Scalping",
                "Futures Intermarket Spreads"
            ],
            "7 . Estratégias de Momentum Interdiário": [
                "Introdução",
                "Tests for Time Series Momentum",
                "Scalping",
                "Futures Intermarket Spreads"
            ],
            "8 . Estratégias de Momentum Intradiário": [
                "Introdução",
                "Trading Pairs",
                "Scalping",
                "Futures Intermarket Spreads"
            ],
            "9 . Gestão de Riscos": [
                "Introdução",
                "Alavancagem",
                "Indicadores e métricas",
                "Conclusão"
            ]
        }
        if pagina_atual in subsecoes:
            return st.sidebar.radio("Subseções", subsecoes[pagina_atual])
        return None
    # Navegação das subseções
    subsecao = mostrar_subsecoes(pagina)

# ====================================================================================

    # ==================== Introdução
     
    if pagina == "1 . Introdução":
        st.title("Introdução ao Algoritmo Trading")
        
        st.markdown(r"""
        Este curso oferece um guia prático sobre estratégias de trading algorítmico que podem ser implementadas tanto por traders individuais quanto institucionais. Diferente de abordagens puramente teóricas, o foco está em estratégias que realmente são usadas no mercado.
                    
        Vamos explorar uma ampla gama de estratégias, divididas em dois grandes grupos: estratégias de reversão à média e estratégias de momentum. Cada categoria será explicada em detalhes, com ênfase tanto nas técnicas padrão de trading quanto nos fundamentos que justificam o funcionamento dessas estratégias.
                    
        ---
        ### Estratégias de Reversão à Média
                    
        No campo das estratégias de reversão à média, cobriremos diversas técnicas estatísticas para detectar a reversão à média em séries temporais. Entre elas estão:

            Teste Dickey-Fuller Aumentado (ADF);
            Exponente de Hurst;
            Teste da Razão de Variância;
            Meia-vida.

        Também discutiremos a cointegração, utilizando testes como:

            Teste Dickey-Fuller Aumentado para Cointegração (CADF);
            Teste de Johansen.

        O foco será explicar de forma intuitiva o que cada um desses testes realmente mede e as equações matemáticas simples por trás deles.

        #### Técnicas de Trading com Reversão à Média

        Abordaremos as técnicas mais simples e eficazes para operar portfólios que seguem a reversão à média, como:
                    
            Linear
            Bandas de Bollinger;
            Filtro de Kalman.

        Discutiremos a melhor forma de usar dados de preços para essas estratégias: preços brutos, logaritmos dos preços ou suas razões. O filtro de Kalman, em especial, será apresentado como uma ferramenta valiosa em diversas estratégias. Também faremos distinção entre reversão à média em séries temporais e reversão à média cross-sectional (entre diferentes ativos).

        #### Exemplos Práticos

        Os exemplos de estratégias de reversão à média incluirão:

            Modelos de ações interdiários e intradiários;
            Pares e triplas de fundos negociados em bolsa (ETFs);
            Spreads de futuros.

        Além disso, vamos discutir como a ascensão dos dark pools e do high-frequency trading tornaram essas estratégias mais desafiadoras nos últimos anos.
                    
        ---           
        ### Estratégias de Momentum

        Por outro lado, as estratégias de momentum são guiadas por quatro principais fatores que impulsionam esse comportamento em ações e futuros. Veremos como extrair momentum a partir de séries temporais e entre diferentes ativos. Novas abordagens, como aquelas baseadas em eventos de notícias, sentimento de mercado, fluxo de ordens e trading de alta frequência, também serão exploradas.
                    
        ---                       
        ### Armadilhas Comuns

        Uma parte importante deste curso será dedicada a discutir as armadilhas comuns que podem fazer com que os resultados do trading ao vivo divergem significativamente dos backtests. Questões como overfitting e viés de sobrevivência serão abordadas.

        """)
             
    # ==================== Introdução

# ====================================================================================

#  ====================  Chapter 1  Backtesting e Execução Automática ==============

    elif pagina == "2 . Backtesting e Execução Automática":
        st.title("Backtesting e Execução Automática")

        if subsecao == "Introdução":
            st.markdown(r"""                      
            Embora o foco deste curso esteja nas categorias específicas de estratégias, é fundamental abordar algumas considerações importantes e armadilhas comuns antes de iniciar o backtesting (teste retroativo). Ignorar essas questões pode tornar o backtest inútil ou, pior, enganoso, resultando em perdas financeiras significativas.

            O backtesting é o processo de testar uma estratégia de trading com dados históricos para avaliar seu desempenho. No entanto, para que esse teste seja válido, é crucial evitar certas armadilhas comuns. Se essas precauções não forem tomadas, o resultado do backtest pode não refletir com precisão o desempenho futuro de uma estratégia.
                                    
            #### Importância da Significância Estatística

            Uma preocupação central no backtesting é a significância estatística dos resultados. Em outras palavras, até que ponto os resultados obtidos durante o teste podem ser considerados estatisticamente confiáveis? Para avaliar isso, utilizamos metodologias de testes de hipótese e simulações de Monte Carlo.

            * Quanto mais operações (trades) de ida e volta forem realizadas no backtest, maior será a confiabilidade estatística.
            * Mesmo que o backtest seja conduzido corretamente e com alta significância estatística, isso não garante que os retornos futuros serão previsíveis.

            #### Mudanças de Regime

            Outro fator importante são as mudanças de regime no mercado. Mesmo uma estratégia que tenha funcionado bem no passado pode ser completamente ineficaz no futuro devido a alterações nas condições de mercado. No curso, vamos discutir alguns exemplos históricos em que essas mudanças de regime prejudicaram estratégias previamente bem-sucedidas.
                                    
            #### Escolha da Plataforma de Software

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

        elif subsecao == "Armadilhas Comuns no Backtesting":
            
            st.markdown(r"""
            ### Common Pitfalls of Backtesting

            #### Look-ahead Bias
            Look-ahead bias ocorre quando o programa de backtesting utiliza informações futuras, como os preços de amanhã, para determinar os sinais de negociação de hoje. Um exemplo comum é usar o preço máximo ou mínimo de um dia para definir um sinal de entrada no mesmo dia durante o backtesting, algo impossível de saber antes do fechamento do mercado. Esse viés é essencialmente um erro de programação, afetando apenas o backtesting, pois programas de negociação ao vivo não têm acesso a informações futuras.

            Uma forma eficaz de evitar esse viés é garantir que o programa utilizado para backtesting e negociação ao vivo seja o mesmo, mudando apenas o tipo de dado fornecido (histórico para backtesting e dados ao vivo para negociação). Algumas plataformas permitem essa abordagem, e serão discutidas mais adiante no capítulo.
                        
            ---                               
            """)

            st.markdown("""
                ### Data-Snooping Bias and the Beauty of Linearity

                ##### Data-Snooping Bias
                Data-snooping bias ocorre quando muitos parâmetros livres são ajustados a padrões de mercado aleatórios do passado, gerando uma performance histórica ilusória e com pouca capacidade preditiva. Para evitar isso, deve-se testar o modelo em dados fora da amostra. Porém, ajustes excessivos nos modelos podem transformar os dados fora da amostra em dados ajustados.

                Uma alternativa é utilizar validação cruzada, dividindo os dados em vários subconjuntos para treinamento e validação. Modelos com alta simplicidade, poucas regras e menor número de parâmetros têm menor risco de viés. Modelos lineares geralmente são preferíveis a modelos não-lineares, pois estes últimos são mais complexos e mais suscetíveis ao viés.

                ##### O Papel dos Modelos Lineares
                Modelos lineares oferecem previsões mais simples e robustas. Por exemplo, fórmulas de capital alocadas linearmente, como no modelo Ornstein-Uhlenbeck, permitem estratégias como “scaling-in” para explorar séries de preços com reversão à média. Exemplos práticos incluem estratégias lineares de arbitragem estatística em ações.

                Um exemplo extremo de modelo linear é aquele com pesos iguais atribuídos a fatores preditivos. Normalizando esses fatores em Z-scores e combinando-os, pode-se prever retornos futuros ou, pelo menos, ranquear ativos de forma eficiente. Estratégias baseadas em rankings, como a "magic formula" de Joel Greenblatt, podem gerar retornos superiores ao mercado.

                Mesmo com precauções, o viés de data-snooping pode infiltrar-se. Por isso, testes finais devem incluir walk-forward testing com operações reais em pequena escala. Um bom resultado em negociação ao vivo é alcançar ao menos metade do Sharpe ratio obtido no backtesting.
                """)
            
            st.divider()
            st.markdown("""
                ### Stock Splits and Dividend Adjustments

                Quando uma empresa realiza um desdobramento de ações (stock split) no formato N-para-1, o preço das ações é dividido por N. Contudo, o número de ações possuídas pelo investidor aumenta proporcionalmente, mantendo o valor total do mercado inalterado. No entanto, durante o backtesting, geralmente analisamos apenas a série de preços, e sem ajustes para refletir o desdobramento, pode ocorrer uma queda abrupta no preço na data de vigência, gerando sinais de negociação incorretos.

                Para corrigir esse problema, é necessário ajustar os preços históricos dividindo-os por N antes da data de vigência. Essa prática também se aplica ao vivo, ajustando os dados históricos antes da abertura do mercado na data relevante. Em casos de agrupamento reverso de ações (reverse split), os preços anteriores devem ser multiplicados por N.

                Da mesma forma, quando uma empresa paga dividendos, o preço das ações tende a cair pelo valor do dividendo (ausentes outros movimentos de mercado). Novamente, isso pode causar falsos sinais de negociação se os preços históricos não forem ajustados. Antes da data de pagamento do dividendo, deve-se subtrair o valor do dividendo dos preços históricos para refletir com precisão as mudanças no mercado.

                Esses ajustes também são essenciais para ETFs (fundos negociados em bolsa), embora opções possam exigir métodos mais complexos. Fontes confiáveis, como o site earnings.com, oferecem informações históricas sobre splits e dividendos, permitindo antecipar esses eventos em sistemas de negociação automatizados. Alternativamente, serviços como csidata.com fornecem dados históricos já ajustados para splits e dividendos.
                """)

            st.divider()
            st.markdown("""
                ### Survivorship Bias in Stock Database

                O viés de sobrevivência ocorre quando dados históricos utilizados para backtesting incluem apenas ações que ainda existem, excluindo aquelas que foram deslistadas, geralmente devido à falência. Isso pode gerar resultados distorcidos e excessivamente otimistas.  

                Por exemplo, uma estratégia que compra ações com quedas acentuadas pode parecer lucrativa em um backtest porque inclui apenas empresas que se recuperaram, ignorando as que faliram. Esse viés afeta principalmente estratégias long-only de reversão à média, que dependem de comprar ações depreciadas e vendê-las após a recuperação. Para estratégias short-only, o impacto é oposto: ações que faliram e não aparecem nos dados teriam contribuído positivamente para o retorno.

                Estratégias de momentum, por outro lado, são menos impactadas, pois o viés tende a reduzir os retornos short e aumentar os long, resultando em um efeito compensatório parcial.

                ##### Como Evitar o Viés de Sobrevivência
                1. **Dados Livres de Viés**: Utilize bases de dados que incluam ações deslistadas, como as oferecidas por csidata.com, kibot.com e tickdata.com. Essas bases geralmente listam ações deslistadas e evitam o viés de sobrevivência.
                
                2. **Coleta Própria**: Outra abordagem é armazenar os preços históricos de todas as ações de um índice diariamente, permitindo recriar um histórico livre de viés.

                3. **Backtests Recentes**: Se não for possível acessar dados completos, limite o backtesting aos últimos anos, pois o viés de sobrevivência é menos significativo em períodos curtos.

                Lembre-se de que a precisão dos dados é crucial para estratégias realistas e que resultados inflados devido ao viés de sobrevivência podem levar a decisões de investimento ruins.
            """)

            st.divider()
            st.markdown("""
                ### Primary versus Consolidated Stock Prices**

                Nos mercados de ações dos EUA, as negociações podem ocorrer em múltiplas plataformas, como NYSE, Nasdaq, ECNs e dark pools. Os preços históricos geralmente refletem dados consolidados, ou seja, a soma de todas essas plataformas. Contudo, estratégias que dependem de ordens de mercado no fechamento (MOC) ou na abertura (MOO) devem considerar apenas os preços da bolsa primária.

                ##### Problemas com Preços Consolidados
                1. **Diferenças entre Consolidados e Primários**: Preços consolidados podem incluir negociações atípicas realizadas em volumes baixos ou em horários diferentes dos leilões de abertura/fechamento da bolsa primária. Isso pode distorcer os dados e inflar artificialmente os resultados de backtesting.

                2. **Efeito em Estratégias de Reversão à Média**: O uso de preços consolidados pode superestimar os retornos de estratégias de reversão à média. Por exemplo, um preço atípico fora da bolsa primária pode parecer uma oportunidade de compra, mas não seria acessível no mercado real.

                ##### Soluções
                - **Utilizar Dados da Bolsa Primária**: Estratégias dependentes de MOC ou MOO devem basear-se nos preços históricos das bolsas primárias. Esses preços são mais representativos das condições reais de mercado.
                - **Cuidado com Altos e Baixos Consolidados**: Valores consolidados de máximas e mínimas frequentemente resultam de negociações esporádicas em mercados secundários, tornando-os inadequados para estratégias baseadas nesses indicadores.

                ##### Fontes de Dados
                - Assinaturas do Bloomberg oferecem acesso a preços históricos das bolsas primárias.
                - Alternativamente, é possível coletar dados ao vivo diretamente das bolsas e armazená-los em bases de dados personalizadas. Isso garante precisão e elimina a dependência de consolidados.

                Estratégias eficazes dependem da escolha correta dos dados. Preços consolidados podem ser úteis para algumas análises, mas estratégias específicas exigem a precisão dos preços da bolsa primária para garantir resultados realistas.
                """)

            st.divider()
            st.markdown(r"""
                ### Short-Sale Constraints

                Modelos de negociação que envolvem vendas a descoberto enfrentam restrições significativas, tornando a execução prática mais complexa do que o sugerido pelos backtests. Para realizar uma venda a descoberto, o corretor precisa localizar ações disponíveis para empréstimo, geralmente de instituições ou investidores com posições longas. Quando há grande interesse em shorting ou quando o float da ação é limitado, as ações tornam-se "difíceis de emprestar" (hard to borrow). Isso pode gerar custos adicionais, como juros pagos ao locador, ou até a impossibilidade de executar a venda.  

                Essas limitações foram exacerbadas durante a crise de 2008-2009, quando a SEC proibiu vendas a descoberto de ações financeiras por meses, criando retornos irreais em backtests de estratégias que shortavam ações indisponíveis. As ações de baixa capitalização (small caps) são mais afetadas por essas restrições do que as de grande capitalização (large caps), e até ETFs, como o SPY, podem ser difíceis de emprestar em momentos de estresse.

                Outra limitação é a **regra do uptick**, que esteve em vigor de 1938 a 2007 e foi substituída pela Alternative Uptick Rule em 2010. Esta regra exige que vendas a descoberto só sejam executadas acima do melhor preço de oferta nacional em mercados que sofreram quedas superiores a 10%. Isso limita ainda mais as ordens de mercado de venda a descoberto.

                Para backtests precisos, é crucial considerar se as ações eram emprestáveis ou se as regras do uptick estavam em vigor no período analisado. Ignorar essas restrições pode inflar artificialmente os resultados, comprometendo a validade dos modelos.
                """)

            st.divider()
            st.markdown(r"""
                ### **Futures Continuous Contracts**

                Contratos futuros possuem datas de vencimento, o que torna uma estratégia de trading focada em contratos futuros, como de petróleo bruto, uma combinação de várias operações em contratos diferentes. O momento de "rollover" (substituir o contrato próximo ao vencimento por um com prazo maior) pode variar: alguns preferem rolar contratos dias antes do vencimento, enquanto outros esperam por eventos como o cruzamento de interesse em aberto. Embora o rollover seja essencial, ele não contribui significativamente para os lucros, exceto pelo efeito do retorno de rolagem, discutido no Capítulo 5.

                ##### Dados de Contratos Contínuos
                A maioria dos fornecedores de dados históricos de futuros oferece séries ajustadas de contratos contínuos, que unem preços de contratos consecutivos. No entanto, essas séries podem introduzir problemas, como lacunas de preço em datas de rollover, resultando em cálculos incorretos de lucro e retorno. Para corrigir:
                1. **Ajuste de Preço**: Elimina lacunas ajustando os preços históricos para refletir mudanças entre contratos.
                2. **Ajuste de Retorno**: Garante que cálculos de retorno estejam corretos, mas pode comprometer os de lucro.

                Infelizmente, ajustar preços para lucros corretos pode tornar os cálculos de retorno imprecisos, e vice-versa. Isso obriga o trader a escolher entre priorizar lucro ou retorno no backtest.

                ##### Considerações sobre Ajustes
                1. **Preços Negativos**: O ajuste de preços pode gerar valores negativos em séries históricas distantes. Para mitigar, adiciona-se uma constante positiva a todos os preços.  
                2. **Estratégias de Spreads**: Para estratégias baseadas em diferenças de preço, o ajuste de preço é essencial para evitar sinais errados devido a erros de rollover. Já para estratégias baseadas em proporções de preços, o ajuste de retorno é mais adequado.

                A escolha do fornecedor de dados é crítica. Alguns, como csidata.com, ajustam apenas preços com a opção de evitar preços negativos. Outros, como tickdata.com, permitem escolher entre ajuste de preço ou retorno, mas não evitam preços negativos. Compreender como os ajustes são aplicados é essencial para garantir a precisão e a relevância do backtest.
                """)

            st.divider()
            st.markdown("""
                ### Futures Close versus Settlement Prices**

                Os preços de fechamento diário fornecidos por provedores de dados de contratos futuros geralmente correspondem ao preço de liquidação ("settlement price") determinado pela bolsa, e não ao último preço negociado do dia. Mesmo em dias sem transações, os contratos futuros têm um preço de liquidação definido. 

                ##### Escolha do Preço para Backtests
                - **Preço de Liquidação**: É geralmente preferido, pois reflete melhor os preços próximos ao fechamento real das negociações, especialmente útil em estratégias como pares de futuros. Ele garante que os spreads sejam calculados com preços contemporâneos, desde que os contratos compartilhem o mesmo horário de fechamento.
                - **Último Preço Negociado**: Pode ser enganoso, especialmente se a última transação ocorreu muito antes do fechamento, tornando-o inadequado para estratégias que dependem de spreads, como arbitragem.

                ##### Estratégias Intraday e Spreads
                1. **Dados Intraday**: Para estratégias intraday ou spreads mais sensíveis, é necessário usar dados intraday detalhados com cotações bid-ask ou diretamente os spreads nativos da bolsa. 
                2. **Sincronização de Preços**: Últimos preços de contratos futuros ilíquidos podem não ser contemporâneos, criando spreads irreais que inflacionam os retornos de backtest. Isso é especialmente importante ao negociar contratos com baixa liquidez.

                ##### Considerações para Spreads Intermercados
                - **Horários de Fechamento Diferentes**: Contratos negociados em bolsas distintas podem ter horários de fechamento divergentes, resultando em spreads incorretos.
                - **Alternativas**: Para evitar problemas de sincronização, considere negociar ETFs que refletem futuros. Por exemplo, negocie GLD contra GDX em vez de GC contra GDX, já que ambos compartilham o mesmo horário de fechamento na Arca (4:00 p.m. ET).

                Escolher os dados certos (preço de liquidação, bid-ask intraday ou spreads nativos) é crucial para evitar resultados inflacionados e obter backtests mais realistas. A atenção à sincronização e à liquidez garante uma maior precisão nas estratégias baseadas em futuros.
                """)

        elif subsecao == "Significância Estatística do Backtesting: Teste de Hipóteses":
            st.markdown("""
                ### **Significância Estatística do Backtesting: Teste de Hipóteses**

                Backtests enfrentam o problema de amostras finitas, onde métricas como retornos médios ou drawdowns podem ser influenciadas por sorte. Para lidar com isso, utiliza-se o teste de hipótese, uma metodologia estatística que avalia a significância dos resultados obtidos.

                ##### Passos do Teste de Hipótese
                1. **Cálculo do Teste Estatístico**: Usamos métricas como o retorno médio diário como o teste estatístico do backtest.
                2. **Hipótese Nula**: Supomos que o retorno médio verdadeiro seja zero para a população infinita de dados.
                3. **Distribuição de Probabilidade**: Determinamos a distribuição dos retornos sob a hipótese nula, frequentemente assumindo uma distribuição normal.
                4. **Cálculo do p-valor**: Avaliamos a probabilidade de obter resultados tão extremos quanto os observados no backtest, dada a hipótese nula. Se o p-valor for pequeno (ex.: < 0,01), rejeitamos a hipótese nula, indicando que os resultados são estatisticamente significativos.

                ##### Métodos para Estimar a Distribuição Nula
                1. **Método Paramétrico**: Assume-se uma distribuição normal para os retornos, com média zero e desvio padrão baseado nos dados amostrais. O índice Sharpe, ajustado pela raiz quadrada do número de dias, é usado para determinar significância com base em valores críticos.
                2. **Método Monte Carlo**: Gera séries de preços simuladas com as mesmas características estatísticas da série real. A estratégia é aplicada a essas séries simuladas, avaliando a frequência em que o retorno médio supera o retorno do backtest.
                3. **Método de Simulação de Trades**: Cria conjuntos simulados de negociações com o mesmo número e período médio de manutenção que no backtest, mas distribuídos aleatoriamente nos preços reais. Avalia a proporção de retornos que excedem o resultado do backtest.

                ##### Limitações do Teste de Hipótese
                O teste de hipótese apresenta limitações, como:
                - **Dependência da Hipótese Nula**: Resultados variam dependendo da definição da hipótese nula, tornando os testes sensíveis às escolhas iniciais.
                - **Probabilidade Condicional**: Os testes avaliam a probabilidade do resultado dado que a hipótese nula é verdadeira, mas não o inverso (probabilidade da hipótese nula ser verdadeira dado o resultado).

                Mesmo com limitações, a falha em rejeitar a hipótese nula pode gerar insights valiosos. Por exemplo, distribuições com alta curtose podem ser favoráveis a estratégias de momentum, indicando padrões ocultos no mercado.

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
                st.image("img/h_test.png", caption='Legenda: Este é o gráfico da distribuição dos valores.', use_column_width=True)

                st.image("img/h_test2.jpg", caption='Legenda: Este é o gráfico da distribuição dos valores.', use_column_width=True)
            # Exibir a imagem do segundo gráfico
            with col2:
                print("")
           
        elif subsecao == "Quando não fazer Backtest em uma estratégia":

            st.markdown(r"""
            ### Quando não fazer Backtest em uma estratégia

            Embora o backtesting seja essencial para avaliar estratégias de trading, nem todas as estratégias merecem ser testadas. Algumas possuem falhas tão óbvias que investir tempo nelas é inútil. A seguir, são apresentados exemplos de estratégias que não devem ser testadas:

            ##### Exemplo 1: Alta Retorno, Baixo Sharpe Ratio  
            Uma estratégia com retorno anualizado de 30%, Sharpe ratio de 0.3 e duração máxima de drawdown de dois anos.  
            - **Problemas**: A baixa consistência (Sharpe ratio baixo) e o longo período de drawdown tornam a estratégia insustentável para a maioria dos traders.  
            - **Conclusão**: Provavelmente é um caso de viés de data-snooping, com pouca chance de sucesso em validação cruzada. Estratégias com altos retornos, mas baixo Sharpe ratio, geralmente não valem o teste.

            ##### Exemplo 2: Estratégia Long-only em Petróleo  
            Uma estratégia que gerou 20% de retorno em 2007, com Sharpe ratio de 1.5.  
            - **Problemas**: O retorno do buy-and-hold no petróleo bruto foi de 47% no mesmo ano, com Sharpe ratio de 1.7.  
            - **Conclusão**: A estratégia não é superior ao benchmark apropriado (buy-and-hold). Sempre compare estratégias com benchmarks relevantes.

            ##### Exemplo 3: "Buy-Low-Sell-High"  
            Escolhe as 10 ações mais baratas no início do ano e as mantém por 12 meses, gerando 388% de retorno em 2001.  
            - **Problemas**: Estratégias como essa frequentemente utilizam bancos de dados com viés de sobrevivência, ignorando ações deslistadas. Isso infla os retornos, tornando-os irreais.  
            - **Conclusão**: Se os dados não incluem ações deslistadas, o resultado é suspeito e irrealizável.

            ##### Exemplo 4: Modelo de Redes Neurais com 100 Nós  
            Um modelo de redes neurais com 100 nós gera Sharpe ratio de 6 no backtest.  
            - **Problemas**: Redes neurais com muitos nós têm centenas de parâmetros ajustáveis, permitindo ajustes perfeitos em séries históricas, mas com pouco ou nenhum poder preditivo devido ao viés de data-snooping.  
            - **Conclusão**: Estratégias com modelos excessivamente complexos não devem ser levadas a sério sem justificativas sólidas.

            ##### Exemplo 5: Estratégia de Alta Frequência no E-mini S&P 500  
            Uma estratégia de alta frequência com retorno médio anual de 200%, Sharpe ratio de 6 e período médio de manutenção de 50 segundos.  
            - **Problemas**: A lucratividade depende da estrutura do mercado, do tipo de ordem e da reação de outros participantes, fatores que o backtest não consegue replicar adequadamente.  
            - **Conclusão**: Backtests de estratégias de alta frequência frequentemente falham em capturar a dinâmica do mercado real e devem ser tratados com ceticismo.

            #### Conclusão  
            Nem toda estratégia vale o esforço do backtesting. Reconhecer falhas óbvias economiza tempo e evita falsas expectativas. Use benchmarks adequados, evite viés de sobrevivência, e desconfie de estratégias com complexidade excessiva ou resultados surpreendentes sem justificativa sólida.
            """)

        elif subsecao == "Um Backtest Será Preditivo de Retornos Futuros?":

            st.markdown(r"""
            ### **Um Backtest Será Preditivo de Retornos Futuros?**

            Mesmo evitando erros comuns no backtesting e garantindo significância estatística, a capacidade de prever retornos futuros depende de uma suposição central: que as propriedades estatísticas da série de preços permanecerão inalteradas. Na prática, essa suposição frequentemente é violada devido a mudanças econômicas, gerenciais ou estruturais nos mercados financeiros.  

            ##### Exemplos de Mudanças de Regime nos EUA
            1. **Decimalização (2001)**: A mudança para cotações decimais em ações dos EUA reduziu os spreads bid-ask, mas também diminuiu a liquidez exibida nos melhores preços. Isso reduziu a lucratividade de estratégias de arbitragem estatística, enquanto aumentou a de estratégias de alta frequência.
            
            2. **Crise Financeira de 2008**: 
            - Colapso de 50% nos volumes diários de negociação, afetando especialmente o varejo.
            - Redução na volatilidade média dos mercados, mas aumento na frequência de eventos extremos, como o flash crash (2010) e o rebaixamento da dívida dos EUA (2011). Esses fatores prejudicaram estratégias de reversão à média.
            - Início de um mercado de baixa para estratégias de momentum, que se estendeu por vários anos.

            3. **Regulação NMS (2007)**: Implementada pela SEC, contribuiu para a drástica redução nos tamanhos médios de negociações e a obsolescência de operações de blocos na NYSE.

            4. **Mudanças na Regra de Uptick para Vendas a Descoberto**: A remoção da antiga regra de uptick (2007) e sua substituição pela Alternative Uptick Rule (2010) afetaram estratégias que dependiam dessas regulamentações.

            ##### Impacto das Mudanças
            Estratégias que foram altamente lucrativas antes dessas mudanças podem tornar-se obsoletas ou menos eficazes. Backtests com dados anteriores a essas mudanças ("shifts de regime") podem não refletir condições futuras. Mesmo dados recentes podem ser enganosos se novas mudanças ocorrerem.

            #### Conclusão
            O trading algorítmico vai além de algoritmos, programação e matemática. É essencial considerar fatores econômicos e estruturais para avaliar se um backtest é preditivo e se sua eficácia pode ser mantida em condições futuras. Consciência dessas questões ajuda a mitigar o risco de confiar excessivamente em modelos baseados em dados históricos que podem não se repetir.
            """)


#  ====================  Chapter 1  Backtesting e Execução Automática ===============

# ====================================================================================


# ====================== Chapter 2 The Basics of Mean Reversion ===============

    elif pagina == "3 . Os Fundamentos da Reversão à Média":
        st.title("3 . Os Fundamentos da Reversão à Média")


# ==================== Introdução ========================

        if subsecao == "Introdução":
            st.markdown("""
                        
            A reversão à média é um conceito que está presente em vários aspectos da natureza, mesmo que muitas vezes não percebamos. Esse fenômeno também aparece em ciências sociais. "Exemplo melhor - Daniel Kahneman, por exemplo, citou o famoso caso da "maldição da capa da Sports Illustrated", que afirma que atletas que aparecem na capa da revista têm maior probabilidade de ter um desempenho ruim na temporada seguinte. A explicação científica para isso é que o desempenho de um atleta pode ser visto como algo distribuído ao redor de uma média. Assim, um desempenho excepcional em um ano (que o coloca na capa da revista) provavelmente será seguido por desempenhos mais próximos da média."
                        
            ### A Reversão à Média nos Preços dos Ativos Financeiros

            Será que a reversão à média também acontece nas séries de preços de ativos financeiros? Se fosse tão comum, a vida dos traders seria muito mais fácil e lucrativa. Bastaria comprar um ativo quando seu preço estivesse abaixo da média, esperar a reversão para a média e, em seguida, vender a um preço mais alto, repetindo o processo continuamente. No entanto, a maioria das séries de preços não é reversora à média. Em vez disso, seguem o que chamamos de passeio aleatório . Enquanto os retornos (e não os preços) tendem a se distribuir ao redor de uma média próxima de zero, não podemos lucrar diretamente com a reversão à média dos retornos.

            É importante não confundir a reversão à média dos retornos com a anticorrelação serial dos retornos, que é negociável. A anticorrelação serial dos retornos é equivalente à reversão à média dos preços, e esse tipo de comportamento dos preços pode, sim, ser explorado.
                        
            ### Testes de Estacionariedade

            Algumas séries de preços que exibem reversão à média são chamadas de séries estacionárias.  Discutiremos os testes estatísticos usados para identificar a estacionariedade de uma série de preços, como o teste ADF, o expoente de Hurst e o teste de razão de variâncias. No entanto, não existem muitos ativos negociados publicamente que possuam séries de preços naturalmente estacionárias.

            Felizmente, podemos criar mais séries de preços estacionárias combinando dois ou mais ativos que, individualmente, não são reversores à média, mas que juntos podem formar um portfólio cujo valor de mercado total seja estacionário. Essas séries de preços são chamadas de cointegradas, e descreveremos os testes estatísticos usados para verificar a cointegração, como o teste CADF e o teste de Johansen. Como resultado desses testes, também podemos determinar as ponderações exatas de cada ativo para criar um portfólio com reversão à média. Isso abre várias oportunidades para traders que buscam lucrar com a reversão à média.
            
            """)

# ==================== Introdução ========================


# ==================== Mean Reversion ========================

        if subsecao == "1. Mean Reversion and Stationarity":
# ----------------------------------------------  

            latext = r'''
            A reversão à média e a estacionariedade são duas maneiras complementares de analisar o mesmo tipo de série de preços, cada uma com seus respectivos testes estatísticos.

            A descrição matemática de uma série de preços que reverte à média é que a mudança no próximo período é proporcional à diferença entre o preço atual e a média histórica. Isso leva ao teste ADF (Augmented Dickey-Fuller), que testa se podemos rejeitar a hipótese nula de que essa constante de proporcionalidade é zero (ou seja, não há reversão à média).

            Já uma série de preços estacionária é descrita matematicamente como uma série em que a variância dos logs dos preços aumenta mais lentamente do que em um caminho aleatório geométrico (onde a variância aumenta linearmente ao longo do tempo). Essa variação sublinear é geralmente aproximada por uma função do tempo, como $\tau^{2H}$, onde $\tau$ é o intervalo de tempo entre duas medições de preços e $H$ é o expoente de Hurst. Se $H$ for menor que 0,5, a série é estacionária; se for igual a 0,5, a série é um caminho aleatório. O teste de razão de variâncias é utilizado para verificar se podemos rejeitar a hipótese nula de que o expoente de Hurst é 0,5.

            Vale destacar que a estacionariedade não significa que os preços são necessariamente limitados dentro de um intervalo fixo, com variância independente do tempo (que resultaria em um expoente de Hurst igual a zero). Significa apenas que a variância aumenta de forma mais lenta que a difusão normal.

            Esses testes são essenciais para identificar oportunidades de negociação com base na reversão à média, ajudando a distinguir se uma série de preços apresenta características que possam ser exploradas em estratégias de trading quantitativo.
            '''
            st.write(latext)

            st.divider()
            latext = r'''
            ### Augmented Dickey-Fuller Test (ADF)

            A série de preços que apresenta reversão à média fornece informações sobre o movimento futuro dos preços com base no nível atual. Se o preço estiver acima da média, é esperado que haja um movimento de queda; se estiver abaixo da média, um movimento de alta. O teste ADF (Augmented Dickey-Fuller) se baseia nessa premissa para determinar se uma série de preços é ou não um passeio aleatório.

            O modelo linear para as mudanças nos preços é descrito pela seguinte equação:
            $$
            \Delta y(t) = \lambda y(t-1) + \mu + \beta t + \alpha_1 \Delta y(t-1) + \dots + \alpha_k \Delta y(t-k) + \epsilon_t
            $$

            Onde:

            - $\Delta y(t) = y(t) - y(t-1)$, representando a variação do preço.
            - $\lambda$ é o coeficiente que indica se há dependência da variação de preço atual com o nível anterior.
            - O teste ADF avalia se $\lambda = 0$, ou seja, se o próximo movimento $\Delta y(t)$ é independente do nível atual $y(t-1)$, indicando um caminho aleatório.

            O valor do teste estatístico é dado pela razão:
            $$
            \frac{\lambda}{SE(\lambda)}
            $$
            onde $SE(\lambda)$ é o erro padrão do ajuste de regressão. Se essa razão for significativamente negativa, o teste rejeita a hipótese nula de $\lambda = 0$, indicando que a série de preços não segue um caminho aleatório e que há reversão à média.

            A tabulação de valores críticos para esse teste foi feita por Dickey e Fuller, permitindo que os resultados sejam avaliados em níveis de confiança como 95%. Para que a hipótese nula seja rejeitada, o valor de $\frac{\lambda}{SE(\lambda)}$ deve ser negativo e mais negativo do que o valor crítico tabelado.

            **Exemplo 2.1**: Aplicação do teste ADF em uma série de taxas de câmbio, como o par USD/CAD, pode ajudar a determinar se a série de preços reverte à média ou se segue um caminho aleatório, oferecendo insights para estratégias de trading baseadas na reversão à média.
            '''
            st.write(latext)

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
                st.write("Explicação da tabela e mais alguns pontos a serem adicionados")

# ----------------------------------------------  

            st.divider()

            latext = r'''
            ### Hurst Exponent and Variance Ratio Test

            O exponente de Hurst e o Teste de Razão de Variância são ferramentas importantes para caracterizar o comportamento de séries temporais financeiras, especialmente em relação à sua tendência de reversão à média ou de passeio aleatório.

            ### Exponente de Hurst

            Intuitivamente, uma série de preços "estacionária" significa que os preços se difundem a partir de seu valor inicial de forma mais lenta do que em um passeio aleatório geométrico. Isso pode ser descrito pela equação de variância:

            $$
            \text{Var}(\tau) = \langle |z(t+\tau) - z(t)|^2 \rangle
            $$

            Onde $z$ são os logaritmos dos preços $y$, $\tau$ é o intervalo de tempo, e $\langle ... \rangle$ denota uma média sobre todos os $t$. Para um passeio aleatório geométrico, a relação é aproximadamente linear:

            $$
            \langle |z(t+\tau) - z(t)|^2 \rangle \sim \tau
            $$

            No entanto, para séries de preços que são revertidas à média ou têm tendência, essa relação muda para:

            $$
            \langle |z(t+\tau) - z(t)|^2 \rangle \sim \tau^{2H}
            $$

            Aqui, $H$ é o exponente de Hurst, onde:

            - $H = 0,5$ indica um passeio aleatório geométrico.
            - $H < 0,5$ indica uma série de preços revertendo à média.
            - $H > 0,5$ indica uma série de preços com tendência.

            Quanto mais próximo de 0 o valor de $H$, mais forte é a reversão à média. Um valor de $H$ mais próximo de 1 indica uma forte tendência. No **Exemplo 2.2**, ao calcular o exponente de Hurst para o par USD/CAD, o valor de $H = 0,46$ foi obtido, sugerindo uma fraca reversão à média.
            '''
            st.write(latext)

            code_2 = '''

            # Importação de bibliotecas necessárias
            import numpy as np  # Para operações matemáticas e manipulação de arrays
            import yfinance as yf  # Para download de dados financeiros

            # Função para calcular o coeficiente de Hurst
            def hurst_stat(ts, lags=100):

            # Define o intervalo de defasagens para calcular a variância
            rng = range(2, lags)
            
            # Converte a série temporal em logaritmo natural
            ts = np.log(ts)
            
            # Calcula a variância entre os valores com a defasagem especificada
            tau = [np.var(np.subtract(ts[lag:], ts[:-lag])) for lag in rng]
            
            # Ajusta uma linha reta (usando a regressão linear) na escala log-log
            poly = np.polyfit(np.log(rng), np.log(tau), 1)
            
            # Retorna o coeficiente de Hurst, que é o coeficiente angular da reta dividido por 2
            return poly[0] / 2

            # Download de dados históricos do par de moedas USD/CAD usando o Yahoo Finance
            df = yf.download('USDCAD=X', start="2007-06-22", end="2014-03-28")

            # Calcula o coeficiente de Hurst para o fechamento ajustado (Adj Close) da série temporal
            hurst = hurst_stat(df["Adj Close"].dropna().values)

            # Imprime o resultado do coeficiente de Hurst
            print(f"Hurst Coefficient: {hurst}")

            ====================== Output ============================

            Hurst Coefficient: 0.4627476687591544

            '''
            st.code(code_2, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

# ----------------------------------------------  

            st.divider()
            st.write(r"""
            ### Teste de Razão de Variância

            Como o cálculo do exponente de Hurst pode ser sensível ao tamanho da amostra, o Teste de Razão de Variância fornece uma hipótese formal para verificar se a série segue um passeio aleatório. O teste compara a variância de diferentes intervalos de tempo para avaliar se a variância cresce de forma proporcional ao tempo, o que seria esperado em um passeio aleatório. A equação do teste é:

            $$
            \frac{\text{Var}(z(t) - z(t-\tau))}{\text{Var}(z(t-1) - z(t-\tau-1))} = 1
            $$

            No **Exemplo 2.3**, ao aplicar o teste à série USD/CAD, o valor de $p = 0,367$ foi obtido, indicando que há uma probabilidade de 37% de que a série seja um passeio aleatório. Como o valor de $p$ é maior que 10%, a hipótese nula (de que a série é um passeio aleatório) não pode ser rejeitada.

            Esses testes, portanto, fornecem informações importantes sobre a natureza da série de preços e se podem ser explorados para estratégias de negociação baseadas na reversão à média ou em tendências.
            """)


            code_3 = '''
            # Importação da função VarianceRatio da biblioteca arch para realizar o teste de razão de variância
            from arch.unitroot import VarianceRatio

            # Aplicação do teste de Razão de Variância sobre a coluna 'close' do dataframe df, com defasagem (lag) de 5 períodos
            vr = VarianceRatio(df['close'], 5)

            # Exibição do sumário dos resultados do teste em formato de texto
            print(vr.summary().as_text())
            '''
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")
            
# ----------------------------------------------  
            
            st.divider()
            st.write(r"""
            ### Half-Life da Reversão à Média

            Os testes estatísticos para reversão à média ou estacionaridade são rigorosos, exigindo uma certeza mínima de 90%. No entanto, em trading prático, muitas vezes podemos ser rentáveis com um grau de certeza menor. Nesta seção, vamos explorar uma interpretação alternativa do coeficiente λ na Equação 2.1, o que nos ajuda a entender se seu valor negativo é suficiente para tornar uma estratégia de trading prática, mesmo sem rejeitar a hipótese nula de que seu valor real é zero com 90% de certeza no teste ADF.

            Esse coeficiente, λ, é uma medida do tempo que um preço leva para reverter à média. Para entender essa nova interpretação, podemos transformar a série temporal discreta da Equação 2.1 para uma forma diferencial, onde as variações nos preços são consideradas infinitesimais. Se ignorarmos o drift (βt) e as diferenças defasadas (Δy(t − 1), …, Δy(t − k)) na Equação 2.1, ela se assemelha à fórmula de Ornstein-Uhlenbeck, usada em cálculos estocásticos para descrever processos reversores à média:

            \[
            dy(t) = (λy(t − 1) + μ)dt + dε
            \]

            onde \( dε \) representa algum ruído Gaussiano. Na forma discreta, obtemos λ por meio de uma regressão linear de Δy(t) contra y(t − 1). Esse valor de λ é mantido na forma diferencial, mas a vantagem de expressá-la assim é que obtemos uma solução analítica para o valor esperado de y(t):

            \[
            E(y(t)) = y_0 e^{λt} - \frac{μ}{λ}(1 - e^{λt})
            \]

            Sabendo que λ é negativo em um processo reversor à média, essa expressão indica que o valor esperado do preço decai exponencialmente para \(- \frac{μ}{λ}\) com uma meia-vida igual a \(-\frac{\log(2)}{λ}\).

            #### Interpretações Úteis do Coeficiente λ para Traders

            1. **Sinal de λ**: Se λ for positivo, isso significa que a série de preços não é reversora à média, logo, uma estratégia baseada em reversão à média não seria adequada.
            2. **Magnitude de λ**: Se λ for muito próximo de zero, a meia-vida será longa, o que torna uma estratégia de reversão à média menos lucrativa, já que não conseguiremos realizar muitas operações completas em um período de tempo razoável.
            3. **Escala Temporal Natural**: λ também define uma escala de tempo natural para vários parâmetros da estratégia. Por exemplo, se a meia-vida é de 20 dias, não deveríamos usar uma janela de 5 dias para calcular uma média móvel ou desvio padrão em uma estratégia de reversão à média. Definir a janela como um múltiplo pequeno da meia-vida tende a ser ideal e evita a otimização exaustiva de um parâmetro baseado no desempenho da estratégia.

            """)


            code_3 = '''
            # Importação da função VarianceRatio da biblioteca arch para realizar o teste de razão de variância
            from arch.unitroot import VarianceRatio

            # Aplicação do teste de Razão de Variância sobre a coluna 'close' do dataframe df, com defasagem (lag) de 5 períodos
            vr = VarianceRatio(df['close'], 5)

            # Exibição do sumário dos resultados do teste em formato de texto
            print(vr.summary().as_text())
            '''
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

# ----------------------------------------------  
            
            st.divider()
            st.markdown("""
    ### Estratégia de Trading Linear com Reversão à Média

    Depois de confirmar que uma série de preços é reversora à média e que sua meia-vida de reversão é curta o suficiente para o nosso horizonte de trading, podemos lucrar com uma estratégia linear simples. Para isso, basta calcular o desvio normalizado do preço em relação à sua média móvel (desvio padrão móvel dividido pelo desvio padrão móvel do preço). A quantidade de unidades desse ativo mantidas na carteira deve ser proporcionalmente negativa em relação a esse desvio normalizado. A janela para a média móvel e o desvio padrão pode ser ajustada para igualar a meia-vida da reversão.

    #### Por Que Usar Média Móvel e Desvio Padrão?

    Você pode se perguntar por que usar uma média móvel ou um desvio padrão móvel em uma estratégia de reversão à média. Se uma série de preços é estacionária, seus parâmetros de média e desvio padrão não deveriam ser fixos? Embora, em teoria, a média de uma série de preços estacionária seja fixa, na prática, ela pode mudar lentamente devido a fatores econômicos ou mudanças na gestão corporativa. Já para o desvio padrão, a Equação 2.4 mostra que até mesmo uma série estacionária com \(0 < H < 0.5\) apresenta uma variância crescente com o tempo, ainda que mais lentamente do que em um passeio aleatório geométrico. Assim, ao usar médias e desvios móveis, ajustamos a estratégia a uma média e desvio padrão que evoluem gradativamente, permitindo capturar lucros de maneira mais ágil.

    #### Importância dos Testes de Estacionaridade e Cálculo da Meia-Vida

    Um objetivo crucial dos traders é determinar se o retorno esperado ou o índice de Sharpe de uma estratégia de reversão à média é satisfatório. Então, por que nos preocuparmos com testes de estacionaridade (como o ADF ou o Teste de Razão de Variância) e o cálculo da meia-vida em vez de rodar um backtest diretamente? Esses testes preliminares têm uma significância estatística geralmente mais alta do que um backtest direto, pois utilizam os dados de preço de todos os dias (ou barras) disponíveis, enquanto um backtest gera um número menor de trades completos para análise de desempenho.

    Além disso, o resultado de um backtest depende dos parâmetros específicos da estratégia. Entretanto, se a série de preços passar nos testes estatísticos de estacionaridade, ou pelo menos apresentar uma meia-vida curta, podemos ter confiança de que conseguiremos encontrar uma estratégia de trading lucrativa, mesmo que não seja exatamente a estratégia backtestada inicialmente.

    Em capítulos seguintes, exploraremos mais essa ideia de adaptar a estratégia a uma média e desvio padrão móveis, principalmente no contexto de “scaling-in” (estratégia de incremento de posição).
    """)

            code_3 = '''
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            from tabulate import tabulate
            import yfinance as yf

            def rolling_z(series, window):
                """Calcula o Z-score móvel de uma série com uma janela especificada."""
                mean = series.rolling(window=window).mean()
                std = series.rolling(window=window).std()
                return (series - mean) / std

            def linear_mean_reversion_strategy(df, window):
                """
                Implementa uma estratégia simples de reversão à média.

                Parâmetros:
                - df (pd.DataFrame): DataFrame contendo uma coluna 'Close' com os preços do ativo.
                - window (int): Janela de tempo para o cálculo do Z-score.
                """
                
                # Calcula a quantidade de ativos a serem mantidos, baseado no Z-score inverso
                df["Quantity"] = -rolling_z(df["Close"], window)
                
                # Calcula o retorno diário, deslocando para obter o retorno no dia seguinte
                df["Return"] = df["Close"].pct_change().shift(-1)
                
                # Remove linhas com valores nulos e a última linha (que não terá retorno futuro)
                df = df.dropna(how="any")[:-1]
                
                # Calcula o lucro e perda (PnL) diário da estratégia multiplicando a quantidade pela variação do ativo
                df["PnL"] = df["Return"] * df["Quantity"]
                    
                # Plota o retorno cumulativo do instrumento e o PnL cumulativo da estratégia
                plt.plot(np.cumsum(df["Return"]), label="Cumulative Return of Stock")
                plt.plot(np.cumsum(df["PnL"]), label="Cumulative PnL of Strategy")
                
                # Adiciona uma legenda para identificação das linhas no gráfico
                plt.legend()
                
                # Exibe o gráfico
                plt.show()

            # Coleta de dados do Yahoo Finance
            ticker = "AAPL"  # Símbolo do ativo (por exemplo, "AAPL" para Apple)
            start_date = "2022-01-01"
            end_date = "2023-01-01"

            # Obtém os dados de preço de fechamento ajustado
            df = yf.download(ticker, start=start_date, end=end_date)[["Close"]]

            # Define o tamanho da janela para o Z-score
            window = 20

            # Aplica a estratégia
            linear_mean_reversion_strategy(df, window)

            '''
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            col1, col2 = st.columns(2)
            # Exibir a imagem do primeiro gráfico
            with col1:
                st.image("img/simple_meanrev_strate.png", caption='Legenda: Estratégia e Trading Linear com Reversão à Média', use_column_width=True)
            # Exibir a imagem do segundo gráfico
            with col2:
                st.write("Explicação da tabela e mais alguns pontos a serem adicionados")

# ==================== Mean Reversion ========================


# ==================== Cointegração ========================

        elif subsecao == "2. Cointegração":
            
            st.markdown("""
                ### Cointegração

                Na introdução deste capítulo, mencionamos que a maioria das séries de preços financeiras não é estacionária ou reversora à média. No entanto, isso não nos limita a negociar essas séries financeiras “pré-fabricadas”. Podemos, de forma proativa, criar uma carteira de séries de preços individuais, de maneira que o valor de mercado (ou preço) dessa carteira seja estacionário. Esse é o conceito de **cointegração**: se conseguimos encontrar uma combinação linear estacionária de várias séries de preços não estacionárias, dizemos que essas séries de preços são cointegradas.

                ##### Estratégia de Pairs Trading (Operação de Pares)

                A combinação mais comum na cointegração envolve duas séries de preços: compramos (long) um ativo e simultaneamente vendemos (short) outro, com uma alocação apropriada de capital em cada ativo. Esse é o conceito de **pairs trading**, uma estratégia que se beneficia da relação entre duas séries de preços. Se as duas séries forem cointegradas, esperamos que qualquer desvio em relação à combinação estacionária entre elas eventualmente retorne à média, o que nos permite lucrar com esses movimentos de reversão.

                ##### Cointegração com Múltiplos Ativos

                Embora o pairs trading seja um exemplo prático de cointegração com apenas dois ativos, o conceito pode ser facilmente estendido para três ou mais ativos. Neste caso, criamos uma combinação linear de várias séries de preços, buscando que a soma ponderada dessas séries resulte em uma série estacionária.

                ##### Testes de Cointegração

                Para verificar se duas ou mais séries de preços são cointegradas, utilizamos testes específicos. Dois testes de cointegração amplamente aplicados são:

                1. **Teste CADF (Augmented Dickey-Fuller Cointegration Test)**: Esse teste é adequado para pares de séries de preços, verificando se uma combinação linear entre elas é estacionária.
                
                2. **Teste de Johansen**: Esse método é aplicável a um número maior de séries e permite identificar relações de cointegração em portfólios que contenham mais de dois ativos.

                Esses testes são fundamentais para traders que desejam criar estratégias baseadas em cointegração, pois permitem identificar ativos cujas relações mantêm uma combinação estacionária ao longo do tempo, possibilitando operações com uma perspectiva de retorno à média.

                **Em resumo**, a cointegração amplia o campo de oportunidades de negociação, permitindo a criação de portfólios estacionários a partir de séries de preços que, individualmente, são não estacionárias. Esta abordagem fornece uma base robusta para estratégias de reversão à média e é uma ferramenta essencial para estratégias de pares e portfólios multivariados.
            """)


            st.divider()
            st.markdown("""
                ### Teste Cointegrated Augmented Dickey-Fuller (CADF)

                O teste Cointegrated Augmented Dickey-Fuller (CADF) é utilizado para determinar se uma combinação linear de duas séries temporais não estacionárias pode formar um portfólio estacionário. Esse teste resolve a questão de identificar as proporções ideais (hedge ratios) para combinar os ativos de forma a criar um portfólio estacionário.

                ##### Por que precisamos do CADF?

                Embora já existam testes como o ADF e o Variance Ratio para verificar a estacionaridade de uma série, eles não são suficientes para lidar com múltiplos ativos. Isso ocorre porque:

                1. **Falta de Hedge Ratios Pré-Definidos**: Quando temos várias séries de preços, não sabemos de antemão os hedge ratios ideais para combiná-las em um portfólio estacionário.
                2. **Combinatórias Aleatórias Não Funcionam**: Nem toda combinação linear aleatória de ativos cointegrados resulta em um portfólio estacionário. 

                ##### Como o CADF Funciona?

                O teste CADF utiliza uma abordagem sistemática para determinar a cointegração:

                1. **Regressão Linear**: Primeiro, realiza-se uma regressão linear entre duas séries de preços para determinar os hedge ratios ideais.
                2. **Formação do Portfólio**: Em seguida, esses hedge ratios são aplicados para criar uma combinação linear das séries de preços.
                3. **Teste de Estacionaridade**: Finalmente, o teste ADF é aplicado à série de preços do portfólio para verificar se ela é estacionária.

                Essa metodologia foi originalmente proposta por Engle e Granger (1987).

                ##### Exemplo de Aplicação

                Considere dois ETFs, **EWA** e **EWC**. O CADF pode ser usado para:

                1. Determinar a proporção ideal de capital para estar comprado (ou vendido) em cada ETF.
                2. Formar um portfólio estacionário com base nesses hedge ratios.
                3. Validar a estacionaridade do portfólio resultante, indicando a viabilidade de estratégias de reversão à média baseadas nesses ETFs.

                Com o CADF, os traders podem identificar combinações de ativos que potencialmente oferecem oportunidades de lucro consistentes por meio de estratégias de reversão à média.
            """)

            colab_link = "https://colab.research.google.com/drive/1zkR1PxN3eLnRESlV03_idqVBPYy3VM1C?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar um exemplo no Colab]({colab_link})")

            # Johansen Test
            st.divider()
            st.markdown("""
                ### Johansen Test for Cointegration

                O Johansen test é uma abordagem estatística usada para identificar relações de cointegração em séries temporais múltiplas. Diferentemente de testes como o CADF, que avaliam cointegração entre duas variáveis e são dependentes da ordem das séries, o Johansen test pode ser aplicado a mais de duas séries simultaneamente, determinando todas as combinações lineares possíveis que formam portfólios estacionários.

                ##### Fundamentos do Johansen Test
                1. **Generalização de Cointegração**: Amplia a análise para vetores de preços e matrizes de coeficientes. O número de relações de cointegração (r) é determinado pelo posto da matriz de coeficientes (Λ).
                2. **Estatísticas de Teste**:
                - **Trace Statistic**: Testa hipóteses nulas de r ≤ k, onde k varia de 0 a (n-1), sendo n o número de séries.
                - **Eigen Statistic**: Também avalia r ≤ k, mas com base na decomposição de autovalores de Λ.

                ##### Exemplo 1: EWA e EWC
                - **Resultado**: Ambos os testes rejeitam a hipótese r = 0 (sem cointegração) e r ≤ 1, confirmando duas relações de cointegração entre os ETFs EWA e EWC.  
                - **Significado**: Mesmo com apenas duas séries, é possível formar dois portfólios estacionários com diferentes hedge ratios. O Johansen test elimina a dependência da ordem das variáveis, fornecendo diretamente todos os portfólios possíveis.

                ##### Exemplo 2: EWA, EWC e IGE
                - **Adição de uma terceira série**: Incluindo o ETF IGE, que representa ações de recursos naturais, o teste foi estendido para três séries.  
                - **Resultado**: Foram identificadas três relações de cointegração com 95% de certeza, permitindo a formação de múltiplos portfólios estacionários. Os autovalores e autovetores encontrados determinam os hedge ratios para cada portfólio.

                ### Considerações Finais
                O Johansen test é uma ferramenta poderosa para estratégias de cointegração, especialmente ao lidar com múltiplas séries temporais. Sua independência em relação à ordem das séries e capacidade de identificar todas as combinações cointegradas tornam-no superior a métodos univariados em análises mais complexas.
                """)

            code = '''
# Importações necessárias
import yfinance as yf
import pandas as pd
import numpy as np
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from tabulate import tabulate

# Função para imprimir linha pontilhada (caso precise)
def print_dashed_line():
    print("-" * 50)

# Função para realizar o teste de cointegração de Johansen
def johansen_cointegration(df, ticker_one, ticker_two):
    """
    Realiza o teste de cointegração de Johansen entre duas séries temporais.

    Parâmetros:
    - df: DataFrame contendo as séries temporais.
    - ticker_one: Nome da primeira série (coluna do DataFrame).
    - ticker_two: Nome da segunda série (coluna do DataFrame).

    Retorno:
    - jres: Resultado do teste de cointegração de Johansen.
    """
    # Realizando o teste de cointegração de Johansen
    jres = coint_johansen(df[[ticker_one, ticker_two]], det_order=0, k_ar_diff=1)

    # Resumo dos resultados do teste Trace
    summary = []
    for i in range(jres.trace_stat.shape[0]):
        summary.append([
            f"r<={i}", jres.trace_stat[i], jres.trace_stat_crit_vals[i][0], jres.trace_stat_crit_vals[i][1],
            jres.trace_stat_crit_vals[i][2]])

    # Exibindo os resultados do teste Trace
    print("Johansen Cointegration Test (Trace Statistics)")
    print(tabulate(summary, headers=["NULL:", "Trace Statistics", "Crit 90%", "Crit 95%", "Crit 99%"]))
    print("\n")

    # Resumo dos resultados do teste Eigen
    summary = []
    for i in range(jres.max_eig_stat.shape[0]):
        summary.append([
            f"r<={i}", jres.max_eig_stat[i], jres.max_eig_stat_crit_vals[i][0], jres.max_eig_stat_crit_vals[i][1],
            jres.max_eig_stat_crit_vals[i][2]])

    # Exibindo os resultados do teste Eigen
    print("Johansen Cointegration Test (Eigen Statistics)")
    print(tabulate(summary, headers=["NULL:", "Eigen Statistics", "Crit 90%", "Crit 95%", "Crit 99%"]))

    # Exibindo os valores próprios e os vetores próprios
    print("Eigen values: " + " ".join(f"{i:0.6f}" for i in jres.eig))
    print("Eigen vectors: " + " ".join(f"{i}" for i in jres.evec))

    # Imprimindo linha pontilhada de separação
    print_dashed_line()

    # Retornando os resultados do teste
    return jres

# Função para obter dados históricos de ativos com o yfinance
def get_data(tickers, start_date, end_date):
    """
    Obtém dados históricos de ativos financeiros com yfinance.

    Parâmetros:
    - tickers: Lista de tickers dos ativos.
    - start_date: Data de início (formato 'YYYY-MM-DD').
    - end_date: Data de fim (formato 'YYYY-MM-DD').

    Retorno:
    - DataFrame com os dados históricos dos ativos.
    """
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Testando a função com dados reais de ativos
if __name__ == "__main__":
    # Defina os tickers e o período
    tickers = ['EWC', 'EWA']  # Exemplo: AAPL e MSFT
    start_date = '2006-01-01'
    end_date = '2012-01-01'

    # Obtendo os dados históricos
    df = get_data(tickers, start_date, end_date)

    # Chamando a função de cointegração de Johansen
    johansen_cointegration(df, 'EWC', 'EWA')


====================== Output ============================
Johansen Cointegration Test (Trace Statistics)
NULL:      Trace Statistics    Crit 90%    Crit 95%    Crit 99%
-------  ------------------  ----------  ----------  ----------
r<=0               20.5197      13.4294     15.4943     19.9349
r<=1                4.30495      2.7055      3.8415      6.6349


Johansen Cointegration Test (Eigen Statistics)
NULL:      Eigen Statistics    Crit 90%    Crit 95%    Crit 99%
-------  ------------------  ----------  ----------  ----------
r<=0               16.2148      12.2971     14.2639     18.52
r<=1                4.30495      2.7055      3.8415      6.6349
Eigen values: 0.010688 0.002849
Eigen vectors: [1.03947063 0.13619127] [-1.53822008  0.2337235 ]
--------------------------------------------------
            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1zkR1PxN3eLnRESlV03_idqVBPYy3VM1C?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            # Estratégia
            st.divider()
            st.markdown("""
                ### Linear Mean-Reverting Trading on a Portfolio

                No exemplo, o portfólio EWA-EWC-IGE, formado com o "melhor" autovetor do Johansen test, mostrou uma curta meia-vida, tornando-o adequado para estratégias de reversão à média. A estratégia testada consiste em acumular unidades do portfólio proporcionalmente ao Z-Score negativo do preço do portfólio. Aqui, o portfólio unitário é determinado pelos pesos do autovetor do Johansen test, funcionando de forma semelhante a um ETF ou fundo mútuo.

                ##### Características da Estratégia
                1. **Linearidade**: 
                - A quantidade investida é proporcional ao Z-Score do portfólio, mas não ao valor de mercado total do investimento.
                - Essa abordagem linear simplifica o modelo, removendo a necessidade de otimização de parâmetros e eliminando o viés de data-snooping.

                2. **Praticidade**:
                - Embora útil para backtesting, a estratégia não é diretamente prática. Entrar ou sair de infinitas posições conforme pequenos movimentos de preço não é viável, e o capital máximo necessário não pode ser previsto com precisão.

                3. **Significância Estatística**:
                - Como a estratégia realiza posições continuamente e não depende de regras de entrada e saída complexas, os resultados têm maior significância estatística, reduzindo o impacto de eventos aleatórios no desempenho.

                O backtesting dessa estratégia linear simples demonstra que lucros podem ser extraídos de séries de preços cointegradas sem viés de otimização, usando apenas propriedades intrínsecas da série, como a meia-vida. Embora não seja diretamente aplicável ao mercado real, o modelo oferece uma base para entender e avaliar estratégias de reversão à média.
                """)


            colab_link = "https://colab.research.google.com/drive/1zkR1PxN3eLnRESlV03_idqVBPYy3VM1C?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

# ==================== Cointegração ========================

# ==================== Pros and Cons of Mean-Reverting Strategies ========================

        elif subsecao == "3. Prós e Contras da Reversão a média":
 
            st.markdown("""
                ### Prós e Contras das Estratégias de Reversão à Média

                As estratégias de reversão à média possuem características específicas que as tornam atraentes para traders, mas também apresentam alguns riscos e desafios. Abaixo, listamos os principais prós e contras dessas estratégias.

                #### Prós

                - **Facilidade de Construção**: É relativamente simples construir estratégias de reversão à média, pois não estamos limitados a instrumentos que sejam intrinsecamente estacionários. Podemos escolher e combinar uma variedade de ações e ETFs cointegrados para criar um portfólio estacionário.

                - **Abundância de Ativos**: Há uma grande variedade de ativos para selecionar, incluindo novos ETFs que surgem anualmente e que oferecem oportunidades de cointegração.

                - **Fundamento Econômico**: Muitas vezes, pares cointegrados possuem uma lógica econômica sólida. Por exemplo, EWA e EWC são ETFs que cointegram devido às economias de Canadá e Austrália serem orientadas por commodities. Esse fundamento sólido diferencia as estratégias de reversão à média das estratégias de momentum, que dependem de diferenças na velocidade de reação dos investidores às notícias.

                - **Variedade de Escalas de Tempo**: As estratégias de reversão à média podem ser aplicadas em diversas escalas de tempo. Estratégias de market-making operam com reversões em segundos, enquanto investidores de longo prazo esperam anos pela valorização de ações subvalorizadas. Em particular, estratégias de curto prazo são vantajosas para traders, pois o maior número de trades aumenta a confiança estatística e o Sharpe Ratio do backtest e das operações ao vivo.

                #### Contras

                - **Risco de Consistência Enganosa**: A aparente consistência nas estratégias de reversão à média pode levar à confiança excessiva e ao uso de alavancagem elevada. Quando a estratégia falha – muitas vezes por razões fundamentais que só ficam claras em retrospecto –, os traders geralmente estão altamente alavancados, o que torna as perdas raras, mas severas.

                - **Desafios na Gestão de Risco**: A gestão de risco é particularmente difícil para essas estratégias, pois o uso de stop losses convencionais não é sempre viável. Além disso, como as perdas são raras, elas podem ser imprevisivelmente grandes quando ocorrem. Em estratégias de reversão à média, é essencial desenvolver técnicas de controle de risco adaptadas, abordadas mais detalhadamente no Capítulo 8.

                Esses pontos ressaltam a importância de equilibrar as vantagens das estratégias de reversão à média com uma gestão de risco rigorosa, especialmente para evitar o impacto de eventos extremos e inesperados.
                """)
        
        elif subsecao == "4. Resumo":
            st.markdown("""
            ###  Conceitos fundamentais:

            - **Reversão à Média**: Refere-se ao fenômeno em que a mudança no preço é proporcional à diferença entre o preço médio e o preço atual. Em outras palavras, espera-se que o preço reverta em direção à média ao longo do tempo.

            - **Estacionaridade**: Uma série estacionária se difunde mais lentamente do que um passeio aleatório geométrico. Isso significa que, embora o preço possa variar, ele tende a se manter dentro de certos limites.

            - **Teste ADF**: O teste de Dickey-Fuller Aumentado (ADF) é utilizado para testar a hipótese de reversão à média em uma série temporal. Ele verifica se a série retorna consistentemente para uma média ao longo do tempo.

            - **Exponente de Hurst e Teste de Razão de Variância**: Esses métodos são empregados para testar a estacionaridade de uma série. Eles ajudam a identificar se a série tende a se difundir de maneira controlada, caracterizando-a como estacionária.

            - **Half-Life de Reversão à Média**: Mede a velocidade com que uma série de preços retorna à sua média. Esse indicador é útil para prever a lucratividade ou o Sharpe Ratio de uma estratégia de trading de reversão à média. Um half-life curto indica uma reversão rápida, ideal para estratégias de trading mais ativas.

            - **Estratégia de Trading Linear**: Em uma estratégia linear, o número de unidades ou ações que possuímos em um portfólio é proporcional ao Z-Score negativo da série de preços. Isso significa que, à medida que o preço se afasta da média, aumentamos ou reduzimos nossa posição de acordo.

            - **Cointegração**: Se combinarmos duas ou mais séries de preços não estacionárias e formarmos um portfólio estacionário, essas séries são consideradas cointegradas. A cointegração permite a criação de portfólios que mantêm uma relação estável, apesar das variações de cada ativo individualmente.

            - **Testes de Cointegração (CADF e Johansen)**: O teste CADF verifica a cointegração entre dois ativos, enquanto o teste de Johansen pode ser aplicado a um número maior de séries. Estes testes ajudam a identificar combinações estacionárias de séries não estacionárias.

            - **Autovalores e Autovetores no Teste de Johansen**: Os autovetores resultantes do teste de Johansen podem ser usados como proporções de hedge para criar um portfólio estacionário a partir das séries de preços analisadas. O autovetor associado ao maior autovalor é aquele com o half-life mais curto, indicando uma reversão mais rápida.

            Esses conceitos são fundamentais para desenvolver estratégias de reversão à média e cointegração, fornecendo uma base analítica para avaliar a viabilidade e lucratividade de operações nesses mercados.
""")

# ====================== Chapter 2 The Basics of Mean Reversion ============


# ====================================================================================


# ===================== Chapter 3 Implementing Mean Reversion Strategies =============

    elif pagina == "4 . Estratégias de Reversão à Média":
        st.title("4 . Estratégias de Reversão à Média")

        if subsecao == "Introdução":
           st.markdown("""
                **Implementing Mean Reversion Strategies**

                Estratégias de reversão à média baseiam-se na ideia de que os preços tendem a retornar a um nível médio ao longo do tempo. Embora o capítulo anterior tenha descrito testes estatísticos para identificar séries estacionárias ou cointegradas adequadas, a implementação prática de estratégias de reversão à média não depende exclusivamente de uma verdadeira estacionariedade.

                ### Considerações sobre Reversão à Média
                1. **Estacionariedade e Cointegração**: Embora ativos individuais raramente sejam estacionários, portfólios de ativos cointegrados (como pares long-short) podem ser explorados. No entanto, a reversão à média também pode ser capturada em períodos curtos ou sazonais, como condições específicas do dia.  
                - **Exemplo**: Uma série estacionária com um tempo de reversão longo (ex.: 10 anos) pode não ser lucrativa para negociação.  

                2. **Estratégias Simples de Reversão**:  
                - Uma estratégia linear escalonada compra proporcionalmente ao desvio do preço em relação à média. Apesar de ser conceitualmente simples, ela não é prática devido à necessidade de reequilíbrio constante e poder de compra ilimitado.  

                ### Estratégias Práticas
                1. **Bandas de Bollinger**:  
                - Uma técnica mais prática para reversão à média, onde limites superiores e inferiores (baseados em desvios-padrão) sinalizam pontos de entrada e saída.  
                - Variantes incluem múltiplos níveis de entrada e saída ("scaling-in"), permitindo ajustes graduais de posição conforme o preço se afasta ou retorna à média.  

                2. **Filtro de Kalman**:  
                - Utilizado para estimar o hedge ratio e o preço médio em tempo real, permitindo uma modelagem dinâmica de reversão.  

                ### Cuidados na Implementação
                1. **Erros de Dados**: Estratégias de reversão à média são altamente sensíveis a erros nos dados. Pequenos erros podem gerar sinais falsos e prejuízos.  
                2. **Custos de Transação**: Embora ignorados nos exemplos apresentados, são críticos para avaliar a viabilidade real da estratégia.  
                3. **Viés de Look-ahead**: Evite usar os mesmos dados para otimizar parâmetros (como o hedge ratio) e para backtesting, pois isso pode inflar resultados e reduzir a utilidade preditiva do modelo.

                ### Conclusão
                Estratégias de reversão à média requerem uma implementação cuidadosa para evitar armadilhas comuns, como viés de look-ahead e erros de dados. Embora os exemplos apresentados ignorem algumas dessas nuances para simplificar a explicação, os traders devem ajustar esses modelos para aplicações reais e robustas.
                """)

        elif subsecao == "Trading Pairs":
  
            st.markdown("""
            ### Trading Pairs Using Price Spreads, Log Price Spreads, or Ratios**

            Estratégias de reversão à média podem usar spreads de preços, logaritmos de preços ou razões como sinais de negociação. O método tradicional utiliza o valor de mercado do portfólio formado por uma combinação linear de preços, onde os pesos são os hedge ratios derivados de regressões ou do Johansen test. Essa abordagem cria uma série estacionária que pode ser usada como sinal de trading.

            ##### Comparação entre Sinais
            1. **Price Spreads**:
            - Simplifica a estratégia ao usar o spread direto entre preços.
            - Requer hedge ratios fixos, mas pode ser menos eficaz se os preços das ações não estiverem escalados proporcionalmente.

            2. **Log Price Spreads**:
            - Considera os logaritmos dos preços, criando um portfólio estacionário com pesos de capital constantes.
            - Exige reequilíbrio frequente para manter as proporções de capital fixas, o que pode aumentar custos operacionais.

            3. **Ratios**:
            - Útil quando os ativos não são verdadeiramente cointegrados, mas o spread é considerado reversível a curto prazo.
            - Permite dispensar hedge ratios dinâmicos, simplificando o modelo.
            - É especialmente vantajoso em cenários onde as diferenças de escala entre preços dificultam o uso de spreads, como no trading de pares com grandes discrepâncias de preço.

            ##### Exemplos e Aplicações
            - **GLD e USO**:
            - Em um exemplo comparativo, spreads de preço com hedge ratios adaptativos superaram o uso de razões como sinais de negociação.
            - **Trading de Moedas**:
            - Pairs como EUR.GBP já representam uma razão, enquanto pares como MXN.NOK podem se beneficiar do uso de ratios, devido à ausência de estacionariedade verdadeira.

            Cada abordagem tem seus méritos dependendo do contexto e das propriedades dos ativos negociados. Spreads de preço são preferíveis em ativos cointegrados, enquanto ratios podem ser mais eficazes em cenários onde os ativos não são verdadeiramente estacionários, simplificando o modelo e evitando reequilíbrios frequentes.
            """)

            colab_link = "https://colab.research.google.com/drive/1ihcWiNwspG_qrUiPeZSstOl3PE9yfPc_?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

        elif subsecao == "Bollinger Bands":
            st.markdown("""
            ### Bollinger Bands 

            A estratégia de reversão à média mais simples descrita até agora é a linear, na qual o número de unidades investidas em um portfólio estacionário é proporcional ao desvio do preço em relação à média móvel. Embora útil para testar a viabilidade da reversão à média, essa abordagem não é prática, pois não define um limite para o capital investido, deixando a estratégia vulnerável a desvios prolongados.

            ##### Estratégia das Bandas de Bollinger
            Para contornar essa limitação, utilizamos **Bollinger Bands**, que estabelecem limites baseados no desvio-padrão da média móvel. A estratégia funciona da seguinte maneira:
            1. **Entrada**: Compra ou venda ocorre quando o preço se desvia **entryZscore** desvios-padrão acima ou abaixo da média móvel.
            2. **Saída**: A posição é encerrada quando o preço retorna a **exitZscore** desvios-padrão da média. Algumas abordagens comuns:
            - **exitZscore = 0**: Sai da posição quando o preço volta à média.
            - **exitZscore = -entryZscore**: Sai da posição apenas quando o preço atinge o extremo oposto da banda, invertendo a posição.

            ##### Parâmetros da Estratégia
            - **entryZscore** e **exitZscore** são parâmetros livres, ajustáveis com otimização em um conjunto de treinamento.
            - **Período de Look-back**: A média móvel e o desvio-padrão podem ser calculados com um período de look-back fixo ou ajustado com base na meia-vida da reversão à média.
            - **Gestão de Capital e Risco**: A estratégia opera com posições discretas (long ou short), facilitando a alocação de capital e o gerenciamento de risco.

            O uso de **Bollinger Bands** torna a estratégia de reversão à média mais prática e controlada, evitando exposição ilimitada a desvios prolongados. A escolha adequada dos parâmetros pode melhorar a robustez da estratégia e minimizar riscos associados a oscilações excessivas do mercado.
            """)

            colab_link = "https://colab.research.google.com/drive/1ihcWiNwspG_qrUiPeZSstOl3PE9yfPc_?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()

            st.markdown("""
**Does Scaling-in Work?**

A estratégia de **scaling-in** (ou averaging-in) consiste em aumentar gradualmente a posição em uma estratégia de reversão à média à medida que o preço se afasta da média. Essa abordagem permite capturar lucros parciais sempre que há uma pequena reversão, reduzindo o impacto de mercado para grandes posições e possibilitando ganhos mesmo quando a série de preços não é perfeitamente estacionária. Uma implementação comum usa múltiplos níveis de entrada e saída em **Bollinger Bands**, ajustando pontos de entrada **(entryZscore = 1, 2, 3...N)** e saída **(exitZscore = 0, 1, 2...N-1)**. No entanto, pesquisas sugerem que **scaling-in pode não ser a abordagem mais lucrativa**.

### Comparação entre "All-in" e "Scaling-in"
O estudo de **Schoenberg e Corwin (2010)** demonstra que entrar em múltiplos pontos **nunca** é a estratégia mais rentável em backtests. Eles argumentam que existe um nível ótimo único de entrada ("all-in") que maximiza os retornos.  
O estudo compara três métodos em um cenário onde o preço oscila entre **L1** (nível inicial), **L2** (nível mais baixo antes da reversão) e **F** (preço final esperado):
1. **All-in at L1**: Compra-se toda a posição em **L1**, independentemente de possíveis quedas adicionais.
2. **All-in at L2**: Aguarda-se a queda para **L2** antes de comprar toda a posição.
3. **Scaling-in**: Compra-se parte da posição em **L1** e o restante em **L2**, se o preço cair mais.

### Conclusões do Estudo:
- Se a probabilidade do preço cair até **L2** for baixa (**p < p̂**), **All-in at L1** é mais lucrativo.
- Se a probabilidade do preço atingir **L2** for alta (**p > p̂**), **All-in at L2** é superior.
- **Scaling-in nunca é o método mais lucrativo** em comparação com os dois anteriores.

### Quando o Scaling-in Ainda Pode Funcionar?
Apesar das evidências contra scaling-in em backtests, há fatores do mercado real que podem justificar seu uso:
- **Volatilidade variável**: A hipótese do estudo assume uma volatilidade constante, mas na realidade, volatilidade muda ao longo do tempo, o que pode favorecer scaling-in.
- **Melhoria no Sharpe Ratio**: Mesmo que os retornos absolutos sejam menores, scaling-in pode reduzir a volatilidade da estratégia e melhorar sua relação risco-retorno.
- **Melhor desempenho fora da amostra**: Embora scaling-in pareça ineficaz nos dados de treinamento, pode superar o método "all-in" em ambientes de mercado dinâmicos.

### Conclusão
Embora **scaling-in** pareça intuitivo e ofereça vantagens como redução do impacto de mercado, estudos sugerem que **"all-in" em um único ponto de entrada otimizado gera retornos superiores**. No entanto, fatores como mudanças na volatilidade podem fazer com que scaling-in tenha um desempenho melhor em condições de mercado reais e fora da amostra. O ideal é testar diferentes abordagens antes de aplicá-las no trading ao vivo.
""")

        elif subsecao == "Kalman Filter":

            st.markdown("""
            Estratégias de rompimento envolvem a identificação e a negociação de momentos em que o preço ultrapassa níveis importantes de suporte ou resistência.
            """)
            mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")


        elif subsecao == "Erros nos dados":
            st.markdown("""
**The Danger of Data Errors**

Erros nos dados são especialmente prejudiciais para estratégias de reversão à média, tanto em **backtesting** quanto em **execução ao vivo**. Pequenos erros ou outliers nos preços históricos podem criar oportunidades fictícias de lucro, inflacionando os resultados do backtest. Por exemplo, se um preço erroneamente registrado for muito mais alto do que o real, a estratégia pode sugerir uma venda a descoberto lucrativa que nunca teria ocorrido no mercado real.

### Impacto nos Backtests
- **Reversão à Média**: Dados errôneos podem inflacionar lucros artificiais ao registrar preços fora do normal, criando sinais falsos de entrada e saída.  
- **Estratégias de Momentum**: São menos afetadas, pois erros nos preços podem resultar em ordens de compra seguidas por perdas rápidas, reduzindo a performance do backtest.

### Problemas em Execução ao Vivo
- **Erros em Cotações Bid/Ask**: Se um erro inflacionar o preço de compra ou venda, uma estratégia pode enviar ordens erradas e gerar perdas reais.  
- **Impacto em Pairs Trading e Arbitragem**: Essas estratégias dependem de pequenas diferenças nos preços entre ativos. Um erro em uma das cotações pode aumentar artificialmente o spread e acionar negociações incorretas.  
  - Exemplo: Se o spread real entre dois ativos for $5, mas um erro fizer parecer que é $6, um trade equivocado pode ser executado, resultando em prejuízo.

### Mitigação de Erros
- **Uso de Feeds de Dados Confiáveis**: Dados errados de corretores podem gerar perdas inesperadas. Testes mostraram que feeds de terceiros, como **Bloomberg** ou até **Yahoo! Finance**, podem oferecer maior estabilidade e precisão.  
- **Cancel-and-Correct Codes**: Alguns provedores utilizam códigos da bolsa para corrigir erros em tempo real, reduzindo impactos negativos na negociação.

### Conclusão
Dados errôneos são um risco oculto, especialmente para estratégias de **reversão à média** e **pairs trading**, onde pequenos erros podem gerar grandes impactos. A escolha de um fornecedor de dados confiável e o monitoramento contínuo da qualidade dos dados são essenciais para evitar perdas desnecessárias e garantir que estratégias sejam eficazes tanto no backtest quanto na execução real.
""")

        elif subsecao == "Conclusão":
            st.markdown("""
        ### Key Points: Mean-Reverting Strategies and Practical Considerations**

        - **Construção de Portfólios**:  
        - Para um portfólio de reversão à média com um **número fixo de ações**, utilize **séries de preços** para calcular os hedge ratios.  
        - Para um portfólio com **valores de mercado fixos**, utilize **logaritmos dos preços**.  

        - **Escolha entre Spreads e Ratios**:  
        - Para **moedas e pares cambiais**, o **uso de razões (ratios)** pode ser mais eficaz do que spreads, especialmente quando não há cointegração perfeita.  

        - **Ajustando-se a Mudanças no Mercado**:  
        - O **hedge ratio, a média e o desvio padrão** podem mudar ao longo do tempo. Para lidar com isso, utilize um **período de look-back móvel** ou um **Filtro de Kalman**.  

        - **Bollinger Bands e Scaling-in**:  
        - A implementação prática de estratégias lineares de reversão à média pode ser feita com **Bandas de Bollinger** e **scaling-in**.  
        - Embora **scaling-in** nem sempre seja ótimo em backtests, ele pode ser útil no **trading ao vivo**, onde a volatilidade e as probabilidades mudam.  

        - **Uso do Kalman Filter**:  
        - Para atualizar dinamicamente a **expectativa de preço** com base nos últimos negócios (preço e volume), o **Filtro de Kalman** pode ser empregado.  

        - **Impacto de Erros nos Dados**:  
        - Erros de dados podem **inflacionar artificialmente os resultados** de backtests em estratégias de **reversão à média**, mas afetam menos estratégias de **momentum**.  
        - Estratégias baseadas em **spreads são altamente sensíveis** a pequenos erros de dados, tanto em backtests quanto em operações ao vivo.  

        ### Conclusão
        A escolha dos métodos corretos para definir hedge ratios, ajustar estratégias e evitar armadilhas como erros de dados pode fazer a diferença entre um modelo teórico viável e uma estratégia prática e rentável no mercado real.
            """)

          

# ===================== Chapter 3 Implementing Mean Reversion Strategies =============

# ====================================================================================
    
# ===================== Chapter 4 Mean Reversion of  =============

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

# ===================== Chapter 4 Mean Reversion of  =============

# ====================================================================================


# ===================== Chapter 5 Mean Reversion of Currencies and Futures =============

    elif pagina == "6 . Reversão à Média de Moedas e Futuros":
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




        elif subsecao == "Futures Intermarket Spreads":
            st.markdown("""
                **Futures Intermarket Spreads**

                Intermarket spreads em contratos futuros envolvem pares de ativos subjacentes diferentes. Embora seja difícil encontrar spreads com comportamento de reversão à média, existem alguns candidatos interessantes, especialmente em mercados inter-relacionados.

                ### Exemplos de Spreads em Mercados de Energia
                1. **Crack Spread (CL, RB e HO)**:
                - Consiste em uma carteira formada por três contratos longos de WTI crude oil (CL), dois contratos short de gasolina (RB) e um contrato short de óleo de aquecimento (HO).
                - Representa a relação entre a produção de derivados a partir do petróleo bruto, onde a proporção 3:2:1 reflete a produção média de refinarias.
                - **Resultado do Teste ADF**: Não estacionário. Durante o período de 2007-2008, apresentou alta volatilidade e retornos negativos em estratégias de reversão à média.
                - **Vantagem Operacional**: A NYMEX oferece uma cesta pronta para o crack spread, reduzindo os requisitos de margem em comparação com negociações separadas.

                2. **Spread entre CL e BZ (1:1)**:
                - Ambas as commodities representam petróleo bruto (WTI e Brent), sugerindo uma relação forte.
                - **Resultado do Teste ADF**: Não estacionário, devido a fatores como:
                    - Aumento da produção de petróleo nos EUA.
                    - Gargalos nos oleodutos em Cushing, Oklahoma.
                    - Questões geopolíticas, como o embargo ao petróleo iraniano, que impactaram o Brent (BZ) mais do que o WTI (CL).

                ### Cuidados no Backtesting de Intermarket Spreads
                1. **Sincronização de Preços**: Certifique-se de que os preços sejam registrados no mesmo horário. Antes de setembro de 2001, o Brent (BZ) era negociado na Intercontinental Petroleum Exchange em Londres, com horário de fechamento diferente do NYMEX, onde o WTI (CL) é negociado.
                2. **Ajustes para USD**: Futuros podem exigir multiplicadores para converter os preços para dólares americanos, garantindo consistência nos cálculos.

                ### Conclusão
                Embora intermarket spreads sejam promissores em mercados relacionados, como energia, a falta de estacionariedade torna muitos deles inadequados para estratégias de reversão à média. A análise cuidadosa e a consideração de fatores como sincronização de preços são essenciais para evitar erros em backtests e estratégias.
                """)

            mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")

# ===================== Chapter 5 Mean Reversion of Currencies and Futures =============

# ====================================================================================



# ===================== Chapter 6 Interday Momentum Strategies ==================

    elif pagina == "7 . Estratégias de Momentum Interdiário":
        st.title("7 . Estratégias de Momentum Interdiário")
        if subsecao == "Introdução":
           st.markdown("""
                **Momentum in Trading**

                Momentum em preços de ativos tem quatro causas principais: persistência nos retornos de rolagem de futuros, lenta assimilação de novas informações, compras ou vendas forçadas por fundos e manipulação de mercado por traders de alta frequência. Esse fenômeno é classificado em dois tipos: **momentum temporal**, em que retornos passados estão positivamente correlacionados com retornos futuros, e **momentum cross-sectional**, em que ativos com desempenho superior a outros tendem a continuar superando. Estratégias de momentum interday, abordadas neste capítulo, mantêm posições por vários dias e podem explorar esses padrões. No entanto, elas apresentam fragilidades recentemente identificadas, que afetam menos as estratégias de momentum intraday, tema do próximo capítulo. Além disso, estratégias de momentum diferem significativamente de estratégias de reversão à média em propriedades, vantagens e desvantagens.

                ### Considerações Finais
                Momentum é uma ferramenta poderosa para trading, especialmente em futuros e ações, mas requer atenção às suas fragilidades e ao contexto de aplicação. A distinção entre estratégias interday e intraday permite adaptar os modelos a diferentes dinâmicas de mercado, maximizando retornos enquanto minimiza riscos associados às vulnerabilidades recentemente descobertas.
                """)

        elif subsecao == "Tests for Time Series Momentum":

            st.markdown("""
            Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.
            """)
            mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")        






        elif subsecao == "Time Series Strategies":
            st.markdown("""
            Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.
            """)
            mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")
        elif subsecao == "Scalping":
            st.markdown("""
            Scalping é uma estratégia de curto prazo que busca obter pequenos lucros a partir de movimentos de preços muito pequenos.
            """)
            mostrar_imagem("https://example.com/imagem_scalping.png", "Scalping")




        elif subsecao == "Futures Intermarket Spreads":
            st.markdown("""
                **Futures Intermarket Spreads**

                Intermarket spreads em contratos futuros envolvem pares de ativos subjacentes diferentes. Embora seja difícil encontrar spreads com comportamento de reversão à média, existem alguns candidatos interessantes, especialmente em mercados inter-relacionados.

                ### Exemplos de Spreads em Mercados de Energia
                1. **Crack Spread (CL, RB e HO)**:
                - Consiste em uma carteira formada por três contratos longos de WTI crude oil (CL), dois contratos short de gasolina (RB) e um contrato short de óleo de aquecimento (HO).
                - Representa a relação entre a produção de derivados a partir do petróleo bruto, onde a proporção 3:2:1 reflete a produção média de refinarias.
                - **Resultado do Teste ADF**: Não estacionário. Durante o período de 2007-2008, apresentou alta volatilidade e retornos negativos em estratégias de reversão à média.
                - **Vantagem Operacional**: A NYMEX oferece uma cesta pronta para o crack spread, reduzindo os requisitos de margem em comparação com negociações separadas.

                2. **Spread entre CL e BZ (1:1)**:
                - Ambas as commodities representam petróleo bruto (WTI e Brent), sugerindo uma relação forte.
                - **Resultado do Teste ADF**: Não estacionário, devido a fatores como:
                    - Aumento da produção de petróleo nos EUA.
                    - Gargalos nos oleodutos em Cushing, Oklahoma.
                    - Questões geopolíticas, como o embargo ao petróleo iraniano, que impactaram o Brent (BZ) mais do que o WTI (CL).

                ### Cuidados no Backtesting de Intermarket Spreads
                1. **Sincronização de Preços**: Certifique-se de que os preços sejam registrados no mesmo horário. Antes de setembro de 2001, o Brent (BZ) era negociado na Intercontinental Petroleum Exchange em Londres, com horário de fechamento diferente do NYMEX, onde o WTI (CL) é negociado.
                2. **Ajustes para USD**: Futuros podem exigir multiplicadores para converter os preços para dólares americanos, garantindo consistência nos cálculos.

                ### Conclusão
                Embora intermarket spreads sejam promissores em mercados relacionados, como energia, a falta de estacionariedade torna muitos deles inadequados para estratégias de reversão à média. A análise cuidadosa e a consideração de fatores como sincronização de preços são essenciais para evitar erros em backtests e estratégias.
                """)

            mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")

# ===================== Chapter 6 Interday Momentum Strategies =============



# ===================== Chapter 7 Interday Momentum Strategies ==================

    elif pagina == "7 . Estratégias de Momentum Interdiário":
        st.title("7 . Estratégias de Momentum Interdiário")
        if subsecao == "Introdução":
           st.markdown("""
                **Momentum in Trading**

                Momentum em preços de ativos tem quatro causas principais: persistência nos retornos de rolagem de futuros, lenta assimilação de novas informações, compras ou vendas forçadas por fundos e manipulação de mercado por traders de alta frequência. Esse fenômeno é classificado em dois tipos: **momentum temporal**, em que retornos passados estão positivamente correlacionados com retornos futuros, e **momentum cross-sectional**, em que ativos com desempenho superior a outros tendem a continuar superando. Estratégias de momentum interday, abordadas neste capítulo, mantêm posições por vários dias e podem explorar esses padrões. No entanto, elas apresentam fragilidades recentemente identificadas, que afetam menos as estratégias de momentum intraday, tema do próximo capítulo. Além disso, estratégias de momentum diferem significativamente de estratégias de reversão à média em propriedades, vantagens e desvantagens.

                ### Considerações Finais
                Momentum é uma ferramenta poderosa para trading, especialmente em futuros e ações, mas requer atenção às suas fragilidades e ao contexto de aplicação. A distinção entre estratégias interday e intraday permite adaptar os modelos a diferentes dinâmicas de mercado, maximizando retornos enquanto minimiza riscos associados às vulnerabilidades recentemente descobertas.
                """)


        elif subsecao == "Tests for Time Series Momentum":

            st.markdown("""
            Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.
            """)
            mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")        

        elif subsecao == "Time Series Strategies":
            st.markdown("""
            Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.
            """)
            mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")
        elif subsecao == "Scalping":
            st.markdown("""
            Scalping é uma estratégia de curto prazo que busca obter pequenos lucros a partir de movimentos de preços muito pequenos.
            """)
            mostrar_imagem("https://example.com/imagem_scalping.png", "Scalping")




        elif subsecao == "Futures Intermarket Spreads":
            st.markdown("""
                **Futures Intermarket Spreads**

                Intermarket spreads em contratos futuros envolvem pares de ativos subjacentes diferentes. Embora seja difícil encontrar spreads com comportamento de reversão à média, existem alguns candidatos interessantes, especialmente em mercados inter-relacionados.

                ### Exemplos de Spreads em Mercados de Energia
                1. **Crack Spread (CL, RB e HO)**:
                - Consiste em uma carteira formada por três contratos longos de WTI crude oil (CL), dois contratos short de gasolina (RB) e um contrato short de óleo de aquecimento (HO).
                - Representa a relação entre a produção de derivados a partir do petróleo bruto, onde a proporção 3:2:1 reflete a produção média de refinarias.
                - **Resultado do Teste ADF**: Não estacionário. Durante o período de 2007-2008, apresentou alta volatilidade e retornos negativos em estratégias de reversão à média.
                - **Vantagem Operacional**: A NYMEX oferece uma cesta pronta para o crack spread, reduzindo os requisitos de margem em comparação com negociações separadas.

                2. **Spread entre CL e BZ (1:1)**:
                - Ambas as commodities representam petróleo bruto (WTI e Brent), sugerindo uma relação forte.
                - **Resultado do Teste ADF**: Não estacionário, devido a fatores como:
                    - Aumento da produção de petróleo nos EUA.
                    - Gargalos nos oleodutos em Cushing, Oklahoma.
                    - Questões geopolíticas, como o embargo ao petróleo iraniano, que impactaram o Brent (BZ) mais do que o WTI (CL).

                ### Cuidados no Backtesting de Intermarket Spreads
                1. **Sincronização de Preços**: Certifique-se de que os preços sejam registrados no mesmo horário. Antes de setembro de 2001, o Brent (BZ) era negociado na Intercontinental Petroleum Exchange em Londres, com horário de fechamento diferente do NYMEX, onde o WTI (CL) é negociado.
                2. **Ajustes para USD**: Futuros podem exigir multiplicadores para converter os preços para dólares americanos, garantindo consistência nos cálculos.

                ### Conclusão
                Embora intermarket spreads sejam promissores em mercados relacionados, como energia, a falta de estacionariedade torna muitos deles inadequados para estratégias de reversão à média. A análise cuidadosa e a consideração de fatores como sincronização de preços são essenciais para evitar erros em backtests e estratégias.
                """)

            mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")

# ===================== Chapter 7 Interday Momentum Strategies =============





# ====================================================================================

# ==================== Chapter 8 - Gestão de Risco ========================

    elif pagina == "9 . Gestão de Riscos":
        st.title("Gestão de Risco")

        if subsecao == "Introdução":
            st.markdown("""
            A gestão de risco é interpretada de maneiras variadas, mas geralmente está associada à aversão a perdas, um comportamento emocional amplamente discutido por Kahneman (2011). Apesar de compreensível, essa aversão nem sempre é racional, pois o objetivo central deve ser a maximização do crescimento do patrimônio no longo prazo.

            Uma gestão de risco eficaz exige o uso prudente da alavancagem, que pode ser otimizada por ferramentas como a fórmula de Kelly, projetada para maximizar a taxa de crescimento composta do capital. Além disso, estratégias como stop loss e constant proportion portfolio insurance (CPPI) são frequentemente implementadas para limitar perdas severas. O CPPI, em particular, busca equilibrar a proteção contra perdas significativas e a maximização de ganhos potenciais.

            Outra abordagem relevante é a de evitar operar em condições adversas, identificando períodos de maior probabilidade de perdas por meio de indicadores de risco. Essa prática permite uma alocação mais eficiente do capital, preservando recursos para momentos mais favoráveis.
            """)

        elif subsecao == "Alavancagem":
            st.markdown(r"""
            ## Optimal Leverage (Alavancagem Ótima)

            A alavancagem, embora seja uma ferramenta poderosa para potencializar os retornos de uma estratégia de trading, traz consigo desafios significativos. A questão central é como determinar a alavancagem ideal para maximizar os retornos, sem correr riscos excessivos. Se a alavancagem for zero, não haverá risco, mas também não se gerará nenhum retorno. Portanto, é essencial encontrar o ponto de equilíbrio.

            Para muitos gestores, especialmente os que administram seus próprios fundos, o objetivo principal é maximizar o crescimento do patrimônio ao longo do tempo. Eles tendem a ignorar volatilidades e quedas de curto prazo. Para esses traders, a alavancagem ótima é aquela que maximiza a taxa de crescimento composta do portfólio, mantendo o risco sob controle.

            Existem várias abordagens para calcular a alavancagem ótima, sendo que a maioria delas se baseia na suposição de que a distribuição dos retornos futuros será semelhante à dos retornos passados. Embora essa premissa não seja completamente precisa, ela é amplamente utilizada em modelos quantitativos. A fórmula de Kelly, por exemplo, assume uma distribuição Gaussiana e oferece uma solução simples para calcular a alavancagem ideal que maximiza o crescimento composto, sem levar a uma perda total do capital (ruína).
            
            ---
                        
            """)

            latext = r'''
            ### A fórmula de Kelly

            A **Fórmula de Kelly** é amplamente utilizada em finanças e estratégias de trading para determinar o nível ótimo de alavancagem e maximizar o crescimento composto do capital. Ela é especialmente relevante quando assumimos que os retornos seguem uma distribuição aproximadamente Gaussiana (normal). O uso da Fórmula de Kelly foi popularizado por Edward Thorp e explorado em profundidade no livro *Quantitative Trading* (Chan, 2009).

            A **Fórmula de Kelly** determina o nível ótimo de alavancagem \( f \) usando a seguinte equação:

            $$
            f = \frac{m}{\sigma^2}
            $$

            Onde:

            - $$ m $$ é o retorno médio excedente (*mean excess return*);
            - $${\sigma^2}$$ é a variância dos retornos excedentes.

            Se assumirmos que os retornos seguem uma distribuição normal (*Gaussiana*), o valor \( f \) calculado pela **Fórmula de Kelly** maximiza a taxa de crescimento composta do capital ao longo do tempo, desde que todos os lucros sejam reinvestidos.
            '''
            st.write(latext)


            code = '''
                import yfinance as yf
                import numpy as np

                def kelly_formula(ticker, risk_free_rate=0.02, start_date="2010-01-01", end_date="2024-12-31"):
                    # Baixar dados históricos do Yahoo Finance
                    data = yf.download(ticker, start=start_date, end=end_date)

                    # Calcular os retornos diários
                    data['Daily Return'] = data['Adj Close'].pct_change()

                    # Calcular o retorno médio excedente (m) e a variância dos retornos excedentes (s^2)
                    excess_returns = data['Daily Return'] - (risk_free_rate / 252)  # Ajustar taxa livre de risco para base diária
                    mean_excess_return = np.mean(excess_returns)
                    variance_excess_return = np.var(excess_returns)

                    # Aplicar a Fórmula de Kelly
                    if variance_excess_return > 0:
                        optimal_leverage = mean_excess_return / variance_excess_return
                    else:
                        optimal_leverage = 0  # Evitar divisão por zero

                    # Exibir resultados
                    print(f"Ticker: {ticker}")
                    print(f"Retorno médio excedente (m): {mean_excess_return:.6f}")
                    print(f"Variância dos retornos excedentes (s^2): {variance_excess_return:.6f}")
                    print(f"Alavancagem ótima (f): {optimal_leverage:.2f}")

                    return optimal_leverage

                # Exemplo de uso
                ticker_symbol = "MSFT"  # Símbolo da ação, ex: AAPL para Apple, MSFT para Microsoft
                optimal_leverage = kelly_formula(ticker_symbol)

            ====================== Output ============================
                Retorno médio excedente (m): 0.000820
                Variância dos retornos excedentes (s^2): 0.000259
                Alavancagem ótima (f): 3.16
            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1oomGr66P92TigEEDKj5b7bkmaxkHSa_v?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            st.write(r"""
                     
            ---           
            ### Monte Carlo Simulation and Leverage Optimization         

            Para determinar a alavancagem ótima em distribuições não-Gaussianas, a fórmula de Kelly pode não ser suficiente. Nessas situações, simulações de Monte Carlo ajudam a estimar o crescimento composto esperado. Considerando que a taxa livre de risco é zero, a fórmula para o crescimento composto esperado em função da alavancagem \(f\) é:

            """)

            st.latex(r"g(f) = \langle \log(1 + fR) \rangle")

            st.write("""
            Onde \( R(t) \) é o retorno diário (ou em qualquer período definido) da estratégia, e \( \langle ... \rangle \) representa a média sobre amostras aleatórias da distribuição de \( R \). Se a distribuição for Gaussiana, a fórmula se reduz a:

            """)

            st.latex(r"g(f) = fm - \frac{f^2 m^2}{2}")

            st.write("""
            Essa fórmula é equivalente à da alavancagem de Kelly em distribuições Gaussianas, onde o máximo de \( g(f) \) pode ser encontrado derivando a equação com relação a \( f \) e igualando a zero. No entanto, para distribuições não-Gaussianas, como as modeladas pelo sistema de Pearson, a solução analítica pode ser impossível.

            O **Sistema de Pearson** utiliza a média, desvio padrão, assimetria e curtose da distribuição empírica para ajustá-la a uma das sete distribuições parametrizadas, incluindo Gaussiana, beta, gamma e Student's t. Embora não capture todos os momentos superiores ou distribuições infinitas, é suficiente para evitar viés por excesso de ajuste em dados limitados.

            ### Exemplo prático

            1. **Cálculo inicial**: Usando retornos diários, a alavancagem de Kelly foi calculada como 18,4.
            2. **Simulação de Monte Carlo**: Baseando-se nos quatro primeiros momentos dos retornos, 100.000 retornos aleatórios foram gerados com o sistema de Pearson usando a função `pearsrnd` do MATLAB.
            3. **Resultados**: A técnica foi aplicada à estratégia de reversão à média descrita no exemplo 5.1, permitindo uma comparação direta entre a alavancagem de Kelly e os resultados da simulação.

            Essas simulações fornecem insights valiosos para otimizar alavancagem em condições de mercado reais, onde as distribuições de retorno frequentemente não seguem uma forma Gaussiana.
            """)


            # ==========================

            st.write(r"""
                      
            ---         

            ### Optimization of Historical Growth Rate
                     
            Em vez de otimizar o valor esperado da taxa de crescimento usando uma distribuição analítica de probabilidades dos retornos, como feito anteriormente, podemos simplesmente otimizar a taxa de crescimento histórica no backtest em relação à alavancagem. 

            Este método requer apenas um conjunto específico de retornos: aqueles que realmente ocorreram no backtest. Contudo, essa abordagem apresenta limitações significativas:

            - **Viés de Data-Snooping**: A otimização nos retornos históricos pode levar a um ajuste excessivo aos dados, resultando em uma alavancagem que não será ideal para realizações futuras.
            - **Generalização Limitada**: A alavancagem ótima encontrada para a realização histórica pode não ser aplicável a outras realizações futuras da estratégia.

            Apesar dessas limitações, em alguns casos, a otimização direta sobre os retornos históricos pode produzir resultados semelhantes à alavancagem de Kelly e à otimização baseada em Monte Carlo.

            Método Prático

            Usando a mesma estratégia mencionada anteriormente, podemos alterar o programa de otimização para utilizar os retornos históricos  no lugar dos retornos simulados. Embora essa abordagem possa fornecer insights rápidos, é importante interpretar os resultados com cautela devido aos problemas inerentes ao uso exclusivo de dados históricos.

            Considerações Finais

            Essa técnica pode ser útil como complemento a métodos mais robustos, como simulações de Monte Carlo, especialmente quando aplicada em conjunto com validações cruzadas ou outros mecanismos para mitigar o viés de ajuste aos dados históricos.
            """)

            st.markdown(""" 
            ---             

            ### Drawdown

            Embora a alavancagem ótima deva maximizar o crescimento composto, muitos traders impõem restrições ao nível de drawdown, ou seja, a perda máxima permitida em relação ao valor do portfólio. Isso é feito para proteger o portfólio de perdas excessivas e manter o risco em níveis aceitáveis. Quando esse limite é estabelecido, o cálculo da alavancagem ótima deve ser ajustado para garantir que a perda máxima não seja ultrapassada.

            Drawdown representa a redução percentual entre o valor máximo atingido pelo portfólio e o seu valor mínimo subsequente, antes que ele volte a crescer. Em outras palavras, é a maior queda sofrida pelo portfólio durante um determinado período. Por exemplo, se o valor do portfólio sobe para 100 mil e em seguida cai para 80 mil, o drawdown será de 20%.

            O drawdown é uma métrica crucial para avaliar o risco de uma estratégia de investimento ou trading. Ele permite entender não apenas o quanto uma estratégia pode perder em momentos de adversidade, mas também como isso pode impactar a capacidade do investidor de permanecer fiel ao plano inicial. Estratégias com drawdowns elevados podem ser insustentáveis a longo prazo, pois podem levar a decisões emocionais, como resgates antecipados ou abandonos de estratégias rentáveis.

            Portanto, ao ajustar a alavancagem para respeitar um nível aceitável de drawdown, os traders buscam equilibrar o crescimento do portfólio com a proteção contra perdas significativas, garantindo assim uma gestão de risco mais robusta.
                        
            ---                      
            """)

            st.markdown("""
                ### Constant Proportion Portfolio Insurance (CPPI)**

                O método CPPI combina o objetivo de maximizar a taxa de crescimento composta com a limitação de perdas máximas (drawdown). Ele separa o capital total em duas partes: uma subconta alocada para negociação e uma conta em caixa. A subconta recebe uma alocação equivalente a uma proporção fixa **D** do capital total, e uma alavancagem **f** é aplicada apenas nessa subconta. Isso garante que o drawdown máximo não exceda **-D** do capital total.  

                ### Funcionamento do CPPI
                1. **Alocação Inicial**:
                - Aloca **D** do capital total para a subconta de negociação.
                - O restante (**1-D**) permanece em caixa para proteger contra perdas.
                2. **Reajuste do Capital**:
                - Quando o capital total atinge um novo pico, a subconta é reajustada para manter a proporção **D**.  
                - Em caso de perdas, o capital não é transferido da conta de caixa para a subconta.
                3. **Encerramento da Estratégia**:
                - Caso a subconta perca todo o seu capital, a estratégia é abandonada, servindo como um mecanismo automático de contenção de riscos.

                ##### Comparação com Alavancagem Reduzida
                Embora pareça semelhante ao uso de uma alavancagem reduzida (**fD**), o CPPI ajusta dinamicamente o tamanho das ordens, reduzindo o risco de atingir o drawdown máximo. Isso também evita o comportamento emocional no encerramento de estratégias.  

                ##### Vantagens do CPPI
                - Limitação do drawdown ao valor projetado (**-D**) por design.
                - Taxa de crescimento composta similar a estratégias com alavancagem reduzida, mesmo após períodos longos.  
                - Redução mais rápida do tamanho das posições em períodos de drawdown, protegendo o capital restante.

                ##### Limitações do CPPI
                - Não oferece proteção contra grandes gaps de mercado ou suspensões de negociação. O uso de opções fora do dinheiro pode mitigar esse risco.  
                - Deve ser aplicado a contas com apenas uma estratégia, pois estratégias não lucrativas podem ser "subsidiadas" por outras em contas multiestratégias, mascarando os drawdowns reais.

                O CPPI é uma abordagem eficiente para maximizar o crescimento composto enquanto limita drawdowns, oferecendo um método disciplinado e automático para controlar riscos. No entanto, é necessário atenção para lidar com eventos fora do controle, como gaps de mercado.
                """)
            
            mostrar_imagem("img/cppi.png", "Constant Proportion Portfolio Insurance (CPPI)")

            colab_link = "https://colab.research.google.com/drive/1oomGr66P92TigEEDKj5b7bkmaxkHSa_v?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()
            st.write("""
    
            ### Conclusão

            A alavancagem ótima deve equilibrar os retornos desejados com o risco de perdas excessivas, respeitando limitações de drawdown. Embora a alavancagem constante seja fundamental para otimizar o crescimento composto, ela pode gerar efeitos negativos, especialmente durante crises. Por isso, é importante gerenciar cuidadosamente os níveis de risco e estar ciente das implicações dessa estratégia no longo prazo.

            """)

        elif subsecao == "Indicadores e métricas":
            st.markdown("""    
            Os indicadores de risco proativos ajudam a evitar períodos desfavoráveis para estratégias de trading ao antecipar riscos. Diferentes indicadores são eficazes dependendo da estratégia utilizada:

            ##### VIX:
            O índice de volatilidade implícita é útil para identificar riscos. Em estratégias como buy-on-gap, um VIX acima de 35 pode indicar alta rentabilidade, enquanto para outras, como gap de abertura FSTX, ele sinaliza períodos a serem evitados.

            ##### TED Spread:
            Mede o risco de default bancário ao calcular a diferença entre a taxa LIBOR de três meses e os T-bills. É especialmente relevante em crises financeiras, como em 2008, quando atingiu níveis recordes.

            ##### Ativos de Risco: 
            ETFs de high-yield bonds (HYG) e moedas emergentes, como o peso mexicano (MXN), funcionam como indicadores em crises específicas. O MXN, por exemplo, serviu como proxy para ativos arriscados durante a crise europeia de 2011.

            ##### Fluxo de Ordens: 
            Mudanças abruptas no fluxo de ordens indicam que informações importantes chegaram a investidores institucionais. Isso afeta negativamente ativos de risco (ações, commodities) e positivamente ativos seguros (USD, JPY, CHF).

            ##### Indicadores Específicos:
            Preços de commodities, como petróleo e ouro, são bons preditores para pair trading entre ETFs de produtores e mineradoras. O Índice Baltic Dry também pode antecipar riscos em países exportadores.

            Apesar da eficácia desses indicadores, crises financeiras são raras, o que aumenta o risco de viés de seleção de dados em backtests. Além disso, eventos imprevisíveis, como desastres naturais, não podem ser antecipados. O fluxo de ordens, por atuar em alta frequência, é uma das ferramentas mais úteis para antecipar mudanças de mercado com precisão.

            Em resumo, combinar indicadores como VIX, TED Spread, fluxo de ordens e ativos específicos permite mitigar riscos e aumentar a eficácia de estratégias de trading. A escolha do indicador deve ser validada rigorosamente para evitar vieses e garantir sua confiabilidade.
                        
            #### Stop Loss
           
            Stop loss pode ser utilizado de duas maneiras: a mais comum é para sair de uma posição existente quando o lucro/prejuízo não realizado atinge um limite negativo, permitindo reentradas futuras. A segunda, menos comum, é usar o stop loss para encerrar completamente uma estratégia caso o drawdown ultrapasse um limite, o que é raro e pouco prático. O stop loss é eficaz apenas em mercados sempre abertos, pois gaps de preços após fechamentos podem resultar em perdas maiores. Em condições extremas, como na crise de liquidez durante o flash crash de 2010, o stop loss pode falhar completamente. Para estratégias de reversão à média, o stop loss pode parecer contraditório, pois se espera que os preços voltem ao normal, mas falha ao considerar mudanças permanentes no comportamento do mercado. Caso ocorra uma mudança de regime, o stop loss pode prevenir perdas catastróficas, sendo mais útil se configurado acima do drawdown máximo do backtest. Já estratégias de momentum se beneficiam logicamente do stop loss, pois perdas indicam reversão do momento, justificando a saída ou reversão da posição.

            """)
            code_3 = '''
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# Baixar os dados do portfólio
ticker = "^GSPC"  # Altere para o ticker desejado

data = yf.download(ticker, start="2015-01-01", end="2023-01-01")
valor_carteira = data['Close']

# Calcular o retorno diário
portfolio_returns = valor_carteira.pct_change().dropna()

# Calcular a volatilidade diária e anualizada
daily_volatility = portfolio_returns.std()
annualized_volatility = daily_volatility * np.sqrt(252)

# Função para calcular o drawdown
def calculate_drawdown(portfolio_values):
    peaks = np.maximum.accumulate(portfolio_values)
    drawdowns = (portfolio_values - peaks) / peaks
    max_drawdown = np.min(drawdowns)
    return drawdowns, max_drawdown

drawdowns, max_drawdown = calculate_drawdown(valor_carteira)

# Calcular o Sharpe Ratio
risk_free_rate = 0.02  # Suponha uma taxa livre de risco anual de 2%
daily_risk_free_rate = (1 + risk_free_rate) ** (1/252) - 1  # Ajustar para base diária
excess_returns = portfolio_returns - daily_risk_free_rate
sharpe_ratio = np.mean(excess_returns) / daily_volatility * np.sqrt(252)  # Ajustar para base anual

# Retorno final
final_return = (valor_carteira.iloc[-1] / valor_carteira.iloc[0] - 1) * 100

# Exibir os resultados
print(f"Volatilidade diária: {daily_volatility}")
print(f"Volatilidade anualizada: {annualized_volatility}")
print(f"Drawdown máximo: {max_drawdown}")
print(f"Sharpe Ratio: {sharpe_ratio}")
print(f"Retorno final: {final_return}%")

            '''
            
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1pjlRF6K4fteMMaeoqGqNluNaiQMO_oFU?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            mostrar_imagem("img/risk_ind.png", "Risk Indicators")

        elif subsecao == "Conclusão":

            st.write("### Maximization of Long-Term Growth Rate and Risk Management")
            st.write("""
            Para maximizar o crescimento composto e gerenciar riscos em estratégias de trading, considere as seguintes abordagens:

            ### 1. Maximização da Taxa de Crescimento de Longo Prazo

            - **Uso da Alavancagem Ótima (Half-Kelly)**:
            - Se o objetivo é maximizar o patrimônio líquido no longo prazo, a alavancagem de meio-Kelly pode oferecer um equilíbrio entre risco e retorno.

            - **Distribuições de Retorno Assimétricas**:
            - Estratégias com retornos de caudas grossas (fat-tailed) devem evitar a fórmula de Kelly pura.
            - Utilize simulações de Monte Carlo para calcular a alavancagem ótima e evitar resultados extremos.

            - **Otimização Direta em Backtests**:
            - Você pode otimizar a alavancagem diretamente com base na taxa de crescimento composta dos retornos históricos.
            - Cuidado com o viés de data-snooping ao confiar exclusivamente nos backtests.

            - **Limitação de Drawdowns com CPPI**:
            - Para limitar o drawdown máximo e ainda maximizar o crescimento, utilize a técnica de Constant Proportion Portfolio Insurance (CPPI).

            ---

            ### 2. Stop Loss

            - **Estratégias de Reversão à Média**:
            - Stop loss geralmente reduz o desempenho nos backtests devido ao viés de sobrevivência.
            - Configure stop loss de forma que não sejam acionados nos backtests, prevenindo eventos de cisne negro.

            - **Estratégias de Momentum**:
            - O uso de stop loss é natural e parte lógica das estratégias de momentum.

            ---

            ### 3. Indicadores de Risco

            - **Indicadores Líderes de Risco**:
            - Considere o uso de indicadores como: VIX, TED spread, HYG, ONN/OFF, MXN.
            - Teste cuidadosamente esses indicadores para evitar viés de data-snooping.

            - **Fluxo de Ordem Negativo**:
            - Um fluxo de ordem cada vez mais negativo de ativos arriscados pode servir como um indicador de risco de curto prazo.

            ---

            ### Conclusão

            Para maximizar o crescimento composto e gerenciar riscos, é essencial equilibrar alavancagem, controle de drawdowns e uso de ferramentas como CPPI, stop loss e indicadores de risco. Testes robustos e validações rigorosas são cruciais para evitar armadilhas de viés e tomar decisões bem informadas.
            """)

# ==================== Chapter 8 - Gestão de Risco ========================

# ==================== Conclusão ========================

    elif pagina == "10 . Conclusão":

        st.title("Conclusão - Princípios Fundamentais do Trading Algorítmico")

        # Texto completo
        st.write("""
        ### 1. Estratégias Não Como Receitas, Mas Como Fundamentos
        O objetivo principal não é fornecer estratégias prontas, mas ilustrar **princípios fundamentais**:
        - **Identificar ineficiências de mercado**:
            - Regressão à média.
            - Retornos de rolagem em futuros.
            - Necessidade de rebalanceamento em ETFs alavancados.
        - A partir dessas ineficiências, criar estratégias simples e eficazes para explorá-las.

        ---

        ### 2. Abordagem Científica ao Trading Algorítmico
        A abordagem ao trading deve seguir um processo científico:
        1. **Formular hipóteses** sobre o mercado.
        2. Criar um **modelo quantitativo**.
        3. Testar o modelo em dados novos e não vistos.
        4. Identificar causas de falhas e ajustar variáveis.

        **Exemplo:** 
        - A cointegração entre GLD e GDX falhou em 2008 devido ao preço elevado do petróleo.
        - Ao adicionar o preço do petróleo como variável, o modelo voltou a funcionar.

        A investigação de **razões fundamentais** para falhas é mais eficaz do que adicionar regras ou indicadores arbitrários.

        ---

        ### 3. Juízo Subjetivo no Trading Algorítmico
        Apesar da base científica, decisões subjetivas são inevitáveis:
        - **Eventos extremos**: Confiar no modelo ou reduzir alavancagem antes de crises?
        - **Distribuição de capital**:
            - Alocar com base no portfólio total (subsidia estratégias temporariamente fracas).
            - Alocar por estratégia individual (reduz rapidamente a alocação em estratégias fracas).

        **Experiência do autor:**
        - Use alavancagem conservadora em tempos bons para evitar cortes em tempos ruins.
        - Aplique Kelly individualmente para estratégias, eliminando aquelas com baixo desempenho.

        ---

        ### 4. Mercados Não-Estacionários e Mudanças de Regime
        Diferenças entre backtest e trading ao vivo geralmente são causadas por **mudanças estruturais** no mercado, como:
        - Regulações governamentais.
        - Alterações macroeconômicas.

        Mesmo em estratégias automatizadas, os gestores desempenham um papel crucial:
        - Fazer julgamentos de alto nível sobre a validade dos modelos.

        ---

        ### 5. Superioridade de Algoritmos Sobre Julgamento Humano
        Como destacado por Daniel Kahneman:
        - Em ambientes de alta incerteza, **algoritmos superam especialistas**.
        - Mercados financeiros provavelmente seguem essa regra.

        Desenvolver estratégias simples, baseadas em fundamentos, e testá-las rigorosamente são práticas-chave para o sucesso.
        """)

# ==================== Conclusão ========================

# ==================== Referências ========================

    elif pagina == "Referências":

        st.title("Referências")

        # Texto completo
        st.write("""
                 
1. CHAN, Ernie. Algorithmic trading: winning strategies and their rationale. John Wiley & Sons, 2013.
2. https://github.com/AnjayGoel/algorithmic-trading/tree/master       
        
        """)

# ==================== Referências ========================



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