# OpenAI Python SDK Context Creator

The purpose of this repository is to describe a simple utility for copying the README page for the Open AI Python SDK then prompting a large language model to reformat it for readability as a piece of contextual data.

The purpose of this workflow is to overcome the problem whereby the Open AI models themselves do not have updated data about the correct syntax for the Python SDK. Commonly, and even when prompting OpenAI's latest flagship models, the code snippets produced use deprecated functions from previous versions of the SDK. 

This problem may be resolved in time. But for the moment this is one workaround that can be used. 

After generating the updated context file, the output format can be tweaked in the prompt. This can be provided to something like an assistant to make sure that it's grounded in the correct syntax for the SDK.

## Utility Flow

- Python script in scripts pulls in the latest version of the README and copies it to the repository. 
- The prompt in the prompts folder instructs a large language model to convert the README into a piece of context data by providing specific formatting instructions. This is where the output format can be tweaked. For example, you may wish to instruct that it be outputted into JSON
- Finally, the formatted context data is collected within the repository. From here it can be piped into a vector store in a pipeline. Or more simply uploaded to a vector store as context data using a drag and drop mechanism. 

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).


