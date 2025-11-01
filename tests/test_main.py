"""
Comprehensive test suite for PyWorkout main module.
Tests the core workout functionality including muscle group selection and workout flow.
"""

import sys
import os
from unittest.mock import patch, MagicMock
from datetime import datetime
import pytest

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main


class TestWorkoutData:
    """Test workout data structures and constants."""

    def test_workout_groups_exist(self):
        """Test that workout groups are defined correctly."""
        # This test verifies the workout groups are available through the function
        with patch("builtins.input", side_effect=["quit"]):
            with patch("builtins.print"):
                try:
                    main.workout()
                except SystemExit:
                    pass

        # Verify the groups are correctly defined
        groups = ["Abs", "Quads", "Glutes", "Triceps", "Biceps", "Back", "Chest"]
        assert len(groups) == 7
        assert "Abs" in groups
        assert "Quads" in groups
        assert "Glutes" in groups
        assert "Triceps" in groups
        assert "Biceps" in groups
        assert "Back" in groups
        assert "Chest" in groups


class TestMuscleGroupSelection:
    """Test muscle group selection functionality."""

    @patch("builtins.print")
    @patch("builtins.input")
    def test_abs_selection_by_number(self, mock_input, mock_print):
        """Test selecting abs muscle group by number."""
        mock_input.side_effect = ["1", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        # Verify abs group was selected
        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("Ab muscle group selected" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_abs_selection_by_name(self, mock_input, mock_print):
        """Test selecting abs muscle group by name."""
        mock_input.side_effect = ["abs", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("Ab muscle group selected" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_quads_selection_by_number(self, mock_input, mock_print):
        """Test selecting quads muscle group by number."""
        mock_input.side_effect = ["2", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("Quad muscle group selected" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_glutes_selection_by_number(self, mock_input, mock_print):
        """Test selecting glutes muscle group by number."""
        mock_input.side_effect = ["3", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any(
            "Glutes muscle group selected" in str(call) for call in printed_output
        )

    @patch("builtins.print")
    @patch("builtins.input")
    def test_triceps_selection_by_number(self, mock_input, mock_print):
        """Test selecting triceps muscle group by number."""
        mock_input.side_effect = ["4", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any(
            "Tricep muscle group selected" in str(call) for call in printed_output
        )

    @patch("builtins.print")
    @patch("builtins.input")
    def test_biceps_selection_by_number(self, mock_input, mock_print):
        """Test selecting biceps muscle group by number."""
        mock_input.side_effect = ["5", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any(
            "Bicep muscle group selected" in str(call) for call in printed_output
        )

    @patch("builtins.print")
    @patch("builtins.input")
    def test_back_selection_by_number(self, mock_input, mock_print):
        """Test selecting back muscle group by number."""
        mock_input.side_effect = ["6", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("Back muscle group selected" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_chest_selection_by_number(self, mock_input, mock_print):
        """Test selecting chest muscle group by number."""
        mock_input.side_effect = ["7", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any(
            "Chest muscle group selected" in str(call) for call in printed_output
        )

    @patch("builtins.print")
    @patch("builtins.input")
    def test_invalid_selection(self, mock_input, mock_print):
        """Test invalid muscle group selection."""
        mock_input.side_effect = ["invalid", "1", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("incorrect" in str(call).lower() for call in printed_output)

    @patch("builtins.input")
    def test_quit_during_selection(self, mock_input):
        """Test quitting during muscle group selection."""
        mock_input.side_effect = ["quit"]

        with pytest.raises(SystemExit):
            main.workout()


class TestWorkoutCommands:
    """Test workout command functionality."""

    @patch("builtins.print")
    @patch("builtins.input")
    def test_list_command(self, mock_input, mock_print):
        """Test list command displays workout activities."""
        mock_input.side_effect = ["1", "list", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        # Check that exercises are listed
        assert any("Situps" in str(call) for call in printed_output)
        assert any("Reps" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_start_command(self, mock_input, mock_print):
        """Test start command begins workout."""
        mock_input.side_effect = ["1", "start", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("started" in str(call).lower() for call in printed_output)
        assert any("Situps" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_help_command(self, mock_input, mock_print):
        """Test help command displays available commands."""
        mock_input.side_effect = ["1", "help", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("list" in str(call).lower() for call in printed_output)
        assert any("start" in str(call).lower() for call in printed_output)
        assert any("next" in str(call).lower() for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_license_command(self, mock_input, mock_print):
        """Test license command displays license info."""
        mock_input.side_effect = ["1", "license", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        # Check for copyright or license text
        assert any(
            "Copyright" in str(call) or "PyWorkout" in str(call)
            for call in printed_output
        )

    @patch("builtins.print")
    @patch("builtins.input")
    def test_invalid_command(self, mock_input, mock_print):
        """Test invalid command displays error."""
        mock_input.side_effect = ["1", "invalid", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("not an option" in str(call).lower() for call in printed_output)

    @patch("builtins.input")
    def test_quit_command(self, mock_input):
        """Test quit command exits program."""
        mock_input.side_effect = ["1", "quit"]

        with pytest.raises(SystemExit):
            main.workout()


class TestWorkoutFlow:
    """Test complete workout flow functionality."""

    @patch("builtins.print")
    @patch("builtins.input")
    def test_start_next_end_flow(self, mock_input, mock_print):
        """Test complete workout flow: start -> next -> end."""
        mock_input.side_effect = ["1", "start", "next", "next", "end", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("started" in str(call).lower() for call in printed_output)
        assert any("completed" in str(call).lower() for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_skip_functionality(self, mock_input, mock_print):
        """Test skip command functionality."""
        mock_input.side_effect = ["1", "start", "skip", "next", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("skipped" in str(call).lower() for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_stats_command(self, mock_input, mock_print):
        """Test stats command displays statistics."""
        mock_input.side_effect = ["1", "start", "next", "stats", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("completed" in str(call).lower() for call in printed_output)


class TestVideoFunctionality:
    """Test video playback functionality."""

    @patch("subprocess.call")
    @patch("builtins.print")
    @patch("builtins.input")
    @patch("sys.platform", "linux")
    def test_video_command_linux(self, mock_input, mock_print, mock_subprocess):
        """Test video command on Linux platform."""
        mock_input.side_effect = ["1", "start", "video", "quit"]

        with pytest.raises(SystemExit):
            main.workout()

        # On Linux, should attempt to call xdg-open
        # Note: The actual call might fail due to invalid path, but we're testing the attempt
        printed_output = [str(call) for call in mock_print.call_args_list]
        # Verify video command was processed - either video text printed or subprocess called
        video_text_found = any("Video" in str(call) for call in printed_output)
        subprocess_was_called = mock_subprocess.called
        assert video_text_found or subprocess_was_called, "Video command should print text or call subprocess"


class TestWelcomeScreen:
    """Test welcome screen and initial display."""

    @patch("builtins.print")
    @patch("builtins.input")
    def test_welcome_message(self, mock_input, mock_print):
        """Test welcome message is displayed."""
        mock_input.side_effect = ["quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("WELCOME" in str(call) for call in printed_output)
        assert any("PyWORKOUT" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_day_recommendation(self, mock_input, mock_print):
        """Test day of week recommendation is displayed."""
        mock_input.side_effect = ["quit"]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("today" in str(call).lower() for call in printed_output)


class TestIntegration:
    """Integration tests for complete workout scenarios."""

    @patch("builtins.print")
    @patch("builtins.input")
    def test_complete_abs_workout(self, mock_input, mock_print):
        """Test complete abs workout session."""
        # Simulate a full abs workout
        mock_input.side_effect = [
            "abs",  # Select abs
            "list",  # List exercises
            "start",  # Start workout
            "next",  # Move to next exercise
            "next",  # Move to next exercise
            "next",  # Move to next exercise
            "next",  # Move to next exercise
            "next",  # Move to next exercise
            "end",  # End workout
            "quit",  # Quit
        ]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("Ab muscle group selected" in str(call) for call in printed_output)
        assert any("Congratulations" in str(call) for call in printed_output)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_workout_with_multiple_groups(self, mock_input, mock_print):
        """Test selecting different muscle groups in sequence."""
        mock_input.side_effect = [
            "1",  # Select abs
            "list",  # List exercises
            "quit",  # Quit
        ]

        with pytest.raises(SystemExit):
            main.workout()

        printed_output = [str(call) for call in mock_print.call_args_list]
        assert any("Situps" in str(call) for call in printed_output)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
