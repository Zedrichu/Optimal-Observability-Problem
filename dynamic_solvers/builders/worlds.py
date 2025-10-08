from abc import ABC, abstractmethod
from sys import implementation
from typing import List, override
import re


class World(ABC):
    size: int
    actions: List[str]

    @abstractmethod
    def navigate(self, state: int, action: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def dist(self, source: int, target: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def draw_ssp(self, model: dict, goal_state: int, use_color: bool = True) -> str:
        """Draw the world with sensor placements from dictionary model (SSP)."""
        raise NotImplementedError()

    @abstractmethod
    def draw_pop(self, model: dict, goal_state: int, budget: int, use_color: bool = True) -> str:
        """Draw the world with observation classes from dictionary model (POP).

        Args:
            model: The Z3 model solution
            goal_state: The goal state index
            budget: The observation budget
            use_color: If True, use ANSI colors. If False, use plain symbols for file output.
        """
        raise NotImplementedError()

    @staticmethod
    def _get_observation_emoji(obs_class: int, use_color: bool = True) -> str:
        """Get colored circle for observation class using ANSI colors.

        Args:
            obs_class: The observation class number (1-9)
            use_color: If True, use ANSI colors. If False, use plain symbols.
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
            if obs_class <= 0 or obs_class > len(colors):
                return '○'  # Default for invalid classes
            return colors[obs_class - 1]
        else:
            # Plain ASCII numbers for file output (monospace)
            if obs_class <= 0 or obs_class > 9:
                return '0'  # Default for invalid classes
            return str(obs_class)

    @staticmethod
    def to_html(text: str, title: str = "World Visualization") -> str:
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
        html_text = html_text.replace('<', '&lt;').replace('>', '&gt;')
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


class Line(World):
    def __init__(self, length: int):
        self.length = length

        self.size = length
        self.actions = ['l', 'r']

    def navigate(self, state: int, action_idx: int) -> int:
        action = self.actions[action_idx]
        if action == 'l':
            return max(state - 1, 0)
        else:  # action == 'r'
            return min(state + 1, self.length - 1)

    def dist(self, source: int, target: int) -> int:
        return abs(source - target)

    def draw_ssp(self, model: dict, goal_state: int) -> str:
        """Draw line world with sensor placements marked."""
        lines = []

        # Calculate width needed for state numbers
        max_state = self.length - 1
        num_width = len(str(max_state))
        cell_width = num_width + 2  # Add padding

        # State numbers
        state_line = ""
        sensor_line = ""

        for state in range(self.length):
            if state == goal_state:
                state_line += f" {state:{num_width}} "
                # Center the symbol in the cell
                padding = (cell_width - 1) // 2
                sensor_line += " " * padding + "✓" + " " * (cell_width - padding)
            else:
                state_line += f" {state:{num_width}}  "
                sensor_on = model.get(f'ys{state}', 0)
                symbol = "●" if sensor_on == 1 else "○"
                # Center the symbol in the cell
                padding = (cell_width - 1) // 2
                sensor_line += " " * padding + symbol + " " * (cell_width - padding)

        lines.append("Line World:")
        lines.append(state_line)
        lines.append(sensor_line)
        lines.append("\nLegend: ✓=goal, ●=sensor on, ○=sensor off")

        return "\n".join(lines)

    def draw_pop(self, model: dict, goal_state: int, budget: int, use_color: bool = True) -> str:
        """Draw line world with observation classes marked."""
        lines = []

        # Calculate width needed for state numbers
        max_state = self.length - 1
        num_width = len(str(max_state))
        cell_width = num_width + 3  # 1 leading space + num_width + 2 trailing spaces

        # State numbers
        state_line = ""
        obs_line = ""

        for state in range(self.length):
            if state == goal_state:
                state_line += f" {state:{num_width}}  "
                # Center the symbol in the cell
                padding = (cell_width - 1) // 2
                obs_line += " " * padding + "✓" + " " * (cell_width - padding - 1)
            else:
                state_line += f" {state:{num_width}}  "
                # Find which observation class this state belongs to
                obs_class = 0
                for o in range(1, budget + 1):
                    if model.get(f'ys{state}o{o}', 0) == 1:
                        obs_class = o
                        break
                symbol = self._get_observation_emoji(obs_class, use_color)
                # Center the symbol in the cell (ANSI colors don't affect width)
                padding = (cell_width - 1) // 2
                obs_line += " " * padding + symbol + " " * (cell_width - padding - 1)

        lines.append("Line World (POP):")
        lines.append(state_line)
        lines.append(obs_line)

        # Build legend
        legend = "\nLegend: ✓=goal"
        for o in range(1, budget + 1):
            legend += f", {self._get_observation_emoji(o, use_color)}=obs {o}"
        lines.append(legend)

        return "\n".join(lines)


class Grid(World):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.size = width * height
        self.actions = ['l', 'r', 'u', 'd']

    def navigate(self, state: int, action_idx: int) -> int:
        """Navigate in 2D grid based on action"""
        action = self.actions[action_idx]
        x = state % self.width
        y = state // self.width

        if action == 'l':  # left
            if x != 0:
                return state - 1
        elif action == 'r':  # right
            if x != self.width - 1:
                return state + 1
        elif action == 'u':  # up
            if y != 0:
                return state - self.width
        else:  # action == 'd' (down)
            if y != self.height - 1:
                return state + self.width
        return state

        # size_x = 4; size_y = 3; column = 11 % 4 = 3
        # 3 -> 3 % 4 == 3 -> (11 - 3) // 4 == 2
        # 5 -> 5 % 4 == 1 -> (3 - 1) + 6 // 4 = 2 + 1 = 3
        # size_x -> size_y |
        # 0 1 2 3          v  5 4 3 2
        # 4 5 6 7             4 3 2 1
        # 8 9 10 11           3 2 1 0

    def dist(self, source: int, target: int) -> int:
        """
        Compute Manhattan distances between each state and the goal state based on the grid topology.
        """
        # Grid-specific bounds calculation
        goal_column = target % self.width
        column = source % self.width
        return abs(goal_column - column) + (abs(target - source) // self.width)

    def draw_ssp(self, model: dict, goal_state: int) -> str:
        """Draw grid world with sensor placements marked."""
        lines = []
        lines.append(f"Grid World ({self.width}x{self.height}):")
        lines.append("")

        # Calculate width needed for state numbers
        max_state = self.size - 1
        num_width = len(str(max_state))
        cell_width = num_width + 2  # Add padding

        for y in range(self.height):
            state_line = ""
            sensor_line = ""

            for x in range(self.width):
                state = y * self.width + x

                if state == goal_state:
                    state_line += f" {state:{num_width}} "
                    # Center the symbol in the cell
                    padding = (cell_width - 1) // 2
                    sensor_line += " " * padding + "✓" + " " * (cell_width - padding)
                else:
                    state_line += f" {state:{num_width}}  "
                    sensor_on = model.get(f'ys{state}', 0)
                    symbol = "●" if sensor_on == 1 else "○"
                    # Center the symbol in the cell
                    padding = (cell_width - 1) // 2
                    sensor_line += " " * padding + symbol + " " * (cell_width - padding)

            lines.append(state_line)
            lines.append(sensor_line)
            lines.append("")

        lines.append("Legend: ✓=goal, ●=sensor on, ○=sensor off")

        return "\n".join(lines)

    def draw_pop(self, model: dict, goal_state: int, budget: int, use_color: bool = True) -> str:
        """Draw grid world with observation classes marked."""
        lines = []
        lines.append(f"Grid World ({self.width}x{self.height}) (POP):")
        lines.append("")

        # Calculate width needed for state numbers
        max_state = self.size - 1
        num_width = len(str(max_state))
        cell_width = num_width + 3  # 1 leading space + num_width + 2 trailing spaces

        for y in range(self.height):
            state_line = ""
            obs_line = ""

            for x in range(self.width):
                state = y * self.width + x

                if state == goal_state:
                    state_line += f" {state:{num_width}}  "
                    # Center the symbol in the cell
                    padding = (cell_width - 1) // 2
                    obs_line += " " * padding + "✓" + " " * (cell_width - padding)
                else:
                    state_line += f" {state:{num_width}}  "
                    # Find which observation class this state belongs to
                    obs_class = 0
                    for o in range(1, budget + 1):
                        if model.get(f'ys{state}o{o}', 0) == 1:
                            obs_class = o
                            break
                    symbol = self._get_observation_emoji(obs_class, use_color)
                    # Center the symbol in the cell (ANSI colors don't affect width)
                    padding = (cell_width - 1) // 2
                    obs_line += " " * padding + symbol + " " * (cell_width - padding - 1)

            lines.append(state_line)
            lines.append(obs_line)
            lines.append("")

        # Build legend
        legend = "Legend: ✓=goal"
        for o in range(1, budget + 1):
            legend += f", {self._get_observation_emoji(o, use_color)}=obs {o}"
        lines.append(legend)

        return "\n".join(lines)


class Maze(World):
    def __init__(self, width, depth):
        if width % 2 == 0:
            raise ValueError('Width must be odd for maze generation')

        self.width = width
        self.depth = depth

        self.size = width + 3 * (depth - 1)
        self.actions = ['l', 'r', 'u', 'd']

    def navigate(self, state: int, action_index: int) -> int:
        """Navigate in 2D maze based on action"""
        action = self.actions[action_index]
        if action == 'l':
            if 0 < state < self.width:
                return state - 1
        elif action == 'r':
            if 0 <= state < self.width - 1:
                return state + 1
        elif action == 'u':
            if state == self.width:
                return 0
            elif state == self.width + 1:
                return (self.width - 1) // 2
            elif state >= self.width + 2:
                return state - 3
        else:  # action == 'd'
            if state == 0:
                return self.width
            elif state == (self.width - 1) // 2:
                return self.width + 1
            elif self.width - 1 <= state < self.size - 3:
                return state + 3
        return state

    def dist(self, source: int, target: int) -> int:
        """
        Compute shortest-path distances between each state and the goal state based on the maze topology.
        """
        goal_column = target if target < self.width \
                             else (target - self.width) % 3 * (self.width // 2)
        goal_height = 0 if target < self.width \
                        else (target - self.width) // 3 + 1

        if source < self.width:
            return goal_height + abs(source - goal_column)
        else:
            column = (source - self.width) % 3 * (self.width // 2)
            row = (source - self.width) // 3 + 1
            diff = int(goal_column != column)
            return abs(column - goal_column) + abs(row - goal_height + 2 * goal_height * diff)

    def draw_ssp(self, model: dict, goal_state: int) -> str:
        """Draw maze world with sensor placements marked."""
        lines = []
        lines.append(f"Maze World (width={self.width}, depth={self.depth}):")
        lines.append("")

        # Calculate width needed for state numbers
        max_state = self.size - 1
        num_width = len(str(max_state))
        cell_width = num_width + 2  # Add padding

        # Top row (states 0 to width-1)
        top_state_line = ""
        top_sensor_line = ""
        for state in range(self.width):
            if state == goal_state:
                top_state_line += f" {state:{num_width}} "
                padding = (cell_width - 1) // 2
                top_sensor_line += " " * padding + "✓" + " " * (cell_width - padding)
            else:
                top_state_line += f" {state:{num_width}}  "
                sensor_on = model.get(f'ys{state}', 0)
                symbol = "●" if sensor_on == 1 else "○"
                padding = (cell_width - 1) // 2
                top_sensor_line += " " * padding + symbol + " " * (cell_width - padding - 1)

        lines.append(top_state_line)
        lines.append(top_sensor_line)
        lines.append("")

        # Subsequent rows (3 states per row, starting from state 'width')
        # The 3 pillars should align under states: 0, (width-1)//2, and (width-1)
        pillar_positions = [0, (self.width - 1) // 2, self.width - 1]

        # Actual cell width in output (1 space + num_width digits + 2 spaces)
        actual_cell_width = num_width + 3

        state = self.width
        for depth_level in range(self.depth - 1):
            row_state_line = ""
            row_sensor_line = ""

            for col in range(3):
                if state >= self.size:
                    break

                # Add spacing to align this column under the correct position from top row
                if col == 0:
                    spacing = pillar_positions[0] * actual_cell_width
                else:
                    # Space from end of previous column to start of this column
                    spacing = (pillar_positions[col] - pillar_positions[col - 1] - 1) * actual_cell_width

                row_state_line += " " * spacing
                row_sensor_line += " " * spacing

                if state == goal_state:
                    row_state_line += f" {state:{num_width}}  "
                    padding = (cell_width - 1) // 2
                    row_sensor_line += " " * padding + "✓" + " " * (cell_width - padding)
                else:
                    row_state_line += f" {state:{num_width}}  "
                    sensor_on = model.get(f'ys{state}', 0)
                    symbol = "●" if sensor_on == 1 else "○"
                    padding = (cell_width - 1) // 2
                    row_sensor_line += " " * padding + symbol + " " * (cell_width - padding - 1)

                state += 1

            lines.append(row_state_line)
            lines.append(row_sensor_line)
            lines.append("")

        lines.append("Legend: ✓=goal, ●=sensor on, ○=sensor off")

        return "\n".join(lines)

    def draw_pop(self, model: dict, goal_state: int, budget: int, use_color: bool = True) -> str:
        """Draw maze world with observation classes marked."""
        lines = []
        lines.append(f"Maze World (width={self.width}, depth={self.depth}) (POP):")
        lines.append("")

        # Calculate width needed for state numbers
        max_state = self.size - 1
        num_width = len(str(max_state))
        cell_width = num_width + 3  # 1 leading space + num_width + 2 trailing spaces

        # Top row (states 0 to width-1)
        top_state_line = ""
        top_obs_line = ""
        for state in range(self.width):
            if state == goal_state:
                top_state_line += f" {state:{num_width}}  "
                padding = (cell_width - 1) // 2
                top_obs_line += " " * padding + "✓" + " " * (cell_width - padding)
            else:
                top_state_line += f" {state:{num_width}}  "
                # Find which observation class this state belongs to
                obs_class = 0
                for o in range(1, budget + 1):
                    if model.get(f'ys{state}o{o}', 0) == 1:
                        obs_class = o
                        break
                symbol = self._get_observation_emoji(obs_class, use_color)
                # Center the symbol in the cell (ANSI colors don't affect width)
                padding = (cell_width - 1) // 2
                top_obs_line += " " * padding + symbol + " " * (cell_width - padding)

        lines.append(top_state_line)
        lines.append(top_obs_line)
        lines.append("")

        # Subsequent rows (3 states per row, starting from state 'width')
        # The 3 pillars should align under states: 0, (width-1)//2, and (width-1)
        pillar_positions = [0, (self.width - 1) // 2, self.width - 1]

        state = self.width
        for depth_level in range(self.depth - 1):
            row_state_line = ""
            row_obs_line = ""

            for col in range(3):
                if state >= self.size:
                    break

                # Add spacing to align this column under the correct position from top row
                if col == 0:
                    spacing = pillar_positions[0] * cell_width
                else:
                    # Space from end of previous column to start of this column
                    spacing = (pillar_positions[col] - pillar_positions[col - 1] - 1) * cell_width

                row_state_line += " " * spacing
                row_obs_line += " " * spacing

                if state == goal_state:
                    row_state_line += f" {state:{num_width}}  "
                    padding = (cell_width - 1) // 2
                    row_obs_line += " " * padding + "✓" + " " * (cell_width - padding)
                else:
                    row_state_line += f" {state:{num_width}}  "
                    # Find which observation class this state belongs to
                    obs_class = 0
                    for o in range(1, budget + 1):
                        if model.get(f'ys{state}o{o}', 0) == 1:
                            obs_class = o
                            break
                    symbol = self._get_observation_emoji(obs_class, use_color)
                    # Center the symbol in the cell (ANSI colors don't affect width)
                    padding = (cell_width - 1) // 2
                    row_obs_line += " " * padding + symbol + " " * (cell_width - padding)

                state += 1

            lines.append(row_state_line)
            lines.append(row_obs_line)
            lines.append("")

        # Build legend
        legend = "Legend: ✓=goal"
        for o in range(1, budget + 1):
            legend += f", {self._get_observation_emoji(o, use_color)}=obs {o}"
        lines.append(legend)

        return "\n".join(lines)
