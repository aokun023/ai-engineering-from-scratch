import os
import anthropic

# 手动加载 .env 文件，而不是硬加载，防止 API KEY泄露
env_path = os.path.join(os.path.dirname(__file__), '.env')
with open(env_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            os.environ[key] = value

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("❌ 错误：没有找到 ANTHROPIC_API_KEY")
else:
    print("✅ 找到 ANTHROPIC_API_KEY")
    print(f"密钥前 10 位：{api_key[:10]}...")

    # 测试 API 调用
    try:
        client = anthropic.Anthropic(
            base_url="https://token-plan-cn.xiaomimimo.com/anthropic"
        )
        response = client.messages.create(
            model="mimo-v2.5",
            max_tokens=100,
            messages=[{"role": "user", "content": "Say hello in one sentence."}]
        )
        print("✅ API 调用成功！")
        # 遍历响应内容，找到文本块
        for block in response.content:
            if hasattr(block, 'text'):
                print(f"响应：{block.text}")
                break
    except Exception as e:
        print(f"❌ API 调用失败：{e}")
