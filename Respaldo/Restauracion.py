from os import system

system('psql -d ReplicacionLibreria -p 5433 -h localhost -U postgres <  "respaldo.sql"')