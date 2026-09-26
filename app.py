from fastmcp import FastMCP
app = FastMCP("My MCP Server")

# 提供一個加法的工具
@app.tool
def add(n1:int, n2:int) -> int: #指定輸入的參數及輸出的參數為 int
    """Add Two Numbers""" # AI 透過程式內的說明來決定要不要調用這個工具，所以說明很重要
    return n1 + n2