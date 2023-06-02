import pandas as pd

df_donnes_regions = pd.read_csv('/Users/jeremy/Documents/1. Projets/Project DataElec/Datalake/donnees_regions.csv', usecols=['CODREG','REG','PTOT'], sep=';')
df_donnes_departements = pd.read_csv('/Users/jeremy/Documents/1. Projets/Project DataElec/Datalake/donnees_departements.csv', usecols=['CODREG','CODDEP','DEP','PTOT'], sep=';')
df_donnes_communes = pd.read_csv('/Users/jeremy/Documents/1. Projets/Project DataElec/Datalake/donnees_communes.csv', usecols=['CODREG','CODDEP','Code commune','COM','PTOT'], sep=';')
df_regions_zones_scolaires = pd.read_csv('/Users/jeremy/Documents/1. Projets/Project DataElec/Datalake/regions-zones-scolaires.csv', sep=';')

df_calendrier_vacances = pd.read_excel('./datalake/calendrier-vacances.xlsx', "Feuil1", index_col=None, na_values=["NA"])
df_calendrier_vacances.loc[df_calendrier_vacances.Jour == "Dimanche", "Nouvelle colonne"] = "Week-end"
df_calendrier_vacances.to_csv('./warehouse_csv/calendrier_vacances_scolaires')