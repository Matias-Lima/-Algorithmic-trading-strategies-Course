import streamlit as st

# Configuração da página
st.set_page_config(page_title="Guia Conceitual - Trading", layout="wide")

# Função para exibir imagens
def mostrar_imagem(imagem_path, legenda):
    st.image(imagem_path, caption=legenda, use_column_width=True)

# Barra lateral com subseções hierárquicas
st.sidebar.markdown("""
<h2>Seções</h2>
<ol type="A">
  <li><a href="#arquitetura">Arquitetura</a>
    <ul>
      <li><a href="#introducao-arquitetura">Introdução</a></li>
      <li><a href="#analise-tecnica">Análise Técnica</a></li>
      <li><a href="#analise-fundamentalista">Análise Fundamentalista</a></li>
      <li><a href="#day-trading">Day Trading</a></li>
      <li><a href="#swing-trading">Swing Trading</a></li>
    </ul>
  </li>
  <li><a href="#indicadores">Indicadores</a>
    <ul>
      <li><a href="#introducao-indicadores">Introdução</a></li>
      <li><a href="#medias-moveis">Médias Móveis</a></li>
      <li><a href="#rsi">RSI</a></li>
      <li><a href="#macd">MACD</a></li>
    </ul>
  </li>
  <li><a href="#taticas">Táticas</a>
    <ul>
      <li><a href="#introducao-taticas">Introdução</a></li>
      <li><a href="#tape-reading">Tape Reading</a></li>
      <li><a href="#scalping">Scalping</a></li>
      <li><a href="#estrategias-rompimento">Estratégias de Rompimento</a></li>
    </ul>
  </li>
  <li><a href="#pacotes-relacionados">Pacotes Relacionados</a>
    <ul>
      <li><a href="#introducao-pacotes">Introdução</a></li>
      <li><a href="#backtrader">Backtrader</a></li>
      <li><a href="#quantconnect">QuantConnect</a></li>
      <li><a href="#zipline">Zipline</a></li>
    </ul>
  </li>
</ol>
""", unsafe_allow_html=True)

# Corpo da página
st.markdown('<h2 id="arquitetura">Arquitetura</h2>', unsafe_allow_html=True)
st.markdown("""
### Introdução
Aqui explicaremos os conceitos centrais do trading, incluindo análise técnica e fundamentalista, com diferentes estratégias para day trading e swing trading.
""")
st.markdown('<h3 id="introducao-arquitetura">Introdução</h3>', unsafe_allow_html=True)
st.markdown("""
Aqui explicaremos os conceitos centrais do trading, incluindo análise técnica e fundamentalista, com diferentes estratégias para day trading e swing trading.
""")
st.markdown('<h3 id="analise-tecnica">Análise Técnica</h3>', unsafe_allow_html=True)
st.markdown("""
A análise técnica envolve o estudo dos gráficos de preços e a utilização de indicadores técnicos para prever movimentos futuros.
""")
mostrar_imagem("https://example.com/imagem_analise_tecnica.png", "Análise Técnica")
st.markdown('<h3 id="analise-fundamentalista">Análise Fundamentalista</h3>', unsafe_allow_html=True)
st.markdown("""
A análise fundamentalista se concentra em avaliar o valor intrínseco de um ativo com base em dados econômicos e financeiros.
""")
mostrar_imagem("https://example.com/imagem_analise_fundamentalista.png", "Análise Fundamentalista")
st.markdown('<h3 id="day-trading">Day Trading</h3>', unsafe_allow_html=True)
st.markdown("""
Day trading refere-se a estratégias que envolvem a compra e venda de ativos no mesmo dia.
""")
mostrar_imagem("https://example.com/imagem_day_trading.png", "Day Trading")
st.markdown('<h3 id="swing-trading">Swing Trading</h3>', unsafe_allow_html=True)
st.markdown("""
Swing trading é uma abordagem que visa capturar movimentos de preço em um período médio de tempo.
""")
mostrar_imagem("https://example.com/imagem_swing_trading.png", "Swing Trading")

