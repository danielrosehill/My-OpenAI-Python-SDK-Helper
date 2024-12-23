# OpenAI Python SDK Context - October 26, 2023

This document provides context for generating Python scripts using the OpenAI SDK.

## Core Concepts

### Authentication

The SDK requires an API key for authentication. This can be provided via the `openai.api_key` attribute or the `OPENAI_API_KEY` environment variable.

### Asynchronous Operations

The SDK offers asynchronous versions of most functions (e.g., `chat.completions.create` and `chat.completions.acreate`). These should be used within an async context.

## Functionality

### Chat Completions

-   `chat.completions.create(**kwargs)`: Creates a new chat completion.
    -   Parameters include:
        -   `model` (str): The model to use (e.g., "gpt-4", "gpt-3.5-turbo").
        -   `messages` (list): A list of message dictionaries with `role` ("system", "user", "assistant") and `content` keys.
        -   `temperature` (float, optional): Sampling temperature (0 to 2).
        -   `top_p` (float, optional):  Nucleus sampling probability (0 to 1).
        -   `n` (int, optional):  Number of completions to generate.
        -   `stream` (bool, optional): If True, stream partial results.
        -  `stop` (str or list, optional): Stop sequences.
        -   `max_tokens` (int, optional): Maximum number of tokens to generate.
        -  `presence_penalty` (float, optional): Presence penalty (-2.0 to 2.0)
        -  `frequency_penalty` (float, optional): Frequency penalty (-2.0 to 2.0).
        -   `logit_bias` (dict, optional): Token logit bias.
        -   `user` (str, optional):  User identifier.
        -   `tools` (list, optional):  Tools the model can use.
        -   `tool_choice` (str, optional): Tool choice parameters.
-   `chat.completions.acreate(**kwargs)`: Asynchronous version of `chat.completions.create`.
- `chat.completions.with_raw_response.create(**kwargs)`:  Returns a raw HTTP response from the API, in addition to the python object
-  `chat.completions.with_raw_response.acreate(**kwargs)`: Asynchronous version of `chat.completions.with_raw_response.create`.

### Models

-   `models.list()`: Lists available models.
-   `models.retrieve(model_id)`: Retrieves information about a specific model.
- `models.with_raw_response.list()`: Returns raw HTTP response with the list of models
- `models.with_raw_response.retrieve(model_id)`: Returns raw HTTP response with model information.
- `models.acreate()`: Asynchronous version of model create.
- `models.aretreive()`: Asynchronous version of model retrieve.
- `models.awith_raw_response.list()`: Asynchronous version of raw list.
-  `models.awith_raw_response.retrieve()`: Asynchronous version of raw retrieve.

### Edits

-  `edits.create(**kwargs)`: Creates a new edit.
    -   Parameters include:
        - `model` (str): The model to use (e.g., "text-davinci-edit-001").
        - `input` (str, optional): The input text to edit.
        - `instruction` (str):  The instruction for the edit.
        - `n` (int, optional): Number of edits to generate.
        - `temperature` (float, optional): Sampling temperature (0 to 2).
        - `top_p` (float, optional): Nucleus sampling probability (0 to 1).
- `edits.acreate(**kwargs)`: Asynchronous version of `edits.create`
- `edits.with_raw_response.create(**kwargs)`: Returns a raw HTTP response from the API
- `edits.with_raw_response.acreate(**kwargs)`: Asynchronous version of the raw response.

### Images

-   `images.generate(**kwargs)`: Generates an image.
    -   Parameters include:
        -   `prompt` (str): The image generation prompt.
        -   `n` (int, optional): Number of images to generate.
        -   `size` (str, optional): Image size (e.g., "256x256", "512x512", "1024x1024").
        -   `response_format` (str, optional): Response format, "url" or "b64_json".
        - `user` (str, optional):  User identifier.
- `images.with_raw_response.generate(**kwargs)`: Returns raw HTTP response for image generation
-   `images.acreate(**kwargs)`: Asynchronous version of `images.generate`.
- `images.with_raw_response.agenerate(**kwargs)`: Asynchronous version of the raw response image generation.
-  `images.create_variation(**kwargs)`: Creates a variation of a provided image
    -  Parameters include:
        - `image`: A file object or a path.
        - `n` (int, optional): Number of images to generate.
        -   `size` (str, optional): Image size (e.g., "256x256", "512x512", "1024x1024").
         -   `response_format` (str, optional): Response format, "url" or "b64_json".
         - `user` (str, optional):  User identifier.
