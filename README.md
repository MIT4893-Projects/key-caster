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

## Screenshots
![image](https://github.com/MIT4893-Projects/key-caster/assets/116936560/654498a7-a2ee-4c7e-8e2e-521db0449a4a)
![image](https://github.com/MIT4893-Projects/key-caster/assets/116936560/f7438f85-feca-4941-bc18-47f0a1f4802a)

