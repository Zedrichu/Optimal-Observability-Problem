import re
from typing import Tuple, Callable, List

def parse_threshold(arg: str) -> Tuple[List[int], Callable[[int, int], bool]]:
    sign_idx = arg.find('<')
    if sign_idx == -1:
        raise ValueError("No sign in threshold")
    sign = (lambda x, y: x <= y) if arg[sign_idx + 1] == '=' else (lambda x, y: x < y)

    terms = list(map(int, re.findall(r"\d+", arg)))
    assert len(terms) > 0
    return terms, sign

def get_observation_marker(obs_class: int, use_color: bool = True, binary: bool = False) -> str:
    """Get colored circle or digit for observation class using ANSI colors when appropriate.

    Args:
        obs_class: The observation class number (1-9)
        use_color: If True, use ANSI colors. If False, use plain symbols.
        binary: If True, use on/off symbols instead of digits.
    """
    if use_color:
        # ANSI color codes: red, green, blue, yellow, magenta, cyan, white, bright_black, bright_white
        colors = [
            '\033[91m●\033[0m',  # Bright red
            '\033[92m●\033[0m',  # Bright green
            '\033[94m●\033[0m',  # Bright blue
            '\033[93m●\033[0m',  # Bright yellow
            '\033[95m●\033[0m',  # Bright magenta
            '\033[96m●\033[0m',  # Bright cyan
            '\033[97m●\033[0m',  # Bright white
            '\033[90m●\033[0m',  # Bright black (gray)
            '\033[37m●\033[0m',  # White
        ]
        if binary:
            return colors[0] if obs_class == 1 else colors[1]
        if obs_class <= 0 or obs_class > len(colors):
            return '○'  # Default for invalid classes
        return colors[obs_class - 1]
    else:
        if binary:
            return "○" if obs_class == 0 else "●"
        # Plain ASCII numbers for file output (monospace)
        if obs_class <= 0 or obs_class > 9:
            return '#'  # Default for invalid classes
        return str(obs_class)

def convert_text_to_html(text: str, title: str = "World Visualization") -> str:
    """Convert ANSI-colored text to HTML.

    Args:
        text: Text with ANSI color codes
        title: HTML page title

    Returns:
        Complete HTML document as string
    """
    # Map ANSI color codes to CSS colors
    ansi_to_css = {
        '91': '#ff5555',  # Bright red
        '92': '#50fa7b',  # Bright green
        '94': '#8be9fd',  # Bright blue
        '93': '#f1fa8c',  # Bright yellow
        '95': '#ff79c6',  # Bright magenta
        '96': '#8be9fd',  # Bright cyan
        '97': '#f8f8f2',  # Bright white
        '90': '#6272a4',  # Bright black (gray)
        '37': '#f8f8f2',  # White
    }

    # Convert ANSI codes to HTML spans
    def replace_ansi(match):
        code = match.group(1)
        content = match.group(2)
        color = ansi_to_css.get(code, '#ffffff')
        return f'<span style="color: {color}; font-weight: bold;">{content}</span>'

    # Pattern: \033[XXm CONTENT \033[0m
    html_text = re.sub(r'\033\[(\d+)m([^\033]+)\033\[0m', replace_ansi, text)

    # Escape any remaining HTML characters
    html_text = html_text.replace('&', '&amp;').replace('<span', '###SPAN###').replace('</span>', '###/SPAN###')
    html_text = html_text.replace('###SPAN###', '<span').replace('###/SPAN###', '</span>')

    # Build complete HTML document
    html = f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{title}</title>
            <style>
                body {{
                    background-color: #282a36;
                    color: #f8f8f2;
                    font-family: 'Courier New', Consolas, monospace;
                    padding: 20px;
                    margin: 0;
                }}
                pre {{
                    background-color: #1e1f29;
                    padding: 20px;
                    border-radius: 5px;
                    overflow-x: auto;
                    line-height: 1.4;
                }}
            </style>
        </head>
        <body>
            <pre>{html_text}</pre>
        </body>
        </html>"""
    return html
