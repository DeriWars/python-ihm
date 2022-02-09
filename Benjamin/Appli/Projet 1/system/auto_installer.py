from pip._internal.utils.misc import get_installed_distributions

import os

def auto_install_package(needed_package):
    installed_packages = get_installed_distributions()
    installed_packages_name = [package.project_name.lower() for package in installed_packages]
    package_to_install = []

    for package in needed_package:
        if not installed_packages_name.__contains__(package.lower()):
            package_to_install.append(package)

    for pack in package_to_install:
        result = os.system("pip install " + pack)
        
        if result == 1:
            print("Echec de l'installation","Impossible d'installer le package " + pack + ". Sans ce package, le programme ne fonctionnera pas correctement.")
            os.system("pause")