-`images.with_raw_response.create_variation(**kwargs)`: Creates a variation of a provided image with a raw response.
-  `images.acreate_variation(**kwargs)`: Asynchronous version of `images.create_variation`.
-`images.with_raw_response.acreate_variation(**kwargs)`: Asynchronous version of the raw response `images.create_variation`
-   `images.edit(**kwargs)`: Creates an edited or in-painted image.
     -  Parameters include:
        - `image`: A file object or a path.
         - `mask` (optional): A mask image object or path.
        - `prompt` (str): The image generation prompt.
        -   `n` (int, optional): Number of images to generate.
        -   `size` (str, optional): Image size (e.g., "256x256", "512x512", "1024x1024").
         -   `response_format` (str, optional): Response format, "url" or "b64_json".
         - `user` (str, optional):  User identifier.
- `images.with_raw_response.edit(**kwargs)`: Returns a raw HTTP response when creating an edited image.
-  `images.aedit(**kwargs)`: Asynchronous version of `images.edit`
-  `images.with_raw_response.aedit(**kwargs)`: Asynchronous version of the raw response when editing an image.

### Embeddings

-   `embeddings.create(**kwargs)`: Creates an embedding for input text.
    -   Parameters include:
        -   `model` (str): Embedding model (e.g., "text-embedding-ada-002").
        -   `input` (str or list): Input text or list of texts.
        - `user` (str, optional):  User identifier.
-`embeddings.with_raw_response.create(**kwargs)`: Returns a raw HTTP response when creating an embedding
-   `embeddings.acreate(**kwargs)`: Asynchronous version of `embeddings.create`.
- `embeddings.with_raw_response.acreate(**kwargs)`: Asynchronous version of the raw response when creating an embedding

### Files

-   `files.list()`: Lists uploaded files.
- `files.with_raw_response.list()`: Returns a raw HTTP response when listing files.
-   `files.upload(**kwargs)`: Uploads a file.
    -   Parameters include:
        - `file`: File object or path
        - `purpose` (str): Purpose for the file
- `files.with_raw_response.upload(**kwargs)`: Uploads a file with a raw HTTP response.
-   `files.retrieve(file_id)`: Retrieves a specific file's information.
- `files.with_raw_response.retrieve(file_id)`: Retrieves file info with a raw response
-   `files.delete(file_id)`: Deletes a file.
- `files.with_raw_response.delete(file_id)`: Delete a file with a raw HTTP response
-   `files.retrieve_content(file_id)`: Retrieves a files content
-  `files.with_raw_response.retrieve_content(file_id)`: Retrieves a files content with a raw HTTP response.
-   `files.acreate()`: Asynchronous file creation
-   `files.alist()`: Asynchronous listing of files.
- `files.awith_raw_response.list()`: Asynchronous raw response of file list
- `files.aupload()`: Asynchronous file upload
- `files.awith_raw_response.upload()`: Asynchronous raw response of file upload
- `files.aretrieve()`: Asynchronous file retrieval
- `files.awith_raw_response.retrieve()`: Asynchronous raw response of file retrieval
- `files.adelete()`: Asynchronous file deletion
- `files.awith_raw_response.adelete()`: Asynchronous raw response file deletion
-`files.aretrieve_content()`: Asynchronous file content retrieval
-`files.awith_raw_response.aretrieve_content()`: Asynchronous raw response file content retrieval

### Fine-tuning

-   `fine_tuning.jobs.create(**kwargs)`: Creates a fine-tuning job.
    -   Parameters include:
        -   `training_file` (str): ID of training file.
        -   `model` (str, optional): Base model for fine-tuning.
