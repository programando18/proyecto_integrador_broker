#!/bin/bash

# Configuración inicial
BRANCH_PREFIX="development_"
MAIN_BRANCH="main"
LOG_FILE="merge_errors.log"

# Función para loguear errores
log_error() {
    echo "[ERROR] $1" | tee -a $LOG_FILE
}

# Limpiar archivo de log
> $LOG_FILE

# Asegurarse de estar en la rama principal
echo "Cambiando a la rama principal $MAIN_BRANCH..."
git checkout $MAIN_BRANCH
if [ $? -ne 0 ]; then
    log_error "Error al cambiar a la rama principal $MAIN_BRANCH."
    exit 1
fi

# Hacer pull de los últimos cambios de la rama principal
echo "Haciendo pull de la rama principal $MAIN_BRANCH..."
git pull origin $MAIN_BRANCH
if [ $? -ne 0 ]; then
    log_error "Error al hacer pull de la rama $MAIN_BRANCH."
    exit 1
fi

# Obtener todas las ramas que empiezan con development_*
branches=$(git branch --list "${BRANCH_PREFIX}*")
if [ -z "$branches" ]; then
    echo "No se encontraron ramas que comiencen con '${BRANCH_PREFIX}'."
    exit 1
fi

# Loop por cada rama
for branch in $branches; do
    echo "Cambiando a la rama $branch..."
    git checkout $branch
    if [ $? -ne 0 ]; then
        log_error "Error al cambiar a la rama $branch."
        continue
    fi

    echo "Haciendo pull de los últimos cambios de $branch..."
    git pull origin $branch
    if [ $? -ne 0 ]; then
        log_error "Error al hacer pull de la rama $branch."
        continue
    fi

    # Merge de las demás ramas
    for other_branch in $branches; do
        if [ "$branch" != "$other_branch" ]; then
            echo "Haciendo merge de $other_branch en $branch..."
            git merge $other_branch --no-ff
            if [ $? -ne 0 ]; then
                log_error "Error al hacer merge de $other_branch en $branch."
                git merge --abort  # Abortamos el merge si hay conflictos
                continue
            fi
        fi
    done

    # Push de los cambios después de mergear
    echo "Haciendo push de los cambios en $branch..."
    git push origin $branch
    if [ $? -ne 0 ]; then
        log_error "Error al hacer push de la rama $branch."
        continue
    fi
done

# Regresar a la rama principal
echo "Volviendo a la rama principal $MAIN_BRANCH..."
git checkout $MAIN_BRANCH
if [ $? -ne 0 ]; then
    log_error "Error al regresar a la rama principal $MAIN_BRANCH."
    exit 1
fi

echo "Script terminado. Revisa $LOG_FILE para errores, si los hubiera."
