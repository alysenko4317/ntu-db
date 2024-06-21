docker run ^
  --name=postgres ^
  --rm ^
  --volume="%cd%/schema.sql":/docker-entrypoint-initdb.d/schema.sql ^
  --volume="%cd%":/repo ^
  --env=PSQLRC=/repo/.psqlrc ^
  --env=POSTGRES_PASSWORD=foo ^
  postgres:latest -c log_statement=all