- `fine_tuning.jobs.with_raw_response.create(**kwargs)`: Creates a fine-tuning job with raw response.
-   `fine_tuning.jobs.list()`: Lists fine-tuning jobs.
-`fine_tuning.jobs.with_raw_response.list()`: Lists fine-tuning jobs with raw response.
-   `fine_tuning.jobs.retrieve(job_id)`: Retrieves information about a specific fine-tuning job.
- `fine_tuning.jobs.with_raw_response.retrieve(job_id)`: Retrieves a specific fine-tuning job info with raw response.
-   `fine_tuning.jobs.cancel(job_id)`: Cancels a fine-tuning job.
-`fine_tuning.jobs.with_raw_response.cancel(job_id)`: Cancels a fine-tuning job with a raw response.
-   `fine_tuning.jobs.list_events(job_id)`: Lists events for a fine-tuning job.
- `fine_tuning.jobs.with_raw_response.list_events(job_id)`: Lists events with a raw response for a fine-tuning job.
- `fine_tuning.jobs.acreate()`: Asynchronous creation of fine tuning jobs
- `fine_tuning.jobs.alist()`: Asynchronous listing of fine tuning jobs
- `fine_tuning.jobs.awith_raw_response.list()`: Asynchronous listing of fine tuning jobs with a raw response.
- `fine_tuning.jobs.aretrieve()`: Asynchronous retrieval of fine tuning jobs
- `fine_tuning.jobs.awith_raw_response.retrieve()`: Asynchronous retrieval of fine tuning jobs with a raw response.
- `fine_tuning.jobs.acancel()`: Asynchronous cancellation of a fine tuning job.
-`fine_tuning.jobs.awith_raw_response.cancel()`: Asynchronous cancellation of a fine tuning job with a raw response
-`fine_tuning.jobs.alist_events()`: Asynchronous listing of fine tuning job events
- `fine_tuning.jobs.awith_raw_response.list_events()`: Asynchronous listing of fine tuning job events with a raw response

### Moderations

-   `moderations.create(**kwargs)`: Moderates input text.
    -   Parameters include:
        -   `input` (str or list): Input text or list of texts.
        -   `model` (str, optional): Model to use for moderation
-`moderations.with_raw_response.create(**kwargs)`: Moderates input text with a raw response.
-   `moderations.acreate(**kwargs)`: Asynchronous version of `moderations.create`.
-`moderations.with_raw_response.acreate(**kwargs)`: Asynchronous version of moderations with raw response.

### Audio

-   `audio.transcriptions.create(**kwargs)`: Transcribes audio
    -   Parameters include:
         - `file`: A file object or path.
         - `model`: The transcription model to use
         - `language` (str, optional): The language of the input audio.
         - `prompt` (str, optional): An optional text to guide the model.
         - `response_format` (str, optional): Response format, "json", "text", "srt", "verbose_json", or "vtt".
         - `temperature` (float, optional): The sampling temperature
- `audio.transcriptions.with_raw_response.create(**kwargs)`: Transcribes audio with a raw response
-    `audio.transcriptions.acreate(**kwargs)`: Asynchronous version of `audio.transcriptions.create`.
- `audio.transcriptions.with_raw_response.acreate(**kwargs)`: Asynchronous version of audio transcriptions with a raw response.
-   `audio.translations.create(**kwargs)`: Translates audio.
    -   Parameters include:
         - `file`: A file object or path.
         - `model`: The translation model to use
         - `prompt` (str, optional): An optional text to guide the model.
         - `response_format` (str, optional): Response format, "json", "text", "srt", "verbose_json", or "vtt".
         - `temperature` (float, optional): The sampling temperature
-`audio.translations.with_raw_response.create(**kwargs)`: Translates audio with a raw response.
-   `audio.translations.acreate(**kwargs)`: Asynchronous version of `audio.translations.create`.
-`audio.translations.with_raw_response.acreate(**kwargs)`: Asynchronous version of audio translation with a raw response.
-   `audio.speech.create(**kwargs)`: Generates speech from text.
     -   Parameters include:
         - `model`: The speech model to use.
         - `input`: The text to generate speech from.
          - `voice`: The voice to use
          - `response_format` (str, optional): Response format, "mp3", "opus", "aac", or "flac".
          - `speed` (float, optional): The speed of the generated audio.
-`audio.speech.with_raw_response.create(**kwargs)`: Generates speech from text with a raw response.
-   `audio.speech.acreate(**kwargs)`: Asynchronous version of `audio.speech.create`.
-`audio.speech.with_raw_response.acreate(**kwargs)`: Asynchronous version of speech creation with a raw response.

### Assistants

