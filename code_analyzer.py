from superagi.tools.base_tool import BaseTool
import subprocess

class CodeAnalyzerTool(BaseTool):
    name = "CodeAnalyzer"
    description = "Analizuje kod w poszukiwaniu błędów i nieefektywności."

    def _execute(self, file_path: str) -> str:
        """Uruchamia analizę kodu przy użyciu Flake8."""
        try:
            result = subprocess.run(["flake8", file_path], capture_output=True, text=True)
            return result.stdout if result.stdout else "Brak błędów w kodzie."
        except Exception as e:
            return f"Błąd podczas analizy kodu: {str(e)}"
