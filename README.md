# 📊 Análise de Horário de Pico - Sistema de Estações CCR

## Descrição do Projeto

Este projeto é um sistema em **Python** para simular e analisar o fluxo de passageiros nas linhas de trem e metrô da **CCR (Linhas 4 Amarela, 8 Diamante e 9 Esmeralda)**.  
O sistema permite **login/cadastro de usuários**, **registro de viagens**, **previsão de pico de passageiros nas estações**, e **relatórios detalhados** das viagens realizadas.

A aplicação visa auxiliar os usuários a visualizarem o movimento das estações e planejarem melhor suas viagens, além de oferecer alertas de lotação.

---

## 🚆 Funcionalidades

- ✅ **Cadastro e Login de Usuário** (integrado com banco de dados Oracle).
- ✅ **Simulação de Viagem** entre estações com registro de horários.
- ✅ **Previsão de Pico** de passageiros em tempo real.
- ✅ **Geração de Relatório** com detalhes de cada viagem.
- ✅ **Alerta de Lotação** quando o número de passageiros atinge um limite.
- ✅ **Dados Armazenados diretamente em um banco de dados Oracle**, permitindo registro e leitura futura das viagens.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- Módulos Padrão:
  - `json` (armazenamento de dados)
  - `datetime` (registro de horário de viagem)
  - `random` (geração automática de fluxo de passageiros)
  - `Oracledb` (armazenamento de dados)
  - `Flask` (Criação de API)

## 🗂 Estrutura do Projeto

📁 Python/
├── app.py # Script principal do sistema<br>
├── conecction_oracle.py # Simulação de conexão com Oracle (não funcional)<br>
├── fluxo_passageiros.csv # Dados simulados de fluxo de passageiros<br>
├── usuarios.json # Base simulada de usuários cadastrados<br>
├── viagens.json # Histórico de viagens registradas<br>

---

## ▶️ Como Executar

1. **Clone o repositório:**

git clone https://github.com/ChallengeCCR1/Python.git<br>
cd Python<br>
python app.py

--- 

## 👥 Equipe

Este projeto foi desenvolvido por:

- **Pedro Henrique Sena**  
  Desenvolvedor Full Stack e Documentação  
  [LinkedIn](https://www.linkedin.com/in/pedro-henrique-sena/) | [GitHub](https://github.com/devpedrosena1)

- **Matteus Viegas**  
  Desenvolvedor Front End  
  [LinkedIn](https://www.linkedin.com/in/matteus-viegas-533437294/) | [GitHub](https://github.com/ChallengeOne-MAT)

- **Sulamita Viegas**  
  Gestora de Negócios  
  [LinkedIn](https://www.linkedin.com/in/sulamita-viegas-dos-santos-280210223/) | [GitHub](https://github.com/Sulamita020905)

---
## 📄 Licença<br>
©Todos os direitos reservados
