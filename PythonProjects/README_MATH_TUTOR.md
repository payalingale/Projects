# Math Tutor with Claude's Extended Thinking

A Python implementation of a math tutoring system using Anthropic's Claude API with extended thinking capability.

## 🎯 Problem Solved

This implementation fixes multiple critical errors in the original mathTutor function:

1. ✅ **Fixed indentation error** - Properly indented the `for` loop
2. ✅ **Fixed API message format** - Changed `'answer'` to `'content'` in conversation history
3. ✅ **Added missing imports** - Added `import anthropic` and `import os`
4. ✅ **Fixed variable initialization** - Initialized `conversationHistory` (also fixed typo)
5. ✅ **Added API key handling** - Proper environment variable handling with error checking
6. ✅ **Added error handling** - Comprehensive exception handling
7. ✅ **Added documentation** - Docstrings and inline comments

## 📁 Files

- **`math_tutor.py`** - Main implementation with fixed code
- **`test_math_tutor.py`** - Unit tests for the math tutor
- **`MATH_TUTOR_FIXES.md`** - Detailed explanation of all fixes
- **`BEFORE_AFTER_COMPARISON.md`** - Side-by-side comparison of original vs fixed code

## 🚀 Installation

1. **Install the Anthropic Python SDK:**
```bash
pip install anthropic
```

2. **Set your API key:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or add it to your `.env` file or shell profile.

## 💻 Usage

### Basic Usage

```python
from math_tutor import mathTutor

# Ask a math question
question = "What is the derivative of x^2 + 3x + 5?"
thinking, answer = mathTutor(question, mode="default")

print("Question:", question)
print("\nThinking Process:", thinking)
print("\nAnswer:", answer)
```

### Multiple Questions (Conversation)

```python
from math_tutor import mathTutor, resetConversation

# First question
q1 = "What is the integral of 2x?"
thinking1, answer1 = mathTutor(q1, mode="default")
print("Q1:", answer1)

# Follow-up question (uses conversation history)
q2 = "Can you verify that answer by taking the derivative?"
thinking2, answer2 = mathTutor(q2, mode="default")
print("Q2:", answer2)

# Start fresh conversation
resetConversation()
```

### Running the Example

```bash
# Make sure API key is set
export ANTHROPIC_API_KEY='your-key-here'

# Run the example
python PythonProjects/math_tutor.py
```

## 🧪 Testing

Run the unit tests:

```bash
cd PythonProjects
python test_math_tutor.py
```

**Note:** Tests will be skipped if the `anthropic` module is not installed.

## 📖 Key Features

- **Extended Thinking**: Uses Claude's extended thinking feature to show the reasoning process
- **Conversation History**: Maintains context across multiple questions
- **Error Handling**: Proper validation and error messages
- **Type Hints**: Clear function signatures
- **Documentation**: Comprehensive docstrings

## ⚠️ Common Errors (Original Code)

The original code had these issues:

```python
# ❌ WRONG - Indentation error
for response in messages.content:  # Not properly indented

# ❌ WRONG - Missing import
client = anthropic.Anthropic()  # anthropic not imported

# ❌ WRONG - Undefined variable
converstionHistory.append(...)  # Variable not initialized (also typo)

# ❌ WRONG - Undefined API key
api_key=api_key  # Variable not defined

# ❌ WRONG - Incorrect key name
'answer': response_text  # Should be 'content'
```

## ✅ Fixed Implementation

All issues are resolved in `math_tutor.py`. See `MATH_TUTOR_FIXES.md` for detailed explanations.

## 🔒 Security

- API keys are loaded from environment variables, not hardcoded
- Sensitive data is not logged or exposed
- Proper error handling prevents information leakage

## 📚 Documentation

For more details, see:
- **[MATH_TUTOR_FIXES.md](./MATH_TUTOR_FIXES.md)** - Detailed error analysis and fixes
- **[BEFORE_AFTER_COMPARISON.md](./BEFORE_AFTER_COMPARISON.md)** - Side-by-side code comparison

## 🤝 API Reference

### `mathTutor(question, mode, use_thinking=True)`

Main function for math tutoring.

**Parameters:**
- `question` (str): The math question to ask
- `mode` (str): Mode of operation (reserved for future use)
- `use_thinking` (bool): Whether to enable extended thinking (default: True)
  - **Note:** Extended thinking may require specific API access. If you get parameter errors, try `use_thinking=False`

**Returns:**
- `tuple`: (thinking_text, response_text)
  - `thinking_text`: Claude's internal reasoning process (None if thinking disabled or not supported)
  - `response_text`: The final answer

**Raises:**
- `ValueError`: If ANTHROPIC_API_KEY is not set, or if thinking parameter is not supported
- `anthropic.APIError`: If there's an API communication error

### `resetConversation()`

Clears the conversation history to start fresh.

**Parameters:** None

**Returns:** None

## 📝 Example Output

```
Question: What is the derivative of x^2 + 3x + 5?

--- Claude's Thinking Process ---
To find the derivative, I'll use the power rule:
- d/dx(x^2) = 2x
- d/dx(3x) = 3
- d/dx(5) = 0
Adding these together...

--- Answer ---
The derivative of x^2 + 3x + 5 is 2x + 3.
```

## 🐛 Troubleshooting

**Error: "ANTHROPIC_API_KEY environment variable is not set"**
- Solution: Set your API key with `export ANTHROPIC_API_KEY='your-key'`

**Error: "No module named 'anthropic'"**
- Solution: Install with `pip install anthropic`

**Error: "Extended thinking feature may not be available" or parameter errors**
- Solution: The `thinking` parameter may require specific API access or model support
- Try using: `mathTutor(question, mode, use_thinking=False)`
- This disables extended thinking but the function will still work

**Tests are skipped**
- This is normal if anthropic module is not installed
- Install anthropic to run full test suite

## 📄 License

This project is part of the payalingale/Projects repository.

## 🙋 Support

For issues or questions, please refer to the detailed documentation in:
- `MATH_TUTOR_FIXES.md` - Error explanations
- `BEFORE_AFTER_COMPARISON.md` - Code comparison
