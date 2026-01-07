"""
Math Tutor using Anthropic's Claude API with Extended Thinking.

This module provides a math tutoring interface that uses Claude's extended thinking
capability to solve mathematical problems.
"""

import anthropic
import os


# Initialize conversation history
conversationHistory = []


def mathTutor(question, mode, use_thinking=True):
    """
    Math tutor function that uses Anthropic's Claude API with optional extended thinking.
    
    Args:
        question (str): The math question to ask
        mode (str): The mode of operation (currently unused, reserved for future use)
        use_thinking (bool): Whether to enable extended thinking (default: True)
                            Note: Extended thinking requires API support
    
    Returns:
        tuple: (thinking_text, response_text) - The thinking process and final response
    
    Raises:
        ValueError: If API key is not set
        anthropic.APIError: If there's an API error
    
    Note:
        The extended thinking feature (thinking parameter) may require specific API access.
        If you encounter errors, try setting use_thinking=False.
    """
    # Get API key from environment variable
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    # Initialize the Anthropic client
    client = anthropic.Anthropic(api_key=api_key)
    
    # Add user question to conversation history
    conversationHistory.append({
        'role': 'user',
        'content': question
    })
    
    # Prepare message parameters
    message_params = {
        'max_tokens': 6000,
        'model': 'claude-sonnet-4-20250514',
        'messages': conversationHistory
    }
    
    # Add thinking parameter if enabled
    # Note: This feature may require specific API access or model support
    if use_thinking:
        message_params['thinking'] = {
            'type': 'enabled',
            'budget_tokens': 5000
        }
    
    # Create message
    try:
        messages = client.messages.create(**message_params)
    except Exception as e:
        # If thinking parameter causes issues, provide helpful error message
        if use_thinking and ('thinking' in str(e).lower() or 'parameter' in str(e).lower()):
            raise ValueError(
                f"Extended thinking feature may not be available: {e}\n"
                "Try calling mathTutor with use_thinking=False"
            ) from e
        raise
    
    # Extract thinking and response text from the message
    thinking_text = None
    response_text = None
    
    for response in messages.content:
        if response.type == 'thinking':
            thinking_text = response.thinking
        elif response.type == 'text':
            response_text = response.text
    
    # Add assistant response to conversation history
    if response_text:
        conversationHistory.append({
            'role': 'assistant',
            'content': response_text
        })
    
    return thinking_text, response_text


def resetConversation():
    """Reset the conversation history."""
    global conversationHistory
    conversationHistory = []


if __name__ == "__main__":
    # Example usage
    try:
        question = "What is the derivative of x^2 + 3x + 5?"
        thinking, answer = mathTutor(question, mode="default")
        
        print("Question:", question)
        print("\n--- Claude's Thinking Process ---")
        print(thinking)
        print("\n--- Answer ---")
        print(answer)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set the ANTHROPIC_API_KEY environment variable")
    except Exception as e:
        print(f"An error occurred: {e}")
