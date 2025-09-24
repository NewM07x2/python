<!-- 起動 -->
uvicorn app.main:app --reload

<!-- GET実行コマンド -->
curl -X GET http://localhost:9999/

<!-- POST実行コマンド -->
curl -X POST -H "Content-Type: application/json" -d '{"title":"Sample Todo"}' http://localhost:9999/todo

