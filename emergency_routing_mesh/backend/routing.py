import os
from groq import Groq
from dotenv import load_dotenv

# Securely extract the API key from the local hidden setup file
load_dotenv()
api_key_value = os.getenv("GROQ_API_KEY")

# Initialize connection instance targeting GroqCloud infrastructure
client = Groq(api_key=api_key_value)

def calculate_emergency_mesh_blueprint(accident_statement):
    """Sends traffic reports to a live model engine to generate tactical rerouting data."""
    
    prompt = (
        f"You are an AI Emergency Traffic Router. Analyze this traffic accident statement "
        f"and provide a clear, tactical emergency routing blueprint: {accident_statement}"
    )
    
    # Updated to the active production model running on GroqCloud
    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b", 
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=800
    )
    
    return response.choices[0].message.content