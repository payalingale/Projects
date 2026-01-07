# Math Tutor - Before and After Comparison

## ❌ ORIGINAL CODE (WITH ERRORS)

```python
def mathTutor(question,mode):
  client = anthropic.Anthropic(api_key=api_key)
  converstionHistory.append({
        'role': 'user',
        'content': question
    })

  messages = client.messages.create(
    max_tokens=6000,
    model='claude-sonnet-4-20250514',
    thinking={
      'type':'enabled',
      'budget_tokens':5000
    },
    messages=converstionHistory
  )
  thinking_text = None
  response_text = None
for response in messages.content:  # ← INDENTATION ERROR
  if response.type == 'thinking':
    thinking_text = response.thinking
  elif response.type == 'text':
    response_text = response.text
if response_text:
  converstionHistory.append({
    'role':'assistant',
    'answer':response_text  # ← WRONG KEY: should be 'content', not 'answer'
  })

return thinking_text, response_text
```

### Errors in Original Code:
1. ❌ Missing `import anthropic` statement
2. ❌ Variable `api_key` is undefined
3. ❌ Variable `converstionHistory` is undefined (also typo: should be "conversation")
4. ❌ Indentation error: `for` loop is not properly indented
5. ❌ Wrong dictionary key: uses `'answer'` instead of `'content'`
6. ❌ No error handling
7. ❌ `return` statement indentation seems to be outside function

---

## ✅ CORRECTED CODE

```python
"""
Math Tutor using Anthropic's Claude API with Extended Thinking.
"""

import anthropic  # ← FIXED: Added import
import os

# Initialize conversation history
conversationHistory = []  # ← FIXED: Initialized variable and fixed typo


def mathTutor(question, mode):
    """
    Math tutor function that uses Anthropic's Claude API.
    
    Args:
        question (str): The math question to ask
        mode (str): The mode of operation
    
    Returns:
        tuple: (thinking_text, response_text)
    
    Raises:
        ValueError: If API key is not set
    """
    # Get API key from environment variable
    api_key = os.environ.get('ANTHROPIC_API_KEY')  # ← FIXED: Properly get API key
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    client = anthropic.Anthropic(api_key=api_key)
    
    # Add user question to conversation history
    conversationHistory.append({  # ← FIXED: Fixed typo
        'role': 'user',
        'content': question
    })
    
    # Create message with extended thinking
    messages = client.messages.create(
        max_tokens=6000,
        model='claude-sonnet-4-20250514',
        thinking={
            'type': 'enabled',
            'budget_tokens': 5000
        },
        messages=conversationHistory
    )
    
    # Extract thinking and response text
    thinking_text = None
    response_text = None
    
    for response in messages.content:  # ← FIXED: Proper indentation
        if response.type == 'thinking':
            thinking_text = response.thinking
        elif response.type == 'text':
            response_text = response.text
    
    # Add assistant response to conversation history
    if response_text:
        conversationHistory.append({
            'role': 'assistant',
            'content': response_text  # ← FIXED: Changed 'answer' to 'content'
        })
    
    return thinking_text, response_text  # ← FIXED: Proper indentation
```

---

## Key Differences Summary

| Issue | Original | Fixed |
|-------|----------|-------|
| Import statement | ❌ Missing | ✅ `import anthropic` |
| API key | ❌ Undefined `api_key` | ✅ `os.environ.get('ANTHROPIC_API_KEY')` |
| Conversation history | ❌ Undefined `converstionHistory` | ✅ Initialized `conversationHistory = []` |
| Indentation | ❌ `for` loop not indented | ✅ Properly indented at 4 spaces |
| Dictionary key | ❌ `'answer'` | ✅ `'content'` |
| Error handling | ❌ None | ✅ Validates API key exists |
| Documentation | ❌ None | ✅ Docstrings added |
| Return statement | ❌ Unclear indentation | ✅ Properly indented |

---

## Why the Original Code Failed

### Error 1: IndentationError
Python would throw: `IndentationError: unexpected indent`

The `for` loop must be at the same indentation level as the statements above it within the function.

### Error 2: NameError  
Python would throw: `NameError: name 'anthropic' is not defined`

The module must be imported before use.

### Error 3: NameError
Python would throw: `NameError: name 'api_key' is not defined`

The variable must be defined before being passed to the Anthropic client.

### Error 4: NameError
Python would throw: `NameError: name 'converstionHistory' is not defined`

The list must be initialized before appending to it.

### Error 5: API Error
Even if the code ran, the Anthropic API would reject messages with `'answer'` key instead of `'content'` key, causing the conversation history to be malformed for subsequent requests.

---

## How to Use the Fixed Code

1. **Set up environment:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. **Run the code:**
```python
from math_tutor import mathTutor

thinking, answer = mathTutor("What is the derivative of x^2?", mode="default")
print("Answer:", answer)
```

3. **Example output:**
```
Answer: The derivative of x^2 is 2x.
```
