import os
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
def load_env_vars():
    # Hardcoded path to the .env file
    dotenv_path = "/home/daniel/Git/openai-pythonsdk-helper/.env"
    if not os.path.exists(dotenv_path):
        raise FileNotFoundError(f".env file not found at {dotenv_path}")
    load_dotenv(dotenv_path)

# Function to parse and reformat the Markdown file
def parse_and_reformat_markdown():
    # Hardcoded paths for input and output files
    input_path = "/home/daniel/Git/openai-pythonsdk-helper/source/README.md"
    output_path = "/home/daniel/Git/openai-pythonsdk-helper/context/context-file.md"

    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"README file not found at {input_path}")

    # Read content from input file
    with open(input_path, 'r') as file:
        content = file.read()

    # Use GPT-3.5 to reformat content
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(
            "Reformat the following Markdown content to describe the functionality "
            "of all functions documented in it. Remove any extraneous material, and "
            "write it as context data for a large language model:\n\n"
            f"{content}"
        ),
        max_tokens=1500,
        temperature=0.7
    )

    # Extract reformatted content from GPT response
    reformatted_content = response.choices[0].text.strip()

    # Write reformatted content to output file
    with open(output_path, 'w') as file:
        file.write(reformatted_content)

# Main execution logic
if __name__ == "__main__":
    try:
        # Load environment variables (API key)
        load_env_vars()

        # Set OpenAI API key from environment variables
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        # Parse and reformat Markdown file
        parse_and_reformat_markdown()
        print("Markdown parsing and reformatting completed successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
