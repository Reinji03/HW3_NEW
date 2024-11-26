'''streamlit run HW3'''

import streamlit as st

st.title('🔎시군구별 합계출산율 지도시각화하기')

st.write('#### 1. GeoPandas에서 지리정보 생성하기')
st.markdown(
  '''
  - GeoJSON 파일로 저장하기
  '''
  )

code="""
import geopandas as gpd

# geoDataFrame 형태로 불러옴
gdf_korea_sigungu = gpd.read_file('../slt/N3A_G0100000.json')
gdf_korea_sigungu

# GeoJSON 파일로 저장하기
gdf_korea_sigungu.to_file('../slt/N3A_G0100000.json', driver='GeoJSON')

# 저장된 GeoJSON 파일 불러오기
import json # json 라이브러리 불러오기
with open('../slt/N3A_G0100000.json', encoding='UTF-8') as f: #파일열기
    data = json.load(f) # 파일 읽기

# 데이터 출력하기(800자까지만 출력하기)
print(json.dumps(data, indent=4, ensure_ascii=False)[0:800])
"""
st.code(code, language="python")

import geopandas as gpd

# geoDataFrame 형태로 불러옴
gdf_korea_sigungu = gpd.read_file('../slt/N3A_G0100000.json')
gdf_korea_sigungu

# GeoJSON 파일로 저장하기
gdf_korea_sigungu.to_file('../slt/N3A_G0100000.json', driver='GeoJSON')

# 저장된 GeoJSON 파일 불러오기
import json # json 라이브러리 불러오기
with open('../slt/N3A_G0100000.json', encoding='UTF-8') as f: #파일열기
    data = json.load(f) # 파일 읽기

# 데이터 출력하기(800자까지만 출력하기)
print(json.dumps(data, indent=4, ensure_ascii=False)[0:800])

st.markdown(
  '''
  - 지도 시각화하기
  '''
  )
code="""
gdf_korea_sigungu.plot(figsize=(10,6)) # 데이터 plot하기
"""
st.code(code, language="python")

st.image("대한민국 시군구 지도.png", caption="대한민국 시군구 지도", use_column_width=True)

st.write('#### 2. 시군구열 전처리하기')

st.markdown(
  '''
  - 시군구별 합계출산율 데이터셋 전처리하기
  '''
  )

code="""
import pandas as pd # pandas 라이브러리 불러오기
# 시군구별(행정구역별) 합계출산율 불러오기
df_korea_birth = pd.read_csv('../slt/연령별_출산율_및_합계출산율_행정구역별.csv', encoding='euc-kr', header=2)
df_korea_birth.head() # 데이터 출력하기
"""
st.code(code, language="python")

import pandas as pd # pandas 라이브러리 불러오기
# 시군구별(행정구역별) 합계출산율 불러오기
df_korea_birth = pd.read_csv('../slt/연령별_출산율_및_합계출산율_행정구역별.csv', encoding='euc-kr', header=2)
df_korea_birth.head() # 데이터 출력하기

code="""
# 필요한 열만 추출
df_korea_birth=df_korea_birth[['전국','0.721']]

# 새로운 컬럼명 지정
columns = ['시군구', '합계출산율']

df_korea_birth
"""
st.code(code, language="python")

# 필요한 열만 추출
df_korea_birth=df_korea_birth[['전국','0.721']]

# 새로운 컬럼명 지정
columns = ['시군구', '합계출산율']

df_korea_birth

st.markdown(
  '''
  - 지도 데이터셋에 시군구열 추가하기
  '''
  )

code="""
# 지도 데이터셋 불러오기
import geopandas as gpd
gdf_korea_sigungu=gpd.read_file('../slt/N3A_G0100000.json')
gdf_korea_sigungu.head()

# 시군구열 추가하기
gdf_korea_sigungu['시군구']=gdf_korea_sigungu['NAME']
gdf_korea_sigungu
"""
st.code(code, language="python")

