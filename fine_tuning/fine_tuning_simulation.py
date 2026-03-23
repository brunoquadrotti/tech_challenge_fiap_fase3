import json


class FineTuningSimulator:

    def __init__(self, data_path="fine_tuning/training_data.json"):
        self.data = self.load_data(data_path)

    def load_data(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def preprocess_data(self):
        processed = []

        for item in self.data:
            processed.append({
                "prompt": item["instruction"],
                "response": item["output"]
            })

        return processed

    def simulate_training(self):
        processed_data = self.preprocess_data()

        print("=== SIMULAÇÃO DE FINE-TUNING ===")
        print(f"Total de exemplos: {len(processed_data)}")

        for i, example in enumerate(processed_data[:2]):
            print(f"\nExemplo {i+1}:")
            print("Prompt:", example["prompt"])
            print("Resposta:", example["response"])

        print("\n✔ Fine-tuning simulado com sucesso!")

        return {
            "status": "success",
            "samples": len(processed_data)
        }


if __name__ == "__main__":
    simulator = FineTuningSimulator()
    simulator.simulate_training()