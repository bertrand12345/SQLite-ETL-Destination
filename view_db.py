import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("/workspaces/SQLite-ETL-Destination/keywords.db")

# Création d'un curseur pour exécuter des requêtes
cursor = conn.cursor()

# Récupérer toutes les tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Récupérer les données d'une table spécifique (remplacez 'keywords' par le nom de votre table)
cursor.execute("SELECT * FROM keywords;")
rows = cursor.fetchall()

# Afficher les données
for row in rows:
    print(row)

# Fermer la connexion
conn.close()
