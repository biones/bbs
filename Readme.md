1. コンテナ起動 
docker-compose up &

2. DBにデータを入れる  
cat dump.sql | docker exec -i bbs_db_1  psql -U postgres


# バックアップの作成
docker exec  bbs_db_1 pg_dumpall -U postgres > dump.sql

