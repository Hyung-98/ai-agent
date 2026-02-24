from agent import get_agent_response

def test_prompt_quality():
    print("[CI] Prompt Evaluation 시작...")
    sample_response = get_agent_response("지구는 왜 땅보다 바다가 더 넓은가요?")

    #
    if isinstance(sample_response, list) and sample_response and isinstance(sample_response[0], dict):
        text = sample_response[0].get("text", "")
    else:
        text = str(sample_response)
    
    if "[CONFIRMED]" in text:
        print("[CI] Prompt Evaluation 성공: [CONFIRMED] 태그가 포함되어 있습니다.")
        return True
    else:
        print("[CI] Prompt Evaluation 실패: [CONFIRMED] 태그가 포함되어 있지 않습니다.")
        return False