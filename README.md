# Key-caster

- A simple keyboard key press displayer for Linux. Based on keycastr for macOS.

## Setup

- Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

- Move to the project directory and run the following command.

```bash
sudo python .
```

## Notes

- Require root previleges to run. (For capturing key events)
- Stop the program by running `sudo kill $PID` which $PID is the process id of the running program.
- If this is the only Python program running, you can stop it by running `sudo killall python` or `sudo pkill python`.
