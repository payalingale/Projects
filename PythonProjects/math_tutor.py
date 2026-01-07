"""
Math Tutor using Anthropic's Claude API with Extended Thinking.

This module provides a math tutoring interface that uses Claude's extended thinking
capability to solve mathematical problems.
"""

import anthropic
import os


# Initialize conversation history
conversationHistory = []


def mathTutor(question, mode):
    """
    Math tutor function that uses Anthropic's Claude API with extended thinking.
    
    Args:
        question (str): The math question to ask
        mode (str): The mode of operation (currently unused, reserved for future use)
    
    Returns:
        tuple: (thinking_text, response_text) - The thinking process and final response
    
    Raises:
        ValueError: If API key is not set
        anthropic.APIError: If there's an API error
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
    
    # Create message with extended thinking enabled
    messages = client.messages.create(
        max_tokens=6000,
        model='claude-sonnet-4-20250514',
        thinking={
            'type': 'enabled',
            'budget_tokens': 5000
        },
        messages=conversationHistory
    )
    
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
