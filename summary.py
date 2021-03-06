from pororo import Pororo
sum = Pororo(task="summary", lang="kr")

TXT = """LG전자가 인공지능(AI), 빅데이터, 코딩 등 소프트웨어(SW) 전문가를 오는 2023년까지 1000명 이상 육성할 계획이다.

이를 위해 LG전자(066570)는 최근 사내 경합을 통해 선발한 소프트웨어 전문가 51명을 대상으로 하는 소프트웨어 전문가 온라인 인증식을 지난 1일 진행했다고 밝혔다. 이날 선발된 AI, 빅데이터 전문가의 경우 서울대학교와 한국과학기술원(KAIST) 등 국내 대학과 미국 카네기멜론대학교, 캐나다 토론토대학교와 연계한 현업 중심 프로젝트를 수행해 왔다.

LG전자의 소프트웨어 전문가들은 경쟁력 있는 소프트웨어를 개발하고, 성능을 개선하며, 문제 해결을 주도하는 것 뿐만 아니라, 직원 멘토로서도 활동하게 된다. 또 LG전자 자체적인 기술 세미나를 열어 임직원 역량을 높이는 데 기여할 것으로 회사는 기대하고 있다.

현재 LG전자는 인공지능(AI) 전문가, 빅데이터 전문가, 코딩 전문가, 보안 전문가, 품질 전문가 등 다양한 사내 인증제도를 운영 중으로, 현재까지 500명의 전문가를 발굴했다. 회사 관계자는 "2023년까지 소프트웨어 전문가를 2배 수준으로 늘릴 계획"이라고 했다.

LG전자는 소프트웨어 전문가 인증 프로그램을 더 갈고 닦을 예정이다. 특히 AI 전문가 프로그램은 기존 해외 대학에 더해 미국 서던캘리포니아대, 뉴욕대 등과도 협업할 예정이다.

박일평 LG전자 최고기술책임자(CTO) 사장은 "미래 성장동력의 핵심인 소프트웨어 분야에서 탁월한 능력을 갖춘 전문가를 양성해 고객가치를 높이는데 집중할 것"이라고 했다."""

def summary(txt=TXT):
    return sum(txt)

if __name__ == "__main__":
    print(summary())


