# AI 프로젝트

## CCTV 이상행동 감지 서비스 만들기
- 기간 : 2020-09-10 ~ 2020-09-23 (2주)
- - -
### 개요 및 개발 필요성
- 인공지능이 CCTV 의 영상을 분석하고 , 이상행동을 감지하는 서비스
- 지능형 CCTV로 효율적으로 관리인력을 분배, 범죄상황에 대한 분석 및 대응을 자동화할 수 있다. 
- - -
### 데이터
- 수원시 이상행동 CCTV 데이터 
- https://aihub.or.kr/aidata/139/tool
- UCF 이상, 정상 영상 데이터 
- https://visionlab.uncc.edu/download/summary/60-data/477-ucf-anomaly-detection-dataset
- - -
### 전처리
![image](https://user-images.githubusercontent.com/66463059/102057232-f84bc680-3e30-11eb-847b-7d19dbc4122d.png)
- 각 영상(.mp4) 에서 16프레임단위로 fc6-1 데이터를 생성한다.
- 만들어진 데이터를 평균 내고 정규화 하여 C3D feature 텍스트를 추출한다.
- - -
### 모델 학습
##### 논문 참조 Real world Anomaly Detection in Surveillance VideosVideos(2018, Waqas Sultani Chen Chen)
![image](https://user-images.githubusercontent.com/66463059/102055494-4f03d100-3e2e-11eb-9679-1691b4f70c99.png)
- Real-world Anomaly Detection in Surveillance Videos(2018, Waqas Sultani, Chen Chen)의 모델 구조를 사용한다.
- 하나의 영상을 32개의 segment c3d feature로 나눈 결과를 bag에 넣으면 이런 세그먼트 하나하나가 bag instance가 된다. 
- 해당 instance는 mean, normalization을 통해 (1,4096)형태가 되고, 이를 모델에 넣어 각 bag instance의 이상행동 score를 정한다. 
- positive bag과 negative bag 안의 가장 높은 score를 가진 instance를 비교하여 positive bag instance의 score가 더 크다면 맞게 판단했고, negative bag instance의 score가 더 크다면 틀린 판단을 했다고 정의한다. 
- 손실함수를 통해 반복 학습하여 전체 손실을 줄이고 분류 정확성을 높인다.
- - -
### 요약 및 결론
![image](https://user-images.githubusercontent.com/66463059/102055902-e23d0680-3e2e-11eb-8044-e2367c153197.png)
- CCTV 영상에서 이상행동을 분류해 내는 기술을 웹에 서비스하고자 웹에서 영상을 입력했을 때, 해당 영상에서 이상행동을 탐지하고 그 발생시기를 시각화하여 영상을 분석할 수 있게 웹을 구현했다. 배포는 진행하지 않았다.
- - -
### ref
1. [https://github.com/WaqasSultani/AnomalyDetectionCVPR2018](https://github.com/WaqasSultani/AnomalyDetectionCVPR2018)
2. [https://github.com/dolongbien/HumanBehaviorBKU](https://github.com/dolongbien/HumanBehaviorBKU)


