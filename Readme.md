1. コンテナ起動  
docker-compose up &

2. DBにデータを入れる  
cat dump.sql | docker exec -i bbs_db_1  psql -U postgres

3. dupplicateが出たらdump.sqlでrowIDを調整する
SELECT pg_catalog.setval('public.posts_id_seq', 10000, true);

# バックアップの作成
docker exec  bbs_db_1 pg_dumpall -U postgres > dump.sql

