class IntroScreen:
    def __init__(self, OS, version):
        self.OS = OS
        self.version = version
    def show_banner(self):
        print(f"""Copyright 2026 The Mountain Systems
        Welcome to TMS File Organizer for {self.OS} v{self.version}!
        Choose one of the following options to get started:

        1) Organize my images
        2) Organize my documents
        3) organize my downloads
        4) Organize my Desktop
        5) Organize everything

        Q) Quit
        """)
    def options(self, option):
        if option == '1':
            return '1'
        elif option == '2':
            return '2'
        elif option == '3':
            return '3'
        elif option == '4':
            return '4'
        elif option == '5':
            return '5'
        elif option == 'Q':
            return 'Q'
