from google.cloud import bigquery

# Création d'un client BigQuery
client = bigquery.Client()

# TODO : Ajouter nom de la table à compléter
table_id = "your-project.your_dataset.your_table_name"

# TODO : Ajouter URL du fichier CSV à implémenter
file_uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"


job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING")
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)

load_job = client.load_table_from_uri(
    file_uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))