# Daily Monitoring 

<br>

**[2023 동계 단기 현장실습]**  
오전 업무 : PC / MO 광고 모니터링  
➔ 자동화하기 위한 크롤링 코드 작성  
<br>
***
- PC 1차 완성 (2023.01.09)    
![브랜드 검색 링크 예시](https://user-images.githubusercontent.com/69826406/211487542-5707c497-c439-4b4d-b281-3b014bd2b187.png)
  - 속도가 아직 많이 느려 보완 필요 😭  
  - 모바일 버전도 작성 필요  
<br>

- Mobile 1차 완성 (2023.01.10)  
![브랜드 검색 예시 모바일](https://user-images.githubusercontent.com/69826406/211487683-eae2d42f-d2d9-45f5-9b58-2495c922fd07.png)
  - 속도가 아직 많이 느려 보완 필요 😭  
  <br>

- PC 보완 1차 (2023.01.11) 
 <br>

- PC 보완 2차 (2023.01.16)  
multiprocessing 모듈 사용  
➔ 각 프로세스마다 메인 URL 1개, 링크 체크용 URL 1개 동작하도록 설정 <br>

  - webdriver 버전 오류 해결하기 위해 ChromeDriverManager 사용한 set_chrome_driver 함수 추가
  - 이전보다 1분 가량 더 느려짐 이유가 뭘까...😵
  - 같은 키워드에 노출 소재가 여러 개인 경우 썸네일과 링크 내용이 일치하지 않는 문제 발생
