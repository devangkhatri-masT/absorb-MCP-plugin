import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Absorb Documentation Server")

DOCS_DIR = r"d:\working docs\absorb_docs"

@mcp.tool()
def trigger_absorb_pipeline(target: str = "all", repo_path: str = "d:\CreatorOS") -> str:
    """
    Trigger the Absorb documentation pipeline.
    target: 'user', 'developer', 'agent', or 'all'
    repo_path: Absolute path to the repository to document.
    """
    return f"Instruction for Agent: Please invoke the `/absorb` slash command on {repo_path} with target={target}."

@mcp.tool()
def analyze_commit_delta(commit_start: str, commit_end: str, repo_path: str) -> str:
    """
    Analyzes the git commit history between two hashes and outputs a Markdown summary.
    """
    return f"Instruction for Agent: Please invoke the `commit_analyzer_agent` subagent. Instruct it to navigate to '{repo_path}', run 'git log -p {commit_start}..{commit_end}', analyze what changed and why, and follow the `commit-analyzer` skill instructions to output a Delta Report."

@mcp.resource("absorb://docs/{target}/{module}")
def get_module_docs(target: str, module: str) -> str:
    """
    Fetch the generated documentation for a specific module and target audience.
    target: 'user', 'developer', or 'agent'
    """
    file_path = os.path.join(DOCS_DIR, target, f"{module}.md")
    if not os.path.exists(file_path):
        return f"Documentation for {module} (target: {target}) not found or pipeline hasn't run yet."
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    mcp.run()
