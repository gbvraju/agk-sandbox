"""Tests of the wordcount CLI, run as a subprocess."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

CLI = Path(__file__).resolve().parents[1] / "src" / "wordcount.py"


def run_cli(data: bytes) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run([sys.executable, str(CLI)], input=data, capture_output=True, check=False)


def test_counts_whitespace_separated_words():
    """REQ-101 AC1: prints the count of whitespace-separated words on stdin."""
    result = run_cli(b"one  two\tthree\nfour\n")
    assert result.returncode == 0
    assert result.stdout.decode().strip() == "4"


def test_empty_input_prints_zero():
    """REQ-101 AC2: empty input prints 0."""
    result = run_cli(b"")
    assert result.returncode == 0
    assert result.stdout.decode().strip() == "0"


def test_non_utf8_input_is_refused_without_echoing_bytes():
    """REQ-102 AC1: exit code 2 and a message naming the input encoding setting, never the bytes."""
    result = run_cli(b"caf\xe9 \xff\xfe")
    assert result.returncode == 2
    assert result.stdout == b""
    message = result.stderr.decode()
    assert "UTF-8" in message
    assert "\xe9" not in message
    assert "\\xe9" not in message
    assert "\\xff" not in message
