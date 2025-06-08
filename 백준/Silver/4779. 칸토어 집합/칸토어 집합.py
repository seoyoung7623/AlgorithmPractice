import sys

def pop_out_middle(dash):
    if len(dash) < 3:
        return dash
    third = len(dash) // 3
    return (
        pop_out_middle(dash[:third])
        + " " * third
        + pop_out_middle(dash[2*third:])
    )
        
for line in sys.stdin:
    N = int(line.strip())
    dash = "-" * (3 ** N)
    print(pop_out_middle(dash))