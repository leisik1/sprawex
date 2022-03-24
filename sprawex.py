from PIL import ImageGrab
from pynput import keyboard

sprawko_name = "LABX_test.txt"
section_number = 1
screen_number = 1


def save_as():
    global screen_number
    name = "ZAD{}_{}".format(section_number, screen_number)
    im = ImageGrab.grabclipboard()
    im.save('{}.png'.format(name), 'PNG')
    write_in_latex(name)
    screen_number += 1


def write_in_latex(name):
    file = open(sprawko_name, 'a')
    text = ["\n", "\\begin{figure}[H] \n", "\t \\centering \n", "\t \\includegraphics[scale=0.7]",
            "\t \\caption{} \n", "\t \\label{fig:my_label} \n", "\end{figure} \n"]
    text[3] += "{" + name + "} \n"
    file.writelines(text)
    file.close()


save_as()
