import openai
import tiktoken

def contar_tokens(prompt, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(prompt)
    return len(tokens)

def evaluar_experiencia(oferta, cv):
    prompt = f"""
    Eres un sistema de evaluación de experiencia para un puesto laboral. Evalúa el siguiente CV basado en la oferta proporcionada.
    
    Oferta: {oferta}
    CV: {cv}

    Devuelve un JSON estructurado con:
    1. Una puntuación de 0 a 100 de relevancia de la experiencia.
    2. Un listado de experiencias relevantes con detalles de puesto, empresa y duración.
    3. Una explicación de la puntuación otorgada.

    Responde en el siguiente formato JSON:
    {{
        "score": int,
        "relevant_experience": [
            {{"puesto": str, "empresa": str, "duracion": str}},
            ...
        ],
        "justification": str
    }}
    """

    tokens_usados = contar_tokens(prompt, model="gpt-3.5-turbo")
    print(f"Tokens usados en el prompt: {tokens_usados}")

    if tokens_usados > 4096:
        raise ValueError("El número de tokens supera el límite permitido para el modelo gpt-3.5-turbo")

    max_respuesta_tokens = 4096 - tokens_usados

    client = openai.OpenAI(api_key="TU_API_KEY")
    
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo",
        max_tokens=max_respuesta_tokens
    )

    return completion.choices[0].message.content

def main():
    # Este es el punto de entrada del programa.
    oferta = input("Introduce la oferta de trabajo: ")
    cv = input("Introduce el CV del candidato: ")
    resultado = evaluar_experiencia(oferta, cv)
    print("Resultado de la evaluación:")
    print(resultado)

# Asegúrate de que solo se ejecute si se llama directamente
if __name__ == "__main__":
    main()




