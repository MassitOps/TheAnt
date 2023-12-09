from cx_Freeze import setup, Executable
setup(
    name = "The Ant",
    version = "0.1",
    description = "Description",
    executables = [Executable("goTk.py")],
)
# python setup.py build