# 지도 데이터셋 불러오기
import geopandas as gpd
gdf_korea_sigungu=gpd.read_file('../slt/N3A_G0100000.json')
gdf_korea_sigungu.head()

# 시군구열 추가하기
gdf_korea_sigungu['시군구']=gdf_korea_sigungu['NAME']
gdf_korea_sigungu

st.markdown(
  '''
  - 시군구 데이터 확인하기
  '''
  )

code="""
print(df_korea_birth['시군구'].unique())
"""
st.code(code, language="python")

st.markdown(
  '''
  ['서울특별시' '종로구' '중구' '용산구' '성동구' '광진구' '동대문구' '중랑구' '성북구' '강북구' '도봉구' '노원구'
 '은평구' '서대문구' '마포구' '양천구' '강서구' '구로구' '금천구' '영등포구' '동작구' '관악구' '서초구' '강남구'
 '송파구' '강동구' '부산광역시' '부산-중구' '서구' '동구' '영도구' '부산진구' '동래구' '남구' '북구' '해운대구'
 '사하구' '금정구' '부산-강서구' '연제구' '수영구' '사상구' '기장군' '대구광역시' '대구-중구' '대구-동구'
 '대구-서구' '대구-남구' '대구-북구' '수성구' '달서구' '달성군' '군위군' '인천광역시' '인천-중구' '인천-동구'
 '연수구' '남동구' '부평구' '계양구' '인천-서구' '강화군' '옹진군' '미추홀구' '광주광역시' '광주-동구'
 '광주-서구' '광주-남구' '광주-북구' '광산구' '대전광역시' '대전-동구' '대전-중구' '대전-서구' '유성구' '대덕구'
 '울산광역시' '울산-중구' '울산-남구' '울산-동구' '울산-북구' '울주군' '세종특별자치시' '세종시' '경기도'
 ..이하 생략
  '''
  )

code="""
print(gdf_korea_sigungu['시군구'].unique())
"""
st.code(code, language="python")

st.markdown(
  '''
  ['가평군' '강남구' '강동구' '강릉시' '강북구' '강서구' '강진군' '강화군' '거제시' '거창군' '경산시' '경주시'
 '계룡시' '계양구' '고령군' '고성군' '고양시' '고창군' '고흥군' '곡성군' '공주시' '과천시' '관악구' '광명시'
 '광산구' '광양시' '광주시' '광진구' '괴산군' '구례군' '구로구' '구리시' '구미시' '군산시' '군위군' '군포시'
 '권선구' '금산군' '금정구' '금천구' '기장군' '기흥구' '김제시' '김천시' '김포시' '김해시' '나주시' '남구'
 '남동구' '남양주시' '남원시' '남해군' '노원구' '논산시' '단양군' '단원구' '달서구' '달성군' '담양군' '당진시'
 '대덕구' '덕양구' '덕진구' '도봉구' '동구' '동남구' '동대문구' '동두천시' '동래구' '동안구' '동작구' '동해시'
 '마산합포구' '마산회원구' '마포구' '만안구' '목포시' '무안군' '무주군' '문경시' '미추홀구' '밀양시' '보령시'
 '보성군' '보은군' '봉화군' '부산진구' '부안군' '부여군' '부천시' '부평구' '북구' '분당구' '사상구' '사천시'
 '사하구' '산청군' '삼척시' '상당구' '상록구' '상주시' '서구'
 ..이하 생략
  '''
  )

code="""
# '중구'의 개수 확인
중구_개수 = (gdf_korea_sigungu['시군구'] == '중구').sum()
print(f"'중구'의 개수: {중구_개수}")
"""
st.code(code, language="python")

st.markdown(
  '''
  '중구'의 개수: 6
  '''
  )

st.markdown(
  '''
  ⇨ 시군구별 합계출산율 데이터셋에는 대구-중구, 대구-남구 등으로 표시되었지만 지도 데이터셋에는 중구, 남구로만 표시되어 이후 이를 전처리하였음
  '''
  )

st.markdown(
  '''
  - 시군구열 전처리하기
  '''
  )

