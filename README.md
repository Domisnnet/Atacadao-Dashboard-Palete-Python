![Repo Size](https://img.shields.io/github/repo-size/Domisnnet/Atacadao-Dashboard-Palete-Python?style=flat&label=REPO%20SIZE&labelColor=2d333b&color=0969da)
![Stars](https://img.shields.io/github/stars/Domisnnet/Atacadao-Dashboard-Palete-Python?style=flat&label=STARS&labelColor=2d333b&color=0969da)
![Last Commit](https://img.shields.io/github/last-commit/Domisnnet/Atacadao-Dashboard-Palete-Python?style=flat&label=LAST%20COMMIT&labelColor=2d333b&color=2ea44f)
![Version](https://img.shields.io/github/package-json/v/Domisnnet/Atacadao-Dashboard-Palete-Python?style=flat&label=VERSION&labelColor=2d333b&color=0969da&logo=python&logoColor=white)

<h2 id="sobre-o-projeto">1. 📊 BI-Python: Inteligência de Dados:</h2>

![Status do Deploy](https://img.shields.io/badge/Status-Online-brightgreen?style=flat&logo=firebase&logoColor=white)
![Tech](https://img.shields.io/badge/Tech-Python%20%7C%20Streamlit%20%7C%20Plotly-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Data](https://img.shields.io/badge/Data-Pandas-yellow?style=flat-square&logo=pandas)
![Imagem Dashboard](/assets/images/dashboard-preview.png)

> Bem-vindo ao `Atacadão Dashboard de Paletes!` Uma solução de Business Intelligence `Open Source` desenvolvida para otimizar o controle de estoque de paletes no Centro de Distribuição - CD. O projeto visa resolver a dor da rastreabilidade de NFs com devoluções parciais de motoristas, utilizando dados extraídos do sistema `Cerberus.`

---

## 📚 Tabela de Conteúdo

| 📊 O Projeto | 🛠️ Técnico | 🤝 Comunidade |
| :---: | :---: | :---: |
| [![1. Sobre](https://img.shields.io/badge/1%20-%20Sobre-4CAF50)](#sobre-o-projeto) | [![5. Destaques](https://img.shields.io/badge/5%20-%20Destaques-607D8B)](#destaques-tecnicos) | [![9. Código](https://img.shields.io/badge/9%20-%20Código-795548)](#codigo-fonte) |
| [![2. Techs](https://img.shields.io/badge/2%20-%20Techs-2196F3)](#tecnologias-utilizadas) | [![6. Estrutura](https://img.shields.io/badge/6%20-%20Estrutura-009688)](#estrutura-do-projeto) | [![10. Créditos](https://img.shields.io/badge/10%20-%20Créditos-607D8B)](#créditos) |
| [![3. Rodar](https://img.shields.io/badge/3%20-%20Rodar-FF9800)](#como-rodar-localmente) | [![7. Contribuir](https://img.shields.io/badge/7%20-%20Contribuir-3F51B5)](#como-contribuir) | [![11. Licença](https://img.shields.io/badge/11%20-%20Licença-E91E63)](#licenca) |
| [![4. Insights](https://img.shields.io/badge/4%20-%20Insights-9C27B0)](#insights-principais) | [![8. FAQ](https://img.shields.io/badge/8%20-%20FAQ-FFC107)](#faq) | [![12. Perfil](https://img.shields.io/badge/12%20-%20Perfil-212121)](#perfil-do-github) |

---

<h2 id="sobre-o-projeto">1. BI-Python: Inteligência de Dados 📊</h2>

No setor de Recebimento de Mercadorias, o controle manual de paletes gera duas dores principais:
1. **Retenção de Paletes:** Motoristas que não levam todos os paletes de volta deixam um "saldo retido" no CD. No caso do CHEP , isso impacta diretamente no custo financeiro.
2. **Rastreabilidade:** Dificuldade em referenciar qual Nota Fiscal - NF , de entrada , originou aquela retenção parcial, dificultando cobranças futuras ou devoluções em lote.

Este Dashboard atua como uma camada de inteligência sobre os dados do Sistema. Através da exportação de relatórios em CSV, o script em Python cruza as informações , calcula o saldo retido e cria um **Status de Rastreamento** vinculado à NF original.

---

<h2 id="tecnologias-utilizadas">2. ⚙️ Tecnologias Utilizadas</h2>

| Camada | Tecnologias | Descrição |
| :--- | :--- | :--- |
| **Linguagem** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core da análise e lógica de ETL. |
| **Processamento** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Tratamento de dados, cálculos de saldo e agrupamentos. |
| **Dashboard** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Interface web interativa e responsiva. |
| **Visualização** | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) | Gráficos dinâmicos e interativos. |

---

<h2 id="como-acessar">3. 🚀 Como Acessar</h2>

Clique no botão abaixo para iniciar o Verificador de Idade diretamente no seu navegador:

<div align="left">
  <a href="https://domisnnet.github.io/Age-Checker-Web-Essentials/" target="_blank">
    <img alt="Botão Acessar" src="/assets/images/botão.webp" height="70" width="70" />
  </a>
</div>


---

<h2 id="funcionalidades">4. 🧩 Funcionalidades Principais</h2>

O projeto foca em simplicidade e feedback instantâneo para o usuário:

| Funcionalidade | Impacto |
| :--- | :--- |
| 📉 **Retenção por Fornecedor** | Identificação de quais fornecedores têm maior índice de paletes não devolvidos. |
| 💬 **Rastreabilidade de NF** | Vinculação direta da NF de devolução parcial com a NF de entrada original. |
| 🔗 **Impacto Financeiro - CHEP** | Visibilidade do volume de paletes alugados que estão retidos no pátio, evitando multas. |
| ⚠️ **Acuracidade de Estoque** | Sistema de verificação do Estoque Físico com o Estoque no Sistema , visando maior acuracidade. |
| 📱 **Design Adaptável** | Interface limpa que permite a verificação em diferentes telas. |

---

<h2 id="destaques-tecnicos">5. 💻 Destaques Técnicos</h2>

O projeto foi construído com foco em **Reprodutibilidade** e **Clareza Analítica**:

<h3>🧹 Pipeline de Limpeza Robusto:</h3>

Tratamento sistemático de campos nulos, duplicados e padronização de tipos antes de qualquer análise, garantindo que os Dados sejam  confiáveis.

<h3>🔒 Segurança e Privacidade - Nota ao CPD/TI:</h3>

Este repositório é público e foi criado estritamente para fins de estudo e demonstração de Prova de Conceito.
Nenhum dado real do Atacadão está armazenado neste repositório.
O arquivo data/raw/dados_palete.csv contém dados fictícios para simulação.
O arquivo .gitignore está configurado para bloquear qualquer upload de dados sensíveis extraídos do sistema.

---

<h2 id="estrutura-do-projeto">6. 📂 Estrutura do Projeto</h2>

```text
Atacadao-Dashboard-Palete-Python
├── data/
│   └── raw/                📌 Datasets originais - CSV.
├── notebooks/
│   └── inicial.ipynb       📌 Notebook principal de análise.
├── assets/
│   └── png/                📌 Gráficos e telas exportadas.
├── src/                    📌 Scripts utilitários.
├── requirements.txt        📌 Dependências Python.
└── README.md               📌 Documentação Técnica.
```

---

<h2 id="como-contribuir">7. 🤝 Como Contribuir</h2>

Deseja melhorar o design ou adicionar novas métricas? Siga o fluxo oficial:

| Fase | Ação | Link / Comando |
| :---: | :--- | :--- |
| **01** | **Fork** | [![Fork](https://img.shields.io/badge/-Fazer%20Fork-blue?style=flat-square&logo=github)](https://github.com/Domisnnet/Atacadao-Dashboard-Palete-Python/fork) |
| **02** | **Branch** | `git checkout -b feature/NovoGrafico` |
| **03** | **Commit** | `git commit -m 'feat: add gráfico de estrelas'` |
| **04** | **Push** | `git push origin feature/NovoGrafico` |
| **05** | **PR** | [![Abrir PR](https://img.shields.io/badge/-Abrir%20PR-green?style=flat-square&logo=git)](https://github.com/Domisnnet/Atacadao-Dashboard-Palete-Python/compare)

<h3>🐛 Encontrou um problema?</h3>

Se algo não estiver funcionando como esperado, não hesite em abrir um chamado:

[![Issues Abertas](https://img.shields.io/github/issues/Domisnnet/Atacadao-Dashboard-Palete-Python?style=flat-square&color=red&logo=github)](https://github.com/Domisnnet/Customer-Retention-Insights-Python/issues)
[![Report Bug](https://img.shields.io/badge/Reportar-Erro-critical?style=flat-square&logo=github)](https://github.com/Domisnnet/Atacadao-Dashboard-Palete-Python/issues/new)

---

<h2 id="faq">8. 🧠 Perguntas Frequentes</h2>

<details>
<summary><strong>Os dados são reais ou fictícios ❓</strong></summary>
<p>
  📊 <strong>Resposta:</strong> Os dados utilizados são amostras representativas <code>dados_palete.csv</code> para fins de demonstração e estudo de técnicas de BI.
</p>
</details>

<details>
<summary><strong>Onde estão os dados reais do Atacadão ❓</strong></summary>
<p>
  ✅ <strong>Resposta:</strong>Por questões de segurança da informação, os dados reais extraídos do Cerberus rodam apenas em ambiente local ou interno da empresa, nunca sendo enviados para a nuvem deste repositório público
</p>
</details>

<details>
<summary><strong>Como adicionar novos gráficos ❓</strong></summary>
<p>
  🎨 <strong>Resposta:</strong>Crie um novo bloco no arquivo <code>app/main.py</code>, importe o Plotly e utilize o <code>st.plotly_chart()</code> para renderizar o novo gráfico no Streamlit.
</p>
</details>

---

<h2 id="codigo-fonte">9. 💻 Código Fonte</h2>

Deseja analisar a lógica de processamento? Explore o Repositório Oficial:

[![Repositório](https://img.shields.io/badge/Repositório-Domisnnet%2FAtacadao--Dashboard--Palete--Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Domisnnet/Atacadao-Dashboard-Palete-Python)

---

<h2 id="créditos">10. 📝 Créditos & Reconhecimentos</h2>

O **BI-Python** é resultado de estudo contínuo em Data Science:

| Atribuição | Responsável / Recurso | Descrição |
| :--- | :--- | :--- |
| **Análise de Dados** | **DomisDev** | Exploração, limpeza e visualização dos datasets. |
| **Empresa:** | | **Atacadão - CD**  | Contexto de negócio e origem dos dados. |
| **Engine Gráfica** | **Plotly & Streamlit** | Base para renderização estatística precisa. |
| **Manipulação** | **Pandas** | Processamento eficiente de tabelas e séries temporais. |
| **Apoio Técnico** | **Google Gemini** | Padronização e refinamento documental. |

---

<h2 id="licenca">11. 📄 Licença</h2>

Este projeto está licenciado sob a &nbsp;[![Licença MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Domisnnet/Atacadão-Dashboard-Palete-Python/blob/main/LICENSE)

---

<h2 id="perfil-do-github">12. 👨‍💻 Perfil do GitHub</h2>

<a href="https://github.com/Domisnnet"> 
  <img src=
    "assets/images/DomisDev.png" width="90" style="border-radius: 50%" alt="Acessar perfil GitHub"
  > 
</a>

&nbsp;
<p align="center">
  <a href="#sobre-o-projeto">
    <img src=
      "https://img.shields.io/badge/⬆️%20VOLTAR%20AO%20TOPO-26FF00?style=flat&labelColor=111827&color=0A0F1C" alt="Voltar ao topo" style="height: 30px;"
    >
  </a>
</p>
