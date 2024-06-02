## 카카오맵 API 활용한 지도에 Marker 표시 & 거리 측정
![image](https://user-images.githubusercontent.com/26128046/335840528-db106e5d-1f1a-43bb-8066-150706e4afe1.png)

### install
```Bash
pip install -r requirements.txt
```

### 사전 설치
* Apache 서버 설치 후 `conf/httpd.conf` 서버 root 변경.

### 실행
1. `xlsx` 파일을 `csv` 파일로 변환 후 `source root` 로 이동
2. `python generate_map_html.py` 로 index.html 만들기
3. `localhost:80` 으로 접속


### TODO
* Marker 위에 '업소명' (title) 표시 안됨.
  * 아마 marker 아이콘 문제인듯.

