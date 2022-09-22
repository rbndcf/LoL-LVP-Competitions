################################################################################
##     Programa para almacenar los resultados en las competiciones de la LVP  ##
##  y calcular cosas como winrate, kda, minions, partidas totales, etc.       ##
##     Este programa es meramente para aprender a programar en Python y no    ##
##  está relacionado con la propia LVP ni ninguna de sus competiciones. Si    ##
##  se quiere utilizar o modificar el programa, contactar primero conmigo por ##
##  Twitter -> @ruben_dcf.                                                    ##
##                                                                            ##
##  Rubén Del Castillo Fuentes                                                ##
################################################################################

import os

str_welcome =  ("================================================================\n"
                "     Bienvenido al programa para consultar las estadísticas de  \n"
                "  la LVP (Liga de Videojuegos Profesional) en su categoría de   \n"
                "  League of Legends.\n"
                "================================================================\n")

if __name__ == "__main__":
    os.system('cls')
    print(str_welcome)
