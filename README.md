# Assistente Médico com LLM e LangChain

**Tech Challenge – Fase 3 (IADT – FIAP)**  

Autor: **Bruno Quadrotti de Freitas**

---

## Objetivo

Desenvolver um assistente médico inteligente capaz de analisar perguntas clínicas, utilizar dados do paciente e protocolos médicos internos para gerar respostas seguras, contextualizadas e rastreáveis, utilizando LLMs e LangChain.

---

## Escopo da Fase 3

Nesta fase, o projeto evolui para a construção de um sistema completo de apoio à decisão médica, incluindo:

- simulação de fine-tuning de LLM com dados médicos;
- construção de pipeline com LangChain;
- aplicação de fluxo de decisão (estilo LangGraph);
- implementação de mecanismos de segurança e validação;
- organização modular do projeto.

---

## Arquitetura do Sistema

O sistema segue o fluxo:

Entrada (pergunta + dados do paciente)  
→ Recuperação de protocolo  
→ Enriquecimento de contexto  
→ Decisão de fluxo  
→ Pipeline com LLM  
→ Validação de segurança  
→ Logging  
→ Resposta final

---

## Estrutura do Projeto

```
fase3/
├── assistant/
│   └── medical_assistant.py
├── data/
│   └── protocols.json
├── fine_tuning/
│   ├── fine_tuning_simulation.py
│   └── training_data.json
├── pipelines/
│   ├── decision_flow.py
│   └── langchain_pipeline.py
├── security/
│   └── guardrails.py
├── logs/
│   └── assistant.log
├── main.py
├── demo.ipynb
├── requirements.txt
└── README.md
```

---

## Funcionalidades

### 1. Recuperação de contexto
Busca protocolos médicos com base na pergunta do usuário.

### 2. Contextualização do paciente
Inclui dados clínicos (idade, glicose, BMI) na análise.

### 3. Fluxo de decisão
Classifica a intenção da pergunta e adapta o comportamento do sistema.

### 4. Pipeline com LangChain
Utiliza PromptTemplate e simula interação com LLM.

### 5. Fine-tuning (simulado)
Dataset sintético com exemplos clínicos para representar ajuste do modelo.

### 6. Segurança (guardrails)
Evita respostas com prescrição médica direta.

### 7. Logging
Registra todas as interações para auditoria.

---

## Execução

### Executar o sistema

```bash
python main.py
```

---

## Exemplo de uso

Entrada:

```
Paciente com glicose alta, como avaliar?
```

Saída:

- análise baseada em protocolo
- contexto do paciente incluído
- recomendação segura

---

## Fine-tuning (Simulado)

Foi criado um dataset sintético contendo perguntas e respostas médicas.

O processo inclui:
- estruturação dos dados
- pré-processamento
- simulação do treinamento

---

## Segurança e Validação

O sistema possui mecanismos para:

- bloquear recomendações médicas diretas;
- evitar prescrição de medicamentos;
- garantir uso responsável da IA.

---

## Conclusão

O projeto demonstra a construção de um assistente médico com arquitetura moderna baseada em LLMs, integrando contexto clínico, fluxo de decisão e mecanismos de segurança.

O sistema possui caráter educacional e simula um ambiente real de apoio à decisão médica.

---

## Autor

**Bruno Quadrotti de Freitas**  
[LinkedIn](https://www.linkedin.com/in/brunoquadrotti/) | [GitHub](https://github.com/brunoquadrotti/)