-   `beta.assistants.create(**kwargs)`: Creates an assistant.
    - Parameters include:
        - `model` (str): The model to use for the assistant
        - `name` (str, optional): The name of the assistant
        - `description` (str, optional): A description of the assistant
        - `instructions` (str, optional): System instructions for the assistant.
        - `tools` (list, optional): List of tools the assistant can use
        - `file_ids` (list, optional): List of file IDs
        - `metadata` (dict, optional): Dictionary of metadata about the assistant
-    `beta.assistants.with_raw_response.create(**kwargs)`: Creates an assistant with a raw response.
- `beta.assistants.retrieve(assistant_id)`: Retrieves an assistant.
- `beta.assistants.with_raw_response.retrieve(assistant_id)`: Retrieves an assistant with a raw response.
- `beta.assistants.modify(assistant_id, **kwargs)`: Modifies an assistant.
     - Parameters include all the same parameters as assistant creation, except for `model`, which cannot be modified.
-`beta.assistants.with_raw_response.modify(assistant_id, **kwargs)`: Modifies an assistant with a raw response.
- `beta.assistants.delete(assistant_id)`: Deletes an assistant.
- `beta.assistants.with_raw_response.delete(assistant_id)`: Deletes an assistant with a raw response.
-  `beta.assistants.list(**kwargs)`: Lists assistants.
    -  Parameters include:
        - `order` (str, optional): Sorts by 'created_at' or 'name', order can be "asc" or "desc"
         - `limit` (int, optional): Limits the number of returned assistants
         - `after` (str, optional): Returns elements after the given cursor
         - `before` (str, optional): Returns elements before the given cursor
-`beta.assistants.with_raw_response.list(**kwargs)`: Lists assistants with raw responses.
- `beta.assistants.acreate()`: Asynchronous creation of assistants.
- `beta.assistants.awith_raw_response.create()`: Asynchronous creation of assistants with a raw response.
-`beta.assistants.aretriev()`: Asynchronous retrieval of assistants.
-`beta.assistants.awith_raw_response.retrieve()`: Asynchronous retrieval of assistants with a raw response.
-`beta.assistants.amodify()`: Asynchronous modification of assistants.
-`beta.assistants.awith_raw_response.modify()`: Asynchronous modification of assistants with a raw response.
-`beta.assistants.adelete()`: Asynchronous deletion of assistants
-`beta.assistants.awith_raw_response.delete()`: Asynchronous deletion of assistants with a raw response
- `beta.assistants.alist()`: Asynchronous list of assistants
-`beta.assistants.awith_raw_response.list()`: Asynchronous list of assistants with a raw response.

### Threads

-  `beta.threads.create(**kwargs)`: Creates a thread.
    - Parameters include:
        -  `messages` (list, optional): A list of message dictionaries.
        - `metadata` (dict, optional): Dictionary of metadata about the thread
-  `beta.threads.with_raw_response.create(**kwargs)`: Creates a thread with a raw response.
- `beta.threads.retrieve(thread_id)`: Retrieves a thread.
- `beta.threads.with_raw_response.retrieve(thread_id)`: Retrieves a thread with a raw response
- `beta.threads.modify(thread_id, **kwargs)`: Modifies a thread.
     - Parameters include:
         - `metadata` (dict, optional): Dictionary of metadata about the thread
- `beta.threads.with_raw_response.modify(thread_id, **kwargs)`: Modifies a thread with a raw response.
- `beta.threads.delete(thread_id)`: Deletes a thread.
-`beta.threads.with_raw_response.delete(thread_id)`: Deletes a thread with a raw response.
- `beta.threads.acreate()`: Asynchronous thread creation.
- `beta.threads.awith_raw_response.create()`: Asynchronous thread creation with a raw response.
-`beta.threads.aretrieve()`: Asynchronous retrieval of a thread.
-`beta.threads.awith_raw_response.retrieve()`: Asynchronous retrieval of a thread with a raw response
-`beta.threads.amodify()`: Asynchronous modification of a thread
-`beta.threads.awith_raw_response.modify()`: Asynchronous modification of a thread with a raw response
-`beta.threads.adelete()`: Asynchronous deletion of a thread.
-`beta.threads.awith_raw_response.delete()`: Asynchronous deletion of a thread with a raw response.

### Messages