code="""
# 하이픈('-')이 포함된 데이터 필터링
df_hyphen = df_korea_birth[df_korea_birth['시군구'].str.contains('-', na=False)]
print(df_hyphen)
"""
st.code(code, language="python")

st.markdown(
  '''
  시군구  합계출산율
27    부산-중구  0.320
38   부산-강서구  0.987
44    대구-중구  0.824
45    대구-동구  0.727
46    대구-서구  0.474
47    대구-남구  0.563
48    대구-북구  0.698
54    인천-중구  0.764
55    인천-동구  0.775
60    인천-서구  0.820
65    광주-동구  0.775
66    광주-서구  0.588
67    광주-남구  0.694
68    광주-북구  0.708
71    대전-동구  0.825
72    대전-중구  0.645
73    대전-서구  0.723
77    울산-중구  0.655
78    울산-남구  0.731
79    울산-동구  0.790
80    울산-북구  0.930
150  강원-고성군  0.870
228   포항-남구  0.814
229   포항-북구  0.875
  '''
  )

st.markdown(
  '''
  ⇨ 하이픈이 있는 시군구에 해당하는 코드를 직접 찾아서 매칭함
  '''
  )

code="""
import pandas as pd

# 변경할 BJCD 값과 대응되는 NAME 값 정의
bcd_to_name = {
    "2611000000": "부산-중구", "2644000000": "부산-강서구",
    "2711000000": "대구-중구", "2714000000": "대구-동구", "2717000000": "대구-서구",
    "2720000000": "대구-남구", "2723000000": "대구-북구",
    "2811000000": "인천-중구", "2814000000": "인천-동구", "2826000000": "인천-서구",
    "2911000000": "광주-동구", "2914000000": "광주-서구", "2915500000": "광주-남구", "2917000000": "광주-북구",
    "3011000000": "대전-동구", "3014000000": "대전-중구", "3017000000": "대전-서구",
    "3111000000": "울산-중구", "3114000000": "울산-남구", "3117000000": "울산-동구", "3120000000": "울산-북구",
    "4282000000": "강원-고성군"
}

gdf_korea_sigungu = gdf_korea_sigungu.copy()
gdf_korea_sigungu['시군구'] = gdf_korea_sigungu['BJCD'].map(bcd_to_name).fillna(gdf_korea_sigungu['시군구'])
"""
st.code(code, language="python")

code="""
print(gdf_korea_sigungu['시군구'].unique())
"""
st.code(code, language="python")

st.markdown(
  '''
  ['가평군' '강남구' '강동구' '강릉시' '강북구' '강서구' '부산-강서구' '강진군' '강화군' '거제시' '거창군'
 '경산시' '경주시' '계룡시' '계양구' '고령군' '강원-고성군' '고성군' '고양시' '고창군' '고흥군' '곡성군'
 '공주시' '과천시' '관악구' '광명시' '광산구' '광양시' '광주시' '광진구' '괴산군' '구례군' '구로구' '구리시'
 '구미시' '군산시' '군위군' '군포시' '권선구' '금산군' '금정구' '금천구' '기장군' '기흥구' '김제시' '김천시'
 '김포시' '김해시' '나주시' '남구' '대구-남구' '광주-남구' '울산-남구' '남동구' '남양주시' '남원시' '남해군'
 '노원구' '논산시' '단양군' '단원구' '달서구' '달성군' '담양군' '당진시' '대덕구' '덕양구' '덕진구' '도봉구'
 '동구' '대구-동구' '인천-동구' '광주-동구' '대전-동구' '울산-동구' '동남구' '동대문구' '동두천시' '동래구'
 ..이하 생략
  '''
  )

code="""
# '중구'의 개수 확인
중구_개수 = (gdf_korea_sigungu['시군구'] == '중구').sum()
print(f"'중구'의 개수: {중구_개수}")
"""
st.code(code, language="python")

st.markdown(
  '''
  '중구'의 개수: 1
  '''
  )

