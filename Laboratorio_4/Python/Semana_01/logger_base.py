import logging as log
import os

log_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(log_dir, "capa_datos.log")


log.basicConfig(level=log.DEBUG,
                format="%(asctime)s:%(levelname)s [%(filename)s: Linea:%(lineno)s] %(message)s",
                datefmt="Hora: %I:%M:%S %p",
                handlers=[
                    log.FileHandler(log_file_path),
                    log.StreamHandler()
                ])


if __name__ == "__main__":    
    log.debug(" Mensaje a nivel debug")
    log.info(" Mensaje a nivel info")
    log.warning(" Mensaje a nivel warning")
    log.error(" Mensaje a nivel error")
    log.critical(" Mensaje a nivel critical")
