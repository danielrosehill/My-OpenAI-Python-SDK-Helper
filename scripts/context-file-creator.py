import os
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file at the root of the repository
# Resolve the absolute path to the .env file
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
dotenv_path = os.path.join(root_dir, ".env")
load_dotenv(dotenv_path)

# Get the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Set up OpenAI API key
openai.api_key = openai_api_key

# Function to parse and reformat the Markdown file
def parse_and_reformat_markdown(input_path, output_path):
    # Read the content of the input Markdown file
    with open(input_path, 'r') as file:
        content = file.read()

    # Use GPT-3.5 to reformat the content
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

    # Extract the reformatted content from GPT's response
    reformatted_content = response.choices[0].text.strip()

    # Write the reformatted content to the output Markdown file
    with open(output_path, 'w') as file:
        file.write(reformatted_content)

# Define paths for input and output files relative to script location
input_path = os.path.abspath(os.path.join(root_dir, "source/README.md"))
output_path = os.path.abspath(os.path.join(root_dir, "context/context-file.md"))

# Call the function to perform parsing and reformatting
parse_and_reformat_markdown(input_path, output_path)
