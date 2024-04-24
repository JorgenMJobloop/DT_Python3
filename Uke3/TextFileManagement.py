class TextFileManagement:
    # Constructor
    def __init__(self, filename):
        self.filename = filename

    # define the read_file method/function
    def read_file(self):
        # using the open() function to communicate with the system I/O stream
        with open(self.filename, "r") as file:
            content = file.read()
        return content
    
    # define the write_file method/function
    def write_file(self, data):
        with open(self.filename, "w") as file:
            # we use the write function from the open() function to access the data as a argument.
            file.write(data)

    # define the read_as_list method/function
    def read_as_list(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()
        return lines
    
    # define the write_as_list method/function
    def write_as_list(self, data_list):
        with open(self.filename, "a") as file:
            for data in data_list:
                file.write("\n" + data + "\n")

    # define the append_to_file method/function
    def append_to_file(self, new_data):
        with open(self.filename, "a") as file:
            file.write(new_data)
    
