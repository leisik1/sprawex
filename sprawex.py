from PIL import ImageGrab

sprawko_name = "LABX_test.txt"


def save_as(name):
    im = ImageGrab.grabclipboard()
    im.save('{}.png'.format(name), 'PNG')
    # write_in_latex(name)


def write_in_latex(name):
    file = open(sprawko_name, 'a')
    text = ["\n", "\\begin{figure}[H] \n", "\t \\centering \n", "\t \\includegraphics[scale=0.7]",
            "\t \\caption{} \n", "\t \\label{fig:my_label} \n", "\end{figure} \n"]
    text[3] += "{" + name + "} \n"
    file.writelines(text)
    file.close()


# save_as("pierwsze_zdj")
write_in_latex("pierwsze.png")