st.markdown(
  '''
  ⇨ 서울특별시 중구만 '중구'로 표시되고 나머지는 '시도명-중구' 이런식으로 표시됨
  '''
  )

code="""
print(df_korea_birth['시군구'].unique())
"""
st.code(code, language="python")

st.markdown(
  '''
  ['서울특별시' '종로구' '중구' '용산구' '성동구' '광진구' '동대문구' '중랑구' '성북구' '강북구' '도봉구' '노원구'
 '은평구' '서대문구' '마포구' '양천구' '강서구' '구로구' '금천구' '영등포구' '동작구' '관악구' '서초구' '강남구'
 '송파구' '강동구' '부산광역시' '부산-중구' '서구' '동구' '영도구' '부산진구' '동래구' '남구' '북구' '해운대구'
 '사하구' '금정구' '부산-강서구' '연제구' '수영구' '사상구' '기장군' '대구광역시' '대구-중구' '대구-동구'
 '대구-서구' '대구-남구' '대구-북구' '수성구' '달서구' '달성군' '군위군' '인천광역시' '인천-중구' '인천-동구'
 '연수구' '남동구' '부평구' '계양구' '인천-서구' '강화군' '옹진군' '미추홀구' '광주광역시' '광주-동구'
 ..이하 생략
  '''
  )

st.markdown(
  '''
  ⇨ 시도명이 포함되어있는걸 알 수 있음, 시도명인 행 삭제
  '''
  )

code="""
# 삭제할 시군구 목록 정의
remove_sido = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
    '경기도', '강원특별자치도', '충청북도', '충청남도', '전라북도', '전라남도',
    '경상북도', '경상남도', '제주특별자치도'
]

# '시군구'가 해당 목록에 포함된 행 삭제
df_korea_birth = df_korea_birth[~df_korea_birth['시군구'].isin(remove_sido)]
df_korea_birth
"""
st.code(code, language="python")

st.markdown(
  '''
  	시군구	합계출산율  
1	종로구	0.406  
2	중구	0.534  
3	용산구	0.547  
4	성동구	0.639  
5	광진구	0.449  
...	...	...  
272	함양군	0.734  
273	거창군	1.020  
274	합천군	0.636  
276	제주시	0.844  
277	서귀포시	0.767  
262 rows × 2 columns  
  '''
  )

st.markdown(
  '''
  ⇨ 포항시가 '포항-남구'와 '포함-북구' 행으로 나눠져있는 것을 확인하여 두 행의 평균값으로 '포항시'를 생성하고 기존 '포항-남구'와 '포항-북구'를 제거함 
  '''
  )

code="""
# '포항-남구'와 '포항-북구' 행을 합쳐서 평균을 구하기
df_korea_birth['시군구'] = df_korea_birth['시군구'].replace({'포항-남구': '포항', '포항-북구': '포항시'})

# '포항시'에 대한 '합계출산율' 평균을 구하고, 나머지 시군구는 그대로 두기
df_grouped = df_korea_birth.groupby('시군구', as_index=False)['합계출산율'].mean()

# '포항시'의 합계출산율을 구한 후, 기존 '포항-남구'와 '포항-북구'를 제거
df_korea_birth = df_korea_birth[~df_korea_birth['시군구'].isin(['포항-남구', '포항-북구'])]

# '포항시'에 대한 평균 합계출산율 값을 추가
df_korea_birth = pd.concat([df_korea_birth, df_grouped[df_grouped['시군구'] == '포항시']], ignore_index=True)

# 결과 확인
print(df_korea_birth)
"""
st.code(code, language="python")

st.markdown(
  '''
   시군구   합계출산율  
0     종로구  0.4060  
1      중구  0.5340  
2     용산구  0.5470  
3     성동구  0.6390  
4     광진구  0.4490  
..    ...     ...  
258   거창군  1.0200  
259   합천군  0.6360  
260   제주시  0.8440  
261  서귀포시  0.7670  
262   포항시  0.8615  
  
[263 rows x 2 columns]  
  '''
  )

st.write('#### 3. 시군구별 합계 출산율을 지도에 시각화하기')

