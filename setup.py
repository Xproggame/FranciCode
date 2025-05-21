from cx_Freeze import setup, Executable

setup(
    name = "FranciCode",
    version = "1.0.0",
    description = "Un language de programation par ligne de code en français",
    executables = [Executable("main.py")],
)