import os, time
from langchain_google_genai import ChatGoogleGenerativeAI
# 라이브러리 호출

# Agent의 응답을 생성하는 함수
def get_agent_response(user_input):
    # API 키를 환경 변수에서 가져옵니다. 실제로는 안전하게 관리해야 합니다.
    api_key = os.getenv("GOOGLE_API_KEY")
    print("API key exists?", bool(api_key))

    # Gemini 모델을 초기화하고 프롬프트를 설정합니다. 프롬프트에는 사용자의 질문과 함께 [CONFIRMED] 태그를 붙여달라는 요청이 포함되어 있습니다.
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", api_key=api_key)
    prompt = f"질문에 대해 답변하되, 반드시 마지막에 [CONFIRMED]를 붙여주세요: {user_input}"

    # Gemini 모델을 호출하여 응답을 생성합니다. 호출 전후로 시간을 출력하여 지연 시간을 확인할 수 있습니다.
    print("Calling Gemini...", time.strftime("%Y-%m-%d %H:%M:%S"))
    out = llm.invoke(prompt)
    print("Returned!", time.strftime("%Y-%m-%d %H:%M:%S"))

    return out.content