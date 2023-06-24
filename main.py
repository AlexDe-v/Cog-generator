import sys
import os
try:
    import inquirer
except ImportError:
    print('You need to have inquirer installed to run this. \nUse: pip install inquirer')
    exit()

def print_with_color(txt: str, color: str):
    class bcolors:
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        ORANGE = '\033[93m'
    if not hasattr(bcolors, color.upper()):
        print(txt)
        return
    print(getattr(bcolors, color.upper()) + txt + '\033[0m')

def main():
    cogname = None
    if len(sys.argv) == 2:
        cogname = sys.argv[1]

    if cogname == None:
        print_with_color("Enter a name for the cog", "blue")
        cogname = input('> ')

    choices = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(script_dir, "Templates")
    for filename in os.listdir(f'{script_dir}'):
        if os.path.isfile(os.path.join(script_dir, filename)):
            choices.append(filename)
    questions = [
    inquirer.List(
        "Template",
        message="What template would you like to load?",
        choices=choices,
    ),
    ]
    answers = inquirer.prompt(questions)
    template = answers['Template']
    with open(f'cogs/{cogname}.py', 'w') as f:
        with open(f'{script_dir}/{template}', 'r') as f2:
            x = f2.read()
        f.write(x)
    print_with_color("Cog created!", 'green')

    
if not os.path.exists('./cogs'):
    print_with_color("You don't have a cogs directory. Create one or check if you're in the right directory!", "orange")
else:
    main()