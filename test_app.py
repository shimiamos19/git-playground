import subprocess
import sys


def test_app_runs_and_says_hello():
    result = subprocess.run([sys.executable, "app.py"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "Hello DevOps" in result.stdout