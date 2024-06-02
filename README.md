## 카카오맵 API 활용한 지도에 Marker 표시 & 거리 측정
![image](https://private-user-images.githubusercontent.com/26128046/335840528-db106e5d-1f1a-43bb-8066-150706e4afe1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTczMDM3OTksIm5iZiI6MTcxNzMwMzQ5OSwicGF0aCI6Ii8yNjEyODA0Ni8zMzU4NDA1MjgtZGIxMDZlNWQtMWYxYS00M2JiLTgwNjYtMTUwNzA2ZTRhZmUxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjAyVDA0NDQ1OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM2MzlhNWM1ZmE2OTg0ZWU3MjcxNDE5YTQwOTEzYTliNjhjN2YxZDljMGJjNGYzYTI3MjcwZjQ2MmE3ZWY1NzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ALoKu7z5xWdSjsqD5qpp3_o3H-A6x0SDailaU1f-uXU)

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

