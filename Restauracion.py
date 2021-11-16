from os import system

system('psql -d PruebasLibreria -p 5433 -h localhost -U postgres <  "respaldo.sql"')