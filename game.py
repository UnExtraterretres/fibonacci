class Game:

    def __init__(self, file_path="fibonacci.txt", condition="True"):
        # to load arguments
        self.file_path = file_path
        self.condition = condition

        # boolean states of the game
        self.states = {
            "running": True
        }

        # to load the series
        try:
            self.fibonacci_series = open(self.file_path, "r").read().split(",")
        except FileNotFoundError:
            self.fibonacci_series = [0, 1]
            open(self.file_path, "w").write("0,1")

        # open the .txt file with mode "a"
        self.txt_file = open(self.file_path, "a")

    def handling_events(self):
        pass

    def update(self):

        if eval(self.condition):
            self.fibonacci_series.append(int(self.fibonacci_series[-1])+int(self.fibonacci_series[-2]))
            self.txt_file.write(f",{str(self.fibonacci_series[-1])}")

    def display(self):
        pass

    def run(self):
        # game LOOP
        while self.states["running"]:
            # check events
            self.handling_events()
            # the logic of the game
            self.update()
            # displays
            self.display()
