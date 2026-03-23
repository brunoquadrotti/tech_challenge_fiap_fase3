from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Este pipeline simula o uso de uma LLM fine-tunada com dados médicos internos,
# utilizando um dataset sintético baseado em protocolos clínicos.

USE_REAL_LLM = False  # controle total

class LangChainPipeline:

    def __init__(self):
        # Este pipeline representa uma LLM adaptada ao domínio médico
        if USE_REAL_LLM:
            self.llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0.2
            )
        else:
            self.llm = None

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
Você é um assistente médico.

Use apenas as informações abaixo:
{context}

Pergunta:
{question}

Regras:
- NÃO prescrever medicamentos
- NÃO sugerir doses
- Sempre recomendar validação médica

Resposta:
"""
        )

    def run(self, context, question):
        final_prompt = self.prompt.format(
            context=context,
            question=question
        )

        if USE_REAL_LLM:
            response = self.llm.invoke(final_prompt)
            return response.content

        # 🔥 fallback mock (obrigatório)
        return f"""
[Resposta simulada]

Baseado no contexto:
{context}

Pergunta:
{question}

O paciente deve ser avaliado clinicamente.
⚠️ Procure um profissional de saúde.
"""