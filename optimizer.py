from superagi.tools.base_tool import BaseTool
import subprocess

class CodeOptimizerTool(BaseTool):
    name = "CodeOptimizer"
    description = "Automatycznie optymalizuje kod źródłowy."

    def _execute(self, file_path: str) -> str:
        """Optymalizuje kod przy użyciu Black."""
        try:
            subprocess.run(["black", file_path], capture_output=True, text=True)
            return f"Kod w pliku {file_path} został zoptymalizowany."
        except Exception as e:
            return f"Błąd podczas optymalizacji kodu: {str(e)}"
