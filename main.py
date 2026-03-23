from assistant.medical_assistant import MedicalAssistant

assistant = MedicalAssistant()

question = "Paciente com glicose alta, como avaliar?"

patient_data = {
    "age": 52,
    "glucose": 180,
    "bmi": 32
}

response = assistant.run(question, patient_data)

print("\n=== RESPOSTA ===")
print(response["answer"])

print("\nFonte:", response["source"])