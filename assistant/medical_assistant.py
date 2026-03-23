import json
import logging
from datetime import datetime
from pipelines.langchain_pipeline import LangChainPipeline
from pipelines.decision_flow import DecisionFlow
from security.guardrails import validate_response

class MedicalAssistant:

    def __init__(self, data_path="data/protocols.json"):
        self.protocols = self.load_protocols(data_path)
        self.pipeline = LangChainPipeline()
        self.decision_flow = DecisionFlow()

        logging.basicConfig(
            filename="logs/assistant.log",
            level=logging.INFO
        )

    def load_protocols(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def retrieve_context(self, question):
        q = question.lower()

        best_match = None

        for protocol in self.protocols:
            if protocol["topic"] in q:
                return protocol["content"]

            # 🔥 matching por palavras-chave
            if protocol["topic"] == "diabetes" and any(word in q for word in ["glicose", "diabetes"]):
                best_match = protocol["content"]

            if protocol["topic"] == "hipertensao" and "pressão" in q:
                best_match = protocol["content"]

        return best_match or "Nenhum protocolo específico encontrado."

    def generate_response(self, question, context, patient_data):
        full_context = f"""
    Dados do paciente:
    - Idade: {patient_data['age']}
    - Glicose: {patient_data['glucose']}
    - BMI: {patient_data['bmi']}

    Protocolo:
    {context}
    """

        return self.pipeline.run(full_context, question)

    def log_interaction(self, question, response):
        logging.info(f"{datetime.now()} | Q: {question}")
        logging.info(f"{datetime.now()} | A: {response}")

    def run(self, question, patient_data):
        context = self.retrieve_context(question)
        
        full_context = f"""
        Dados do paciente:
        - Idade: {patient_data['age']}
        - Glicose: {patient_data['glucose']}
        - BMI: {patient_data['bmi']}

        Protocolo:
        {context}
        """

        raw_response = self.decision_flow.run(
            question,
            full_context,
            self.pipeline
        )

        response = validate_response(raw_response)

        self.log_interaction(question, response)

        return {
            "answer": response,
            "source": "Protocolo interno"
        }