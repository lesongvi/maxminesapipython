# MaxMinesAPIPython
Class Python để dễ dàng sử dụng HTTP API của MaxMines  
Để biết thêm chi tiết về HTTP API của MaxMines vui lòng truy cập [tài liệu MaxMines HTTP API](https://maxmines.com/documentation/http-api)

# Ví dụ (GET)
```py
from maxminesapipython.client import MaxMinesPython

secret_key = ""
client = MaxMinesPython(secret_key)

client.get("/stats/site")
```

# Ví dụ (POST)
```py
from maxminesapipython.client import MaxMinesPython


secret_key = ""
client = MaxMinesPython(secret_key)

client.post("/links/create", {"url": "https://example.com", "hashes": 1024})
```
## Góp ý
[get in touch](https://maxmines.com/contact)
