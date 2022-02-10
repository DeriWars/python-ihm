def auto_install_package(needed_package):
    from pip._internal.utils.misc import get_installed_distributions
    import os
    
    installed_packages = get_installed_distributions()
    installed_packages_name = [package.project_name.lower() for package in installed_packages]
    package_to_install = []

    for package in needed_package:
        if not installed_packages_name.__contains__(package.lower()):
            package_to_install.append(package)

    result = str(input(f"Vous avez besoin de {len(package_to_install)} paquets à installer.\nVoulez-vous les installer automatiquement ? (y/n) "))

    if result.lower() == 'y':
        for pack in package_to_install:
            result = os.system("pip install " + pack)
            
            if result == 1:
                print("Echec de l'installation","Impossible d'installer le package " + pack  + ". Sans ce package, le programme ne fonctionnera pas correctement.")
                input("Appuyez sur une touche pour continuer.")
    else:
        print("Vous avez choisi de ne pas installer les paquets manquants.\nVous pouvez les installer manuellement en suivant les instructions suivantes :\n\n1. Ouvrez un terminal\n2. Entrez la commande suivante :\npip install " + " ".join(package_to_install))