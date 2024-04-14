import numpy as np

def tirage_loi_poisson(lambda_parameter):
    # Tirage d'échantillons selon la loi de Poisson
    sample = np.random.poisson(lambda_parameter)
    gain = sample

    # Remplacer la valeur 0 par -1 si c'est le cas
    if sample == 0:
        gain = -1

    return sample, gain
    
def print_place(name, gain):
    if gain == - 1:
        print(name, " perd une place au classement.")
    elif gain == 1:
        print(name, "gagne une place au classement.")
    else:
        print(name, " gagne", gain, "places au classement.")



# Paramètres de la loi de Poisson
lambda_parameter = 0.6  # paramètre lambda

# Premier tirage
sample1, gain1 = tirage_loi_poisson(lambda_parameter)
print("Premier tirage pour selon la loi de Poisson avec lambda =", lambda_parameter, ": ", sample1)
print_place("Sana", gain1) 
# Deuxième tirage
sample2, gain2 = tirage_loi_poisson(lambda_parameter)
print("Deuxième tirage selon la loi de Poisson avec lambda =", lambda_parameter, ": ", sample2)
print_place("Bilal", gain2) 