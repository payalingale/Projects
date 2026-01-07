"""
Unit tests for the math_tutor module.

These tests verify that the mathTutor function is properly structured
and handles errors correctly.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import, but skip tests if anthropic module is not installed
try:
    from math_tutor import mathTutor, resetConversation, conversationHistory
    ANTHROPIC_AVAILABLE = True
except ImportError as e:
    ANTHROPIC_AVAILABLE = False
    IMPORT_ERROR = str(e)


@unittest.skipUnless(ANTHROPIC_AVAILABLE, "anthropic module not installed")
class TestMathTutor(unittest.TestCase):
    """Test cases for the math_tutor module."""
    
    def setUp(self):
        """Reset conversation history before each test."""
        resetConversation()
    
    def test_missing_api_key_raises_error(self):
        """Test that missing API key raises ValueError."""
        # Save original API key if it exists
        original_key = os.environ.get('ANTHROPIC_API_KEY')
        
        # Remove API key
        if 'ANTHROPIC_API_KEY' in os.environ:
            del os.environ['ANTHROPIC_API_KEY']
        
        try:
            # Should raise ValueError
            with self.assertRaises(ValueError) as context:
                mathTutor("What is 2+2?", mode="default")
            
            self.assertIn("ANTHROPIC_API_KEY", str(context.exception))
        finally:
            # Restore original key if it existed
            if original_key:
                os.environ['ANTHROPIC_API_KEY'] = original_key
    
    def test_conversation_history_initialized(self):
        """Test that conversation history is initialized as a list."""
        self.assertIsInstance(conversationHistory, list)
    
    def test_reset_conversation(self):
        """Test that resetConversation clears the history."""
        # Manually add something to history
        conversationHistory.append({'role': 'user', 'content': 'test'})
        self.assertEqual(len(conversationHistory), 1)
        
        # Reset should clear it
        resetConversation()
        self.assertEqual(len(conversationHistory), 0)
    
    def test_function_signature(self):
        """Test that mathTutor has the correct signature."""
        import inspect
        sig = inspect.signature(mathTutor)
        params = list(sig.parameters.keys())
        
        # Should have 'question' and 'mode' parameters
        self.assertEqual(len(params), 2)
        self.assertIn('question', params)
        self.assertIn('mode', params)


if __name__ == '__main__':
    print("Running math_tutor tests...")
    if not ANTHROPIC_AVAILABLE:
        print(f"Warning: Skipping tests - {IMPORT_ERROR}")
        print("To run full tests, install anthropic: pip install anthropic")
    unittest.main(verbosity=2)
