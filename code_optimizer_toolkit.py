from superagi.tools.toolkit import BaseToolkit
from .code_analyzer import CodeAnalyzerTool
from .optimizer import CodeOptimizerTool

class CodeOptimizerToolkit(BaseToolkit):
    name = "Code Optimizer Toolkit"
    description = "Zestaw narzędzi do analizy i optymalizacji kodu Python."

    tools = [CodeAnalyzerTool(), CodeOptimizerTool()]