st.markdown(
  '''
  - 1차 시각화
  '''
  )

code="""
!pip install folium
"""
st.code(code, language="python")

code="""
import folium

# 대한민국 중심 좌표
Korea = [36.5, 127.5]

# 타이틀 설정
title = '시군구별 출산율 지도'
title_html = f'<h3 align="center" style="font-size:20px"><b>{title}</b></h3>'

# 기본 지도 생성
sido_map = folium.Map(
    location=Korea,  # 대한민국 중심 좌표
    zoom_start=7,    # 전국 확대 정도
    tiles='cartodbpositron'
)

# 제목 추가
sido_map.get_root().html.add_child(folium.Element(title_html))

# Choropleth 맵 추가
folium.Choropleth(
    geo_data=gdf_korea_sigungu,  # GeoJSON 파일
    data=df_korea_birth,      # 데이터프레임
    columns=('시군구', '합계출산율'),  # Choropleth 매핑에 사용할 열
    key_on='feature.properties.시군구',  # GeoJSON의 속성과 매핑
    fill_color='BuPu',        # 색상 Blue-Purple
    fill_opacity=0.7,         # 채우기 투명도
    line_opacity=0.5,         # 경계선 투명도
    legend_name='시군구별 출산율'  # 범례 이름
).add_to(sido_map)

# 지도 출력
sido_map
"""
st.code(code, language="python")

st.image("시군구별 합계출산율 지도_1차.png", caption="시군구별 합계출산율 지도_1차", use_column_width=True)

st.markdown(
  '''
  ⇨ 지도에서 시각화되지 않은 부분이 있는 것을 확인함
  '''
  )

code="""
# '시군구' 매칭되지 않은 부분 찾기
unmatched_sigu = gdf_korea_sigungu[~gdf_korea_sigungu['시군구'].isin(df_korea_birth['시군구'])]

# 결과 출력
print("매칭되지 않은 시군구:", unmatched_sigu['시군구'].tolist())
"""
st.code(code, language="python")

st.markdown(
  '''
  매칭되지 않은 시군구: ['창원시'] 
  '''
  )

st.markdown(
  '''
  ⇨ '창원시'가 시각화되지 않은 것을 확인하여 시군구별 합계출산율 데이터셋에 '통합창원시'라고 표시되어있는 것을 '창원시'로 변경함
  '''
  )

code="""
# '통합창원시'를 '창원시'로 변경
df_korea_birth['시군구'] = df_korea_birth['시군구'].replace({'통합창원시': '창원시'})
"""
st.code(code, language="python")

st.markdown(
  '''
  - 최종 시각화
  '''
  )

code="""
import folium

# 대한민국 중심 좌표
Korea = [36.5, 127.5]

# 타이틀 설정
title = '시군구별 출산율 지도'
title_html = f'<h3 align="center" style="font-size:20px"><b>{title}</b></h3>'

# 기본 지도 생성
sido_map = folium.Map(
    location=Korea,  # 대한민국 중심 좌표
    zoom_start=7,    # 전국 확대 정도
    tiles='cartodbpositron'
)

# 제목 추가
sido_map.get_root().html.add_child(folium.Element(title_html))

# Choropleth 맵 추가
folium.Choropleth(
    geo_data=gdf_korea_sigungu,  # GeoJSON 파일
    data=df_korea_birth,      # 데이터프레임
    columns=('시군구', '합계출산율'),  # Choropleth 매핑에 사용할 열
    key_on='feature.properties.시군구',  # GeoJSON의 속성과 매핑
    fill_color='BuPu',        # 색상 Blue-Purple
    fill_opacity=0.7,         # 채우기 투명도
    line_opacity=0.5,         # 경계선 투명도
    legend_name='시군구별 출산율'  # 범례 이름
).add_to(sido_map)

# 지도 출력
sido_map
"""
st.code(code, language="python")

st.image("시군구별 합계출산율 지도_최종.png", caption="시군구별 합계출산율 지도_최종", use_column_width=True)
