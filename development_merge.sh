#!/bin/bash

# Configuración inicial
BRANCH_PREFIX="development_"
MAIN_BRANCH="main"  # Si tienes una rama principal o master, si no cámbiala.

# Asegurarse de estar en la rama principal (por si acaso)
git checkout $MAIN_BRANCH

# Obtener todas las ramas que empiezan con development_*
branches=$(git branch --list "${BRANCH_PREFIX}*")

# Verificar si hay ramas
if [ -z "$branches" ]; then
    echo "No se encontraron ramas que comiencen con '${BRANCH_PREFIX}'."
    exit 1
fi

# Hacer pull para estar seguros de tener los últimos cambios en el repo local
git pull origin $MAIN_BRANCH

# Loop por cada rama
for branch in $branches; do
    echo "Haciendo checkout a $branch"
    git checkout $branch
    
    echo "Haciendo pull de los últimos cambios"
    git pull origin $branch
    
    # Mergear el resto de las ramas en esta
    for other_branch in $branches; do
        if [ "$branch" != "$other_branch" ]; then
            echo "Haciendo merge de $other_branch en $branch"
            git merge $other_branch --no-ff
        fi
    done
    
    # Hacer push de los cambios después de mergear
    echo "Haciendo push de los cambios en $branch"
    git push origin $branch
done

# Regresar a la rama principal
git checkout $MAIN_BRANCH

echo "Todas las ramas fueron actualizadas."
