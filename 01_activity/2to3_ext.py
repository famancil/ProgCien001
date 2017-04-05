def pyth(line,cell):
    # We first retrieve the current IPython interpreter instance.
    ip = get_ipython()
    # We define the source and executable filenames.
    source_filename = 'example.py'
    # We write the code to the python file.
    with open(source_filename, 'w') as f:
	#Replace raw_input to input
        cell= cell.replace("raw_input","input")
	#Replace print to print()
        cell= cell.replace("print ","print(")
        cell= cell.replace(".\"",".\")")
        f.write(cell)
    #Show output by magic command "%run"
    ip.magic("%run ./example.py")

def load_ipython_extension(ipython):
       """This function is called when the extension is loaded.
       It accepts an IPython InteractiveShell instance.
       We can register the magic with the `register_magic_function`
       method of the shell instance."""
       ipython.register_magic_function(pyth, 'cell')
