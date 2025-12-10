import re
from collections import deque

from src.helpers.file_helper import read_file_as_list


class Machine:
    def __init__(
        self,
        buttons,
        target,
        state,
        buttons_pressed=0,
    ):
        self.buttons = buttons
        self.target = target
        self.state = state
        self.buttons_pressed = buttons_pressed

    def __repr__(self):
        return f"Machine: buttons pressed: {self.buttons_pressed}"

    def press_buttons(self, buttons):
        for btn in buttons:
            self.buttons_pressed += 1
            self.state = btn.toggle(self.state)


class Button:
    def __init__(self, toggles):
        self.toggles = toggles

    def __repr__(self):
        return f"Button: {self.toggles}"

    def toggle(self, val):
        new_val = []
        for i, c in enumerate(list(val)):
            if i in self.toggles:
                new_val.append("." if c == "#" else "#")
            else:
                new_val.append(c)
        return "".join(new_val)


def get_min_button_presses(machine):
    machine_options = deque()
    machine_options.append(machine)
    visited = set()
    visited.add(machine.state)

    while machine_options:
        m = machine_options.popleft()
        if m.state == m.target:
            return m.buttons_pressed

        for btn in m.buttons:
            new_m = Machine(
                m.buttons,
                m.target,
                m.state,
                m.buttons_pressed,
            )
            new_m.press_buttons([btn])

            if new_m.state not in visited:
                visited.add(new_m.state)
                machine_options.append(new_m)

    return -1


def solve():
    lines = read_file_as_list("day10.txt")
    line_pattern = r"\[(.*)] (\(.*\)) ({.*})"

    machines = []
    for line in lines:
        m = re.match(line_pattern, line)
        lights_string = m.group(1)
        buttons_string = m.group(2)
        buttons = []
        for button in buttons_string.split(" "):
            buttons.append(
                Button(list(map(int, button.lstrip("(").rstrip(")").split(","))))
            )
        machines.append(Machine(buttons, lights_string, "." * len(lights_string)))

    result = 0
    for machine in machines:
        result += get_min_button_presses(machine)

    print(f"result: {result}")
    return result


if __name__ == "__main__":
    solve()