-   `beta.threads.messages.create(thread_id, **kwargs)`: Creates a message.
    - Parameters include:
         - `role` (str): The role of the message sender, must be "user"
        - `content` (str): The content of the message
        - `file_ids` (list, optional): List of file IDs
        - `metadata` (dict, optional): Dictionary of metadata about the message
-  `beta.threads.messages.with_raw_response.create(thread_id, **kwargs)`: Creates a message with a raw response.
- `beta.threads.messages.retrieve(thread_id, message_id)`: Retrieves a message.
- `beta.threads.messages.with_raw_response.retrieve(thread_id, message_id)`: Retrieves a message with a raw response.
-`beta.threads.messages.modify(thread_id, message_id, **kwargs)`: Modifies a message.
    - Parameters include:
        - `metadata` (dict, optional): Dictionary of metadata about the message
-`beta.threads.messages.with_raw_response.modify(thread_id, message_id, **kwargs)`: Modifies a message with a raw response.
- `beta.threads.messages.list(thread_id, **kwargs)`: Lists messages within a thread.
    -  Parameters include:
        - `order` (str, optional): Sorts by 'created_at', order can be "asc" or "desc"
         - `limit` (int, optional): Limits the number of returned messages
         - `after` (str, optional): Returns elements after the given cursor
         - `before` (str, optional): Returns elements before the given cursor
-`beta.threads.messages.with_raw_response.list(thread_id, **kwargs)`: Lists messages within a thread with a raw response.
-`beta.threads.messages.acreate()`: Asynchronous creation of messages.
-`beta.threads.messages.awith_raw_response.create()`: Asynchronous creation of messages with a raw response.
-`beta.threads.messages.aretrieve()`: Asynchronous retrieval of a message.
-`beta.threads.messages.awith_raw_response.retrieve()`: Asynchronous retrieval of a message with a raw response.
-`beta.threads.messages.amodify()`: Asynchronous modification of a message.
-`beta.threads.messages.awith_raw_response.modify()`: Asynchronous modification of a message with a raw response.
-`beta.threads.messages.alist()`: Asynchronous listing of messages.
-`beta.threads.messages.awith_raw_response.list()`: Asynchronous listing of messages with a raw response.

### Runs

-  `beta.threads.runs.create(thread_id, **kwargs)`: Creates a run for a thread.
    -  Parameters include:
        - `assistant_id` (str): The ID of the assistant
        - `model` (str, optional): The model to use for the run
        - `instructions` (str, optional): System instructions for the assistant
        - `tools` (list, optional): List of tools the assistant can use
        - `metadata` (dict, optional): Dictionary of metadata about the run.
- `beta.threads.runs.with_raw_response.create(thread_id, **kwargs)`: Creates a run for a thread with a raw response.
- `beta.threads.runs.retrieve(thread_id, run_id)`: Retrieves a run.
- `beta.threads.runs.with_raw_response.retrieve(thread_id, run_id)`: Retrieves a run with a raw response.
- `beta.threads.runs.modify(thread_id, run_id, **kwargs)`: Modifies a run.
     -  Parameters include:
        - `metadata` (dict, optional): Dictionary of metadata about the run.
-  `beta.threads.runs.with_raw_response.modify(thread_id, run_id, **kwargs)`: Modifies a run with a raw response.
-`beta.threads.runs.list(thread_id, **kwargs)`: Lists runs within a thread.
    -  Parameters include:
         - `order` (str, optional): Sorts by 'created_at', order can be "asc" or "desc"
         - `limit` (int, optional): Limits the number of returned runs
         - `after` (str, optional): Returns elements after the given cursor
         - `before` (str, optional): Returns elements before the given cursor
- `beta.threads.runs.with_raw_response.list(thread_id, **kwargs)`: Lists runs within a thread with a raw response
- `beta.threads.runs.create_and_stream(thread_id, **kwargs)`: Creates a run and returns a stream of run steps.
    -  Parameters include:
        - `assistant_id` (str): The ID of the assistant
        - `model` (str, optional): The model to use for the run
        - `instructions` (str, optional): System instructions for the assistant
        - `tools` (list, optional): List of tools the assistant can use
        - `metadata` (dict, optional): Dictionary of metadata about the run.
