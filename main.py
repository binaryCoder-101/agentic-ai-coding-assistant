import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("usage: uv run main.py <prompt>")
        sys.exit(1)
    else:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents="".join(sys.argv[1:]),
        )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:") 
    print(response.text)


if __name__ == "__main__":
    main()


    