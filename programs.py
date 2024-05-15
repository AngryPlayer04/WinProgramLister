import winreg

def listar_programas_instalados():
    programas = []
    try:
        chave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
        i = 0
        while True:
            sub_chave = winreg.EnumKey(chave, i)
            programa = {}
            try:
                info_chave = winreg.OpenKey(chave, sub_chave)
                nome = winreg.QueryValueEx(info_chave, "DisplayName")[0]
                versao = winreg.QueryValueEx(info_chave, "DisplayVersion")[0]
                programa['nome'] = nome
                programa['versao'] = versao
                programas.append(programa)
            except OSError:
                pass
            finally:
                info_chave.Close()
            i += 1
    except WindowsError:
        pass
    return programas
