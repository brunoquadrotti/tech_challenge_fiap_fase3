def validate_response(response: str):
    forbidden = ["remédio", "dosagem", "mg"]

    for word in forbidden:
        if word in response.lower():
            return "Resposta bloqueada por segurança."

    return response