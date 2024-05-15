from gui import mostrar_programas_gui
from programs import listar_programas_instalados


if __name__ == "__main__":
    programas = listar_programas_instalados()
    mostrar_programas_gui(programas)
