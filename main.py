import sys
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    arguments = sys.argv
    flag = ""

    if arguments[-1] == "--verbose":
        flag += "--verbose"
        prompt = "".join(arguments[1:-1])
    else:
        prompt = "".join(arguments[1:])
    
    if len(prompt) < 1:
        print("usage: uv run main.py <prompt>")
        print("usage: uv run main.py <prompt> --verbose")
        sys.exit(1)
    else:
        messages = [
            types.Content(role="user", parts=[types.Part(text=prompt)]),
        ]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
        )
        if not flag:
            print("Response:") 
            print(response.text)
        elif flag == "--verbose":
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print("Response:") 
            print(response.text)
        


if __name__ == "__main__":
    main()


    