-`beta.threads.runs.cancel(thread_id, run_id)`: Cancels a run.
-`beta.threads.runs.with_raw_response.cancel(thread_id, run_id)`: Cancels a run with a raw response.
-`beta.threads.runs.submit_tool_outputs(thread_id, run_id, **kwargs)`: Submits tool outputs.
    - Parameters include:
         - `tool_outputs` (list): A list of tool output objects.
-`beta.threads.runs.with_raw_response.submit_tool_outputs(thread_id, run_id, **kwargs)`: Submits tool outputs with a raw response.
- `beta.threads.runs.acreate()`: Asynchronous run creation.
-`beta.threads.runs.awith_raw_response.create()`: Asynchronous run creation with raw response.
-`beta.threads.runs.aretrieve()`: Asynchronous retrieval of a run.
-`beta.threads.runs.awith_raw_response.retrieve()`: Asynchronous retrieval of a run with a raw response.
- `beta.threads.runs.amodify()`: Asynchronous modification of a run.
-`beta.threads.runs.awith_raw_response.modify()`: Asynchronous modification of a run with a raw response.
-`beta.threads.runs.alist()`: Asynchronous listing of runs.
-`beta.threads.runs.awith_raw_response.list()`: Asynchronous listing of runs with a raw response.
-`beta.threads.runs.acreate_and_stream()`: Asynchronous run creation and streaming of run steps.
-`beta.threads.runs.acancel()`: Asynchronous run cancellation
-`beta.threads.runs.awith_raw_response.cancel()`: Asynchronous run cancellation with a raw response.
-`beta.threads.runs.asubmit_tool_outputs()`: Asynchronous tool output submission
-`beta.threads.runs.awith_raw_response.submit_tool_outputs()`: Asynchronous tool output submission with a raw response.

### Run Steps

- `beta.threads.runs.steps.list(thread_id, run_id, **kwargs)`: Lists steps of a run.
     - Parameters include:
         - `order` (str, optional): Sorts by 'created_at', order can be "asc" or "desc"
         - `limit` (int, optional): Limits the number of returned run steps
         - `after` (str, optional): Returns elements after the given cursor
         - `before` (str, optional): Returns elements before the given cursor
-`beta.threads.runs.steps.with_raw_response.list(thread_id, run_id, **kwargs)`: Lists steps of a run with a raw response.
- `beta.threads.runs.steps.retrieve(thread_id, run_id, step_id)`: Retrieves a run step.
-`beta.threads.runs.steps.with_raw_response.retrieve(thread_id, run_id, step_id)`: Retrieves a run step with a raw response.
-`beta.threads.runs.steps.alist()`: Asynchronous listing of run steps.
-`beta.threads.runs.steps.awith_raw_response.list()`: Asynchronous listing of run steps with a raw response.
- `beta.threads.runs.steps.aretrieve()`: Asynchronous retrieval of a run step.
-`beta.threads.runs.steps.awith_raw_response.retrieve()`: Asynchronous retrieval of a run step with a raw response.

### Run Steps (Continued)

### Files (Beta)

- `beta.files.retrieve(file_id)`: Retrieves a file
- `beta.files.with_raw_response.retrieve(file_id)`: Retrieves a file with a raw response
- `beta.files.delete(file_id)`: Deletes a file
-`beta.files.with_raw_response.delete(file_id)`: Deletes a file with a raw response.
-`beta.files.list(**kwargs)`: Lists files
    - Parameters include:
         - `order` (str, optional): Sorts by 'created_at', order can be "asc" or "desc"
         - `limit` (int, optional): Limits the number of returned files
         - `after` (str, optional): Returns elements after the given cursor
         - `before` (str, optional): Returns elements before the given cursor
-`beta.files.with_raw_response.list(**kwargs)`: Lists files with a raw response.
-`beta.files.aretrieve()`: Asynchronous retrieval of a file.
- `beta.files.awith_raw_response.retrieve()`: Asynchronous retrieval of a file with a raw response.
- `beta.files.adelete()`: Asynchronous deletion of a file
-`beta.files.awith_raw_response.delete()`: Asynchronous deletion of a file with a raw response.
- `beta.files.alist()`: Asynchronous file listing
-`beta.files.awith_raw_response.list()`: Asynchronous file listing with a raw response.

### Usage

- The SDK uses standard python error handling via exceptions.
- The SDK supports both synchronous and asynchronous calls.
- Response objects are standard python classes and can be accessed via standard dot notation.