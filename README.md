# Scrape Websites with Python & NoSQL
Python, Selenium, Requests HTML, Celery, FastAPI, & NoSQL을 사용한 웹스크래핑


사용되는 도구들:

- **Python 3.9** [다운](https://www.python.org/download/) - 사용 프로그래밍 언어
- **AstraDB** [회원가입](https://dtsx.io/3nQnjz1) - DataStax의 고성능 및 확장성 데이터베이스 서비스. AstraDB는 Cassandra NoSQL 데이터베이스입니다. [Cassandra](https://cassandra.apache.org/_/index.html) Netflix, Discord, Apple 및 기타 여러 회사에서 DataStax의 엄청난 양의 데이터베이스 서비스를 처리하는 데 사용합니다. AstraDB는 Cassandra NoSQL 데이터베이스입니다.
- **Selenium** [공식문서](https://selenium-python.readthedocs.io/) - 자동화된 웹 브라우징 :
  - 코드를 통해 모든 웹 브라우저 작업 실행
  - 자바스크립트가 많은 웹사이트 로드
  - 클릭, form submit, 로그인 등과 사용자 인터페이스 수행
- **Requests HTML** [공식문서](https://docs.python-requests.org/) - Selenium에서 추출한 HTML 문서를 구문 분석
- **Celery** [공식문서](https://docs.celeryproject.org/) - 스크래핑 하는 시기를 예약할 수 있는 작업자 precess를 제공합니다. precess queue로 [redis](https://redis.io/) 를 사용합니다.
- **FastAPI** [공식문서](https://fastapi.tiangolo.com/) - 웹 스크래핑 결과를 표시하고 모니터링하는 웹 애플리케이션 프레임워크



4파트로 구성:

- **Scraping** Selenium & Requests HTML을 사용하여 거의 모든 웹사이트에서 데이터를 스크랩하고 구문 분석하는 방법.
- **Data models** `cassandra-driver`, `pydantic` 및 **AstraDB**로 데이터를 저장하고 검증하는 방법.
- **Worker & Scheduling** Redis 및 AstraDB와 통합된 주기적 작업(예: 스크래핑)을 예약하는 방법
- **Presentation** 강력한 웹 애플리케이션 서비스로 위의 단계를 결합하는 방법


## Setup your syste
다음은 과정중 시스템이 완전히 설정되었는지 확인하기 위한 체크리스트입니다.    
모든 가이드와 설정은 이 저장소의 [setup](./setup) 디렉토리에서 찾을 수 있습니다.   

### checklist
- [] Install Selenium & Chromedriver - [setup guide](./setup/Install%20Selenium%20%26%20Chromedriver%20on%20your%20System.md)
- [] Install Redis  - [setup guide](./setup/Setup%20Redis.md)
- [] Create a virtual environment & install dependencies
- [] Setup an account with DataStax
- [] Create your first AstraDB and get API credentials
- [] Use `cassandra-driver` to verify your connection to AstraDB
