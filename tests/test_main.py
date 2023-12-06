"""Test the main program logic."""
#pylint: disable=import-error, no-name-in-module

from io import StringIO
from unittest.mock import patch
from main import run_program  # Assuming this is the function that contains your main program logic

def test_welcome_message():
    """Test that the welcome message is printed."""
    with patch('sys.stdout', new=StringIO()) as fake_out:
        run_program()
        assert "WELCOME TO PyWORKOUT" in fake_out.getvalue()

def test_group_options():
    """Test that the group options are printed."""
    with patch('sys.stdout', new=StringIO()) as fake_out:
        run_program()
        assert "Please select a group from those below." in fake_out.getvalue()

def test_day_reminder():
    """Test that the day reminder is printed."""
    with patch('sys.stdout', new=StringIO()) as fake_out:
        run_program()
        assert "A reminder that today is: " in fake_out.getvalue()
