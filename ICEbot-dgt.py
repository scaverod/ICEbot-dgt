import argparse

from selenium import webdriver

PATH_CHROMEDRIVER = r"C:\Users\Sergio Cavero\Downloads\chromedriver"
OPTIONS = ['headless']

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path-chromedriver", help="Path de la localización de chromedriver", type=str,
                    default=PATH_CHROMEDRIVER)
parser.add_argument("-c", "--carretera",
                    help="Indica la carretera a buscar incidencias, por defecto se buscan en todas las carreteras",
                    default="ALL",
                    type=str)


def get_incidencias(driver, carretera):
    driver.get(
        "http://infocar.dgt.es/etraffic/Incidencias?ca=&provIci=&caracter=acontecimiento&accion_consultar=Consultar"
        "&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA"
        "=IncidenciasMETEOROLOGICA&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasOTROS=IncidenciasOTROS"
        "&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES&ordenacion=fechahora_ini-DESC")
    atags = driver.find_elements_by_tag_name('tr')
    incidents = []
    resul = []
    for fila in atags:
        incidents.append(fila.text)
    incidents.pop(0)
    for incident in incidents:
        if carretera == "ALL":
            resul.append(incident.splitlines())
        elif "\n" + carretera + "\n" in incident:
            resul.append(incident.splitlines())
    return resul


def get_driver(path, options_arg):
    options = webdriver.ChromeOptions()
    for option in options_arg:
        options.add_argument(option)
    try:
        driver = webdriver.Chrome(executable_path=path, options=options)
    except Exception as e:
        print("Invalid driver path. \nDownload driver here: "
              "https://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.20/")
        raise e
    print("Driver path is correct... starting scrapping...")
    return driver


if __name__ == "__main__":
    driver = None
    try:
        args = parser.parse_args()
        driver = get_driver(args.path_chromedriver, OPTIONS)
        if args.carretera.upper() != "ALL":
            print("Se van a buscar incidentes para la carretera ", args.carretera.upper())
        else:
            print("Se van a buscar todos los incidentes de las carreteras españolas")
        data = get_incidencias(driver, args.carretera.upper())
        if data is not None:
            print("Se han encontrado " + str(len(data)) + " incidencias.")
            for incident in data:
                print(incident)
        else:
            print("No se han encontrado incidencias")
    except Exception:
        print("[!] An error ocurred!")
    finally:
        if driver is not None:
            driver.close()
