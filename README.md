# Task-2_HiringHood
# AI Chatbot with DeepSeek API

A full-featured AI chatbot application with both CLI and web-based interfaces, powered by the DeepSeek API via OpenRouter.

## Project Overview

This project provides two ways to interact with DeepSeek AI models:

1. **CLI Interface**: Interact with the AI through a command-line interface
2. **Web Interface**: Chat with the AI using a responsive web application

Both interfaces connect to the DeepSeek API to provide AI-powered responses with proper formatting and error handling.

## Features

- **DeepSeek API Integration**: Direct connection to DeepSeek Chat models through OpenRouter
- **User Input Handling**: Support for conversational interactions
- **Response Formatting**: Markdown support with bullet points and numbered lists
- **Error Handling & Logging**: Robust error management and logging
- **Web Interface**: Responsive design with real-time interaction
- **CLI Interface**: Terminal-based interaction for command-line users

## Project Structure

```
ai-chatbot/
├── cli version/
│   ├── cli_chat.py          # CLI interface implementation
│   ├── deepseek_api.py      # DeepSeek API connection logic
│ 
│
├──
│   ├── app.py              # Flask backend application
│   ├── index.html          # Frontend interface
│   ├── requirements.txt    # Python dependencies for web app
│   
│
└── README.md               # This documentation
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- An OpenRouter API key with access to DeepSeek models
- Flask (for web interface)
- Required Python packages (see requirements.txt in each directory)

### CLI Application Setup


1. Install the required packages:
   ```
   pip install -r requirements.txt
2. Navigate to the CLI directory:
   ```
   cd cli version
   ```  ```

3. Run the CLI application:
   ```
   python cli_chat.py
   ```

=### Web Application Setup

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Update the API key in `app.py`:
   ```python
   API_KEY = "your-api-key-here"  # Replace with your API key
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Usage

### CLI Interface

The CLI application provides a simple text-based interface:

- Enter questions or prompts at the prompt
- Type `/exit` or `/quit` to end the session
- Use `/clear` to clear the conversation history
- Special commands like `/bullets` and `/numbers` format responses accordingly

### Web Interface

The web interface offers a more visual way to interact with the DeepSeek API:

- Type your message in the input field and press Enter or click Send
- The AI will respond with formatted text, including bullet points and lists when appropriate
- Use the `/bullets` or `/numbers` commands for specifically formatted responses

## Error Handling

Both interfaces include robust error handling:

- API connection failures
- Timeouts
- Invalid responses
- Rate limiting issues

Errors are logged to `error_log.txt` for debugging purposes.
## ScreenShots
## User Interface
![Screenshot 2025-03-17 235326](https://github.com/user-attachments/assets/d889f9e3-6d15-46de-bad6-cd0682933b81)

## Results
![Screenshot 2025-03-17 233850](https://github.com/user-attachments/assets/20467d4d-1644-43d3-8855-c1e039651f34)


## Future Improvements

- Conversation history persistence
- Additional formatting options
- User authentication
- Multiple model selection
- File upload/download capabilities

## License

[MIT License](LICENSE)
