
# Evaluar Experiencia

Este proyecto implementa un sistema basado en LLM (Modelo de Lenguaje Grande) para evaluar la experiencia de un candidato en relación con una oferta de trabajo. Utiliza la API de OpenAI para generar una evaluación estructurada en formato JSON.

## Descripción

El sistema recibe dos entradas principales:
- **Oferta de Trabajo**: Una descripción breve del puesto.
- **CV del Candidato**: Información detallada sobre la experiencia laboral, formación y habilidades.

El sistema devuelve una evaluación detallada en formato JSON que incluye:
1. **Puntuación de relevancia** (0 a 100).
2. **Lista de experiencias relevantes** con detalles del puesto, empresa y duración.
3. **Justificación de la puntuación otorgada**.

## Requisitos

Antes de instalar el proyecto, asegúrate de tener instalado Python 3.7 o superior.

### Dependencias

Las dependencias necesarias se encuentran en el archivo `requirements.txt`. Incluyen:
- `openai`
- `tiktoken`

### Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. Para instalar el proyecto como paquete:
   ```bash
   pip install .
   ```

## Uso

Para ejecutar el sistema, simplemente ejecuta el siguiente comando después de la instalación:

```bash
evaluar_experiencia
```

Se te pedirá que ingreses la **oferta de trabajo** y el **CV del candidato**. El sistema generará la evaluación y la mostrará en formato JSON.

### Ejemplo de uso:


Aquí tienes un ejemplo de cv: 
cv = """
Candidato: Imad Saidi
Último Puesto: Comercial de automóviles
Última formación reglada: FP 1 / Técnico medio
Datos de contacto:
- Email: imadsaidiyassine57@gmail.com
- Teléfono: 634151693
- Localidad: 20200 Beasain (Guipúzcoa), España
- Fecha de nacimiento: 13 octubre 2002
- DNI: 48841750P
- Sexo: Hombre

Experiencia:
1. Comercial de automóviles - Autónomo (Enero 2024 / Febrero 2024)
   Venta de vehículos nuevos o usados a particulares y empresas, tasaciones.
   
2. Vendedor/a de puesto de mercado - Mercadona (Octubre 2023 / Marzo 2024)
   Atención al cliente, limpieza, arqueo de la caja, colocación de prsoductos, control de caducidades.

3. Auxiliar de mantenimiento industrial - Agrisolutions (Enero 2020 / Enero 2024)
   Mantenimientos preventivos de baja complejidad, colaboración en limpieza y orden.

4. Camarero/a de barra - Gastroteka Ordizia 1990 (Marzo 2023 / Septiembre 2023)
   Atención al cliente, cobros, pedidos telefónicos y reservas.

5. Limpieza industrial - Zereguin Zerbitzuak (Diciembre 2020 / Mayo 2023)
   Limpieza de superficies horizontales y verticales, limpieza de maquinaria.

6. Personal de mantenimiento - Bellota Herramientas (Mayo 2020 / Noviembre 2020)
   Mantenimiento básico de maquinaria, traslado y orden de zona de trabajo.

Formación:
- Bachillerato (Finalizado en Marzo 2024)
- FP 1 / Técnico medio (Finalizado en Junio 2019)

Idiomas:
- Español: Avanzado (C1), Experto (C2)
- Euskera: Avanzado (C1), Experto (C2)
- Francés: Medio (B1), Avanzado (C1)
- Inglés: Básico (A1), Elemental (A2)
- Árabe: Avanzado (C1), Experto (C2)

Conocimientos técnicos:
- Gestión de datos
- Microsoft Word
- Resolución de problemas
- Atención al cliente


"""
```bash
Introduce la oferta de trabajo: Cajero supermercado Dia
Introduce el CV del candidato: [pega aquí el CV en formato texto]
```

Salida esperada:
```json
{
    "score": 85,
    "relevant_experience": [
        {"puesto": "Vendedor/a de puesto de mercado", "empresa": "Mercadona", "duracion": "Octubre 2023 / Marzo 2024"}
    ],
    "justification": "El candidato tiene experiencia relevante en atención al cliente y manejo de caja."
}
```

## Estructura del Proyecto

```
evaluar_experiencia/
├── evaluar_experiencia/
│   ├── __init__.py
│   ├── main.py
├── setup.py
├── README.md
├── requirements.txt
```

## Problemas Conocidos

- **Límite de tokens**: 
    - Si la suma del prompt y la respuesta supera los límites del modelo (4096 tokens para GPT-3.5-turbo), el sistema lanzará un error.