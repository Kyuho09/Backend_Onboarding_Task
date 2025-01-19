# Backend_Onboarding_Task

<br>

# 개발 기간
2025.01.18 ~ 2025.01.19

<br>

# 프로젝트 개요
Backend_Onboarding_Task는 Django를 활용하여 RESTful API를 개발하고, 배포 과정에서 필요한 모든 설정을 학습하기 위해 설계된 프로젝트입니다. 간단한 계정 관리 시스템과 인증, 그리고 Swagger 기반의 API 문서화까지 포함되어 있습니다.

<br>

# 개발 환경
|Programming Language| python 3.10|
|:----------------:|:----------------:|
| Web Framework | Django 4.2|
| Database | SQLite|
| IDE | Vscode |
| Version Control | Git, Github |
| Backend | Python, Django |
| Database | Django ORM, SQLite |
| HTTP Server | Gunicorn |
| Reverse Proxy | Nginx |

<br>

# 주요 기능
**회원가입 (Signup)**
- 사용자 정보를 받아 계정을 생성합니다.
- 비밀번호는 안전하게 해싱하여 저장합니다.

**로그인 (Login)**
- 사용자가 입력한 자격 증명을 통해 인증을 수행하고, JWT 토큰을 발급합니다.

**토큰 갱신 (Token Refresh)**
- Refresh Token을 사용해 새로운 Access Token을 발급받을 수 있습니다.

**Swagger UI 통합**
- API 명세서를 자동으로 생성하여 사용자 및 개발자가 쉽게 API를 테스트할 수 있도록 합니다.

<br>

# 기술적 의사결정
**Django REST Framework** : 

Django REST Framework는 강력한 Serializer와 뷰셋을 통해 API 개발을 효율적으로 할 수 있어 선택하였습니다.

**Swagger (drf-yasg)** : 

API 문서를 자동으로 생성하고 UI를 통해 테스트할 수 있어 개발 및 유지보수에 유리합니다.

**Gunicorn & Nginx** : 

배포 과정에서 Gunicorn은 WSGI 서버로, Nginx는 정적 파일 제공과 보안 강화를 위해 사용하였습니다.

<br>

# 기능 테스트
**Sign Up**:
![Sign Up](https://github.com/Kyuho09/Backend_Onboarding_Task/blob/main/images/Signin.png)

<br>

---

**Log In**:
![Log in](https://github.com/Kyuho09/Backend_Onboarding_Task/blob/main/images/login.png)

<br>

---

**Refresh Token**:
![Refresh Token](https://github.com/Kyuho09/Backend_Onboarding_Task/blob/main/images/refresh.png)

<br>

# 배포 URL
http://43.201.106.115/

<br>

---

# Django 기본 이해

### Django란 무엇인가?
Django는 파이썬으로 작성된 오픈소스 웹 프레임워크로, 웹 애플리케이션을 빠르게 개발하고 확장할 수 있도록 돕습니다. **MTV(Model-Template-View)** 구조를 기반으로 하며, 강력한 ORM(Object Relational Mapping)을 통해 데이터베이스와의 상호작용을 간단하게 처리할 수 있습니다. 또한, 보안 기능, 인증 시스템, 관리 인터페이스, URL 라우팅 등 웹 개발에 필요한 다양한 기능을 내장하고 있어 효율적인 개발이 가능합니다.

### Middleware란 무엇인가?
Middleware는 Django 애플리케이션에서 요청(Request)과 응답(Response) 사이에 처리되어야 할 작업을 정의하는 구성 요소입니다. 요청이 뷰(View)에 도달하기 전 또는 응답이 클라이언트에 도달하기 전에 특정 작업을 수행할 수 있도록 도와줍니다. 예를 들어, **인증, 세션 관리, 보안 기능** 등을 처리하는 데 사용됩니다.

---

## JWT 기본 이해

### JWT란 무엇인가?
JWT(Json Web Token)는 **JSON 포맷**으로 정보를 안전하게 주고받기 위한 토큰 기반 인증 메커니즘입니다. 클라이언트와 서버 간의 인증 정보를 포함하며, Base64로 인코딩되어 전달됩니다. 토큰은 크게 **Header(헤더)**, **Payload(내용)**, **Signature(서명)**로 구성됩니다.

- **Header**: 알고리즘과 토큰 유형을 명시
- **Payload**: 유저 정보 및 토큰의 데이터가 포함
- **Signature**: 토큰의 유효성을 검증하기 위해 생성된 서명

JWT는 주로 인증 및 권한 부여에 사용되며, **Stateless**하기 때문에 서버에서 세션을 유지할 필요 없이 빠르고 확장성이 높은 인증을 제공합니다.