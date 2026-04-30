import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_functions import available_functions, call_function
from prompts import system_prompt 

def main():
    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    prompt = args.user_prompt
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    verbose_flag = args.verbose
    if verbose_flag:
        print(f"User prompt: {prompt}\n")
    
    for _ in range(20):
        response = generate_response(client, messages, verbose_flag)
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
            messages.append(types.Content(role="user", parts=response))

        
                

def generate_response(client, messages, verbose_flag):
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

    if verbose_flag:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return 

    results = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call)
        if (
            function_call_result.parts == []
            or not function_call_result.parts[0].function_response
            or not function_call_result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
        
        if verbose_flag:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        results.append(function_call_result.parts[0])
    return response

if __name__=="__main__":
    main()