class DecisionFlow:

    def classify_intent(self, question: str) -> str:
        q = question.lower()

        if "exame" in q:
            return "exam_analysis"

        if "tratamento" in q or "tratar" in q:
            return "treatment_guidance"

        if "diagnóstico" in q or "avaliar" in q:
            return "diagnosis_support"

        return "general"

    def run(self, question, context, pipeline):
        intent = self.classify_intent(question)

        if intent == "exam_analysis":
            return pipeline.run(
                context + "\nFoque na análise de exames.",
                question
            )

        elif intent == "treatment_guidance":
            return pipeline.run(
                context + "\nForneça orientação geral, sem prescrição.",
                question
            )

        elif intent == "diagnosis_support":
            return pipeline.run(
                context + "\nAjude na análise clínica do caso.",
                question
            )

        return pipeline.run(context, question)