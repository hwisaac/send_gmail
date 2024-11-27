import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

# Gmail SMTP 서버 정보
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    body: str,
):
    """
    이메일을 보내는 함수
    :param sender_email: 발신자 이메일 주소
    :param sender_password: 발신자 이메일 비밀번호 (앱 비밀번호 권장)
    :param recipient_email: 수신자 이메일 주소
    :param subject: 이메일 제목
    :param body: 이메일 본문
    """
    # MIME 구성
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # SMTP 서버 연결 및 로그인
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # 보안 연결 시작
            server.login(sender_email, sender_password)
            # 이메일 전송
            server.send_message(message)
            print("이메일 전송 성공!")
    except Exception as e:
        print(f"이메일 전송 실패: {e}")


# 예제 호출
if __name__ == "__main__":
    # 발신자 정보
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

    # 수신자 정보
    RECIPIENT_EMAIL = "recipient_email@gmail.com"

    # 이메일 내용
    SUBJECT = "테스트 이메일"
    BODY = "이것은 Python을 사용하여 보낸 테스트 이메일입니다."

    # 함수 호출
    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, BODY)
