import platform
from linux import linux_f_organizer
from macos import macos_f_organizer
from windows import windows_f_organizer

if __name__ == "__main__":
    system = platform.system()
    if system == "Windows":
        windows_f_organizer.organize()
    elif system == "Darwin":
        macos_f_organizer.organize()
    else:
        linux_f_organizer.main()
