import csv
import csv
from jinja2 import Environment, FileSystemLoader
import os
from pyproj import Proj, transform

# CSV 파일 경로
csv_file_list = [x for x in os.listdir('.') if x.endswith('.csv')]
csv_file_path = csv_file_list[0]

# 중부원점TM 좌표계 (EPSG:5174)에서 WGS84 좌표계 (EPSG:4326)로 변환 설정
proj_tm_mid = Proj(init='epsg:5174')
proj_wgs84 = Proj(init='epsg:4326')

# CSV 파일에서 데이터 추출
positions = []
center_lat = None
center_lng = None

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        # 좌표 변환
        x_str = row['좌표정보(X)'].strip()
        y_str = row['좌표정보(Y)'].strip()
        if not x_str or not y_str:
            continue

        try:
            x = float(x_str)
            y = float(y_str)
        except ValueError:
            continue

        # 중부원점TM 좌표계를 위도와 경도로 변환
        lng, lat = transform(proj_tm_mid, proj_wgs84, x, y)
        position = {
            'title': row['사업장명'],
            'latlng': {
                'lat': lat,
                'lng': lng
            }
        }
        positions.append(position)

        # 첫 번째 행의 좌표를 중심 좌표로 설정
        if center_lat is None and center_lng is None:
            center_lat = lat
            center_lng = lng
        #
        # if i == 5:
        #     break

# Jinja2 환경 설정
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# HTML 파일 렌더링
output_from_parsed_template = template.render(positions=positions, center_lat=center_lat, center_lng=center_lng)

# HTML 파일로 저장
with open("index.html", "w", encoding='utf-8') as fh:
    fh.write(output_from_parsed_template)
