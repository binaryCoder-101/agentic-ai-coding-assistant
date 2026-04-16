import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt 
from functions.call_functions import available_functions

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="ChatBot")

    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    prompt = args.user_prompt
    # verbose_flag = args.verbose

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if not response.usage_metadata:
        raise RuntimeError("Failed API request")

    # if verbose_flag:
    #     print(f"User prompt: {prompt}")
    #     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #     print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    #     print("Response:")
    #     print(response.text)
    # else:
    #     print("Response:")
    #     print(response.text)
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")


if __name__=="__main__":
    main()