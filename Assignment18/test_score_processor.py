import pytest
from score_processor import ScoreProcessor


def test_valid_score_file(tmp_path):

    file = tmp_path / "score.txt"
    file.write_text("5")

    processor = ScoreProcessor()

    assert processor.process_score_file(str(file)) == 50


def test_missing_file():

    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing.txt")


def test_invalid_number_format(tmp_path):

    file = tmp_path / "invalid.txt"
    file.write_text("abc")

    processor = ScoreProcessor()

    with pytest.raises(ValueError):
        processor.process_score_file(str(file))