st.markdown('<h2 id="indicadores">Indicadores</h2>', unsafe_allow_html=True)
st.markdown("""
Exploração dos principais indicadores como médias móveis, RSI, e MACD. Esses indicadores ajudam a identificar tendências e momentos para entrar ou sair de posições.
""")
st.markdown('<h3 id="introducao-indicadores">Introdução</h3>', unsafe_allow_html=True)
st.markdown("""
Exploração dos principais indicadores como médias móveis, RSI, e MACD. Esses indicadores ajudam a identificar tendências e momentos para entrar ou sair de posições.
""")
st.markdown('<h3 id="medias-moveis">Médias Móveis</h3>', unsafe_allow_html=True)
st.markdown("""
Médias móveis são usadas para suavizar os dados de preços e identificar tendências.
""")
mostrar_imagem("https://example.com/imagem_median_moveis.png", "Médias Móveis")
st.markdown('<h3 id="rsi">RSI</h3>', unsafe_allow_html=True)
st.markdown("""
O Índice de Força Relativa (RSI) é um indicador de momentum que mede a velocidade e a mudança dos movimentos de preços.
""")
mostrar_imagem("https://example.com/imagem_rsi.png", "RSI")
st.markdown('<h3 id="macd">MACD</h3>', unsafe_allow_html=True)
st.markdown("""
O MACD (Moving Average Convergence Divergence) é um indicador de tendência que mostra a relação entre duas médias móveis.
""")
mostrar_imagem("https://example.com/imagem_macd.png", "MACD")

st.markdown('<h2 id="taticas">Táticas</h2>', unsafe_allow_html=True)
st.markdown("""
Explanação sobre as táticas mais usadas pelos traders, como tape reading, scalping e estratégias de rompimento.
""")
st.markdown('<h3 id="introducao-taticas">Introdução</h3>', unsafe_allow_html=True)
st.markdown("""
Explanação sobre as táticas mais usadas pelos traders, como tape reading, scalping e estratégias de rompimento.
""")
st.markdown('<h3 id="tape-reading">Tape Reading</h3>', unsafe_allow_html=True)
st.markdown("""
Tape reading é uma técnica que envolve a leitura do fluxo de ordens e do livro de ofertas para prever movimentos de preços.
""")
mostrar_imagem("https://example.com/imagem_tape_reading.png", "Tape Reading")
st.markdown('<h3 id="scalping">Scalping</h3>', unsafe_allow_html=True)
st.markdown("""
Scalping é uma estratégia de curto prazo que busca obter pequenos lucros a partir de movimentos de preços muito pequenos.
""")
mostrar_imagem("https://example.com/imagem_scalping.png", "Scalping")
st.markdown('<h3 id="estrategias-rompimento">Estratégias de Rompimento</h3>', unsafe_allow_html=True)
st.markdown("""
Estratégias de rompimento envolvem a identificação e a negociação de momentos em que o preço ultrapassa níveis importantes de suporte ou resistência.
""")
mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")

st.markdown('<h2 id="pacotes-relacionados">Pacotes Relacionados</h2>', unsafe_allow_html=True)
st.markdown("""
**Ferramentas de backtesting**  
Essas ferramentas permitem simular estratégias de trading usando dados históricos, o que ajuda os traders a entenderem a eficácia de suas abordagens antes de colocá-las em prática.
""")
st.markdown('<h3 id="introducao-pacotes">Introdução</h3>', unsafe_allow_html=True)
st.markdown("""
**Ferramentas de backtesting**  
Essas ferramentas permitem simular estratégias de trading usando dados históricos, o que ajuda os traders a entenderem a eficácia de suas abordagens antes de colocá-las em prática.
""")
st.markdown('<h3 id="backtrader">Backtrader</h3>', unsafe_allow_html=True)
st.markdown("""
Backtrader é uma plataforma de backtesting que permite testar e otimizar estratégias de trading.
""")
mostrar_imagem("https://example.com/imagem_backtrader.png", "Backtrader")
st.markdown('<h3 id="quantconnect">QuantConnect</h3>', unsafe_allow_html=True)
st.markdown("""
QuantConnect oferece uma plataforma de backtesting e desenvolvimento de estratégias com suporte para múltiplas classes de ativos.
""")

