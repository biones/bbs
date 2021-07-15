docker-compose run web -d

# DBにデータを入れる 
cat dump.sql | docker exec -i bbs_db_1  psql -U postgres

# DBのバックアップの作成
docker exec  bbs_db_1 pg_dumpall -U postgres > dump.